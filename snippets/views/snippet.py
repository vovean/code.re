import json

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods

from snippets.models import Snippet


@require_http_methods(["GET"])
def get_snippet(request: WSGIRequest, link: str):
    snippet = get_object_or_404(Snippet, link=link)
    return JsonResponse(snippet.as_dict())


@require_http_methods(["POST", "PATCH"])
def create_update_snippet(request: WSGIRequest):
    if request.method == "POST":
        return _create_snippet(request)
    else:
        return _update_snippet(request)


def _create_snippet(request: WSGIRequest):
    data: dict = json.loads(request.body.decode("utf-8"))
    for field in data:
        if field not in ['syntax', 'code', 'link_mode']:
            data.pop(field)
    snippet = Snippet.objects.create(**data)
    return JsonResponse({
        "snippet": snippet.as_dict(),
        "token": str(snippet.token)
    })


def _update_snippet(request: WSGIRequest):
    data: dict = json.loads(request.body.decode("utf-8"))
    snippet = get_object_or_404(Snippet, token=data.get("token", ""))
    required_fields = ("code", "syntax")
    if not all(i in data for i in required_fields):
        return HttpResponseBadRequest("Missing fields")
    for i in required_fields:
        if data[i] is None:
            continue
        setattr(snippet, i, data[i])
    snippet.save()
    return HttpResponse("ok")


@require_http_methods(["PATCH"])
def change_mode(request, link: str):
    data: dict = json.loads(request.body.decode("utf-8"))
    snippet = get_object_or_404(Snippet, token=data.get("token", ""), link=link)
    Snippet.objects.change_link_mode_for(snippet)
    return HttpResponse(snippet.link)
