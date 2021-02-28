from django.urls import path

from snippets.views import syntaxes, snippet

urlpatterns = [
    path('syntaxes', syntaxes.list_syntaxes),
    path('snippet', snippet.create_update_snippet),
    path('snippet/<str:link>', snippet.get_snippet),
]
