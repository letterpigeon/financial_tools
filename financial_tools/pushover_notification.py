import requests
import os


def send_pushover_notification(message: str) -> None:
    """
    Prerequisites:
    1. Create an account at https://pushover.net/
    2. Create an application at https://pushover.net/apps/build
    3. Get the API token and user key
    4. Set the API token and user key as environment variables: PUSHOVER_API_TOKEN and PUSHOVER_USER_KEY

    :param message:
    :return:
    """
    token = os.getenv('PUSHOVER_API_TOKEN')
    user = os.getenv('PUSHOVER_USER_KEY')
    url = 'https://api.pushover.net/1/messages.json'
    data = {
        'token': token,
        'user': user,
        'message': message
    }
    requests.post(url, data=data)


if __name__ == '__main__':
    send_pushover_notification('Hello again')
