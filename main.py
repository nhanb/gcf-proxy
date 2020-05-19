import os

import requests

PASSWORD = os.environ["GCFPROXY_PASSWORD"]
PROXIABLE_METHODS = {
    "get": requests.get,
    "post": requests.post,
}


def nhansproxy(request):
    if request.method != "POST":
        return ("POST only!", 405)

    req = request.json

    if type(req) is not dict:
        return ("Must have JSON body!", 400)

    fields = ("method", "password", "url", "body")
    missing_fields = [f for f in fields if f not in req]
    if missing_fields:
        return (f"Missing fields: {missing_fields}", 400)

    if req.get("password") != PASSWORD:
        return ("Get off my lawn!", 400)

    if req["method"] not in PROXIABLE_METHODS:
        return ("We serve get/post only!", 400)

    requests_func = PROXIABLE_METHODS[req["method"]]
    requests_kwargs = {"url": req["url"], "headers": req["headers"]}
    if req["method"] == "post":
        requests_kwargs["body"] = req["body"]

    try:
        resp = requests_func(**requests_kwargs, timeout=10)
    except Exception as e:
        return (f"Unexpected error:\n{e}", 500)

    return (resp.text, resp.status_code)
