import os
import requests


def main():
    requests.get('https://httpbin.org/get?code=0')
    username = os.environ["INPUT_USERNAME"]
    res = f"Hello {username}"
    print(f"::set-output name=res::{res}")


if __name__ == "__main__":
    main()
