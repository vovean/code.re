import uuid

from django.db import models
# Create your models here.
from django.db.models import TextChoices


class Snippet(models.Model):
    class SyntaxChoices(TextChoices):
        BASH = "Bash"
        C = "C"
        C_SHARP = "C#"
        CPP = "C++"
        CSS = "CSS"
        HTML = "HTML"
        JSON = "JSON"
        JAVA = "Java"
        JAVASCRIPT = "JavaScript"
        LUA = "Lua"
        OBJECTIVE_C = "Objective C"
        PHP = "PHP"
        PERL = "Perl"
        PYTHON = "Python"
        RUBY = "Ruby"
        SWIFT = "Swift"

    created_at = models.DateTimeField(auto_now_add=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    syntax = models.CharField(max_length=20, choices=SyntaxChoices.choices)
    code = models.TextField()
    link = models.CharField(max_length=8, unique=True)
