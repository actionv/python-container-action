import requests

from actions_toolkit import core


def main():
    requests.get('https://httpbin.org/get?code=0')
    username = core.get_input('username')
    res = f"Hello {username}"
    core.set_output(res)


if __name__ == "__main__":
    main()
