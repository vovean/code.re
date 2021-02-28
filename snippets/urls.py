from django.urls import path

from snippets.views import syntaxes

urlpatterns = [
    path('syntaxes', syntaxes.list_syntaxes)
]
