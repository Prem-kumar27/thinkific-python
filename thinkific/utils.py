from urllib.parse import urlencode
BASE_URL = "https://api.thinkific.com/api/public/v1"


def cleanParams(params: dict):
    return {k: v for k, v in params.items() if v}


def mergeURL(url: str, params: dict):
    if params and len(params) > 0:
        return url+'?'+urlencode(cleanParams(params))
    return url
