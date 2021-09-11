from urllib.parse import urlencode
BASE_URL = "https://api.thinkific.com/api"
ADMIN_API_URL = "/public/v1"
WEBHOOKS_API_URL = "/v2"

def cleanParams(params: dict):
    return {k: v for k, v in params.items() if v}


def mergeURL(url: str, params: dict):
    if params and len(params) > 0:
        return url+'?'+urlencode(cleanParams(params))
    return url
