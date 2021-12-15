import requests

from actions_toolkit import core

from actions_toolkit.context import Context


def main():
    requests.get('https://httpbin.org/get?code=0')
    username = core.get_input('username', required=True)
    res = f"Hello {username}"
    core.set_output('res', res)
    context = Context()
    print(context)
    print(context.payload)


if __name__ == "__main__":
    main()
