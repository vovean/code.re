from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponseBadRequest, JsonResponse

from snippets.models import Snippet


def list_syntaxes(request: WSGIRequest):
    if request.method != 'GET':
        return HttpResponseBadRequest(f"Unacceptable method {request.method}")
    return JsonResponse(Snippet.SyntaxChoices.values, safe=False)
