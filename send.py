#!/usr/bin/env python3
import os
import sys
from datetime import datetime as dt

import requests

"""
Lazy quick test script
"""

PASSWORD = os.environ["GCFPROXY_PASSWORD"]


def run():
    start = dt.now()
    resp = requests.post(
        "https://asia-northeast1-nhansproxy.cloudfunctions.net/nhansproxy",
        json={
            "url": "https://httpbin.org/ip",
            "method": "get",
            "body": None,
            "headers": {"Foo-Bar": "ehhhh"},
            "password": PASSWORD,
        },
    )

    """
    print(resp.status_code)
    for hkey, hval in resp.headers.items():
        print(hkey, ":", hval)
    """
    end = dt.now()
    print(resp.status_code)
    print(resp.text)
    print((end - start).total_seconds())


def loop():
    while True:
        run()


if len(sys.argv) == 2 and sys.argv[1] == "loop":
    loop()
else:
    run()
