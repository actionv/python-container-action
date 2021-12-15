from datetime import datetime, timezone, timedelta

import requests
from actions_toolkit import core
from actions_toolkit.context import Context


def main():
    requests.get('https://httpbin.org/get?code=0')
    username = core.get_input('username')
    res = f"Hello {username}"
    core.info("test")
    core.set_command_echo(True)
    core.set_output('res', res)
    tz = timezone(timedelta(hours=+8))
    time = datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')
    print(f"::set-output name=time::{time}")
    context = Context()
    print(context)
    print(context.payload)


if __name__ == "__main__":
    main()
