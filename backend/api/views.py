import json
from django.http import JsonResponse


def api_home(request, *args, **kwargs):
    # request -> HttpRequest -> Django
    # print(dir(request))
    print(request)

    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body) # strings of JSON - dict
    except:
        pass
    print(data)
    print(data.keys())

    print(request.headers)
    print(request.GET) # url query params

    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    data['params'] = dict(request.GET)

    return JsonResponse(data)
