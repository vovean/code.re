import json

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404

from snippets.models import Snippet


def get_snippet(request: WSGIRequest, link: str):
    if request.method != "GET":
        return HttpResponseBadRequest(f"Unacceptable method {request.method}")
    snippet = get_object_or_404(Snippet, link=link)
    return JsonResponse(snippet.as_dict())


def create_update_snippet(request: WSGIRequest):
    if request.method not in ["POST", "PATCH"]:
        return HttpResponseBadRequest(f"Unacceptable method {request.method}")
    if request.method == "POST":
        return create_snippet(request)
    else:
        return update_snippet(request)


def create_snippet(request: WSGIRequest):
    data: dict = json.loads(request.body.decode("utf-8"))
    for field in data:
        if field not in ['syntax', 'code', 'link_mode']:
            data.pop(field)
    snippet = Snippet.objects.create(**data)
    return JsonResponse({
        "snippet": snippet.as_dict(),
        "token": str(snippet.token)
    })


def update_snippet(request: WSGIRequest):
    ...
