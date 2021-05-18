# Generated by Django 3.2 on 2021-04-19 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='syntax',
            field=models.CharField(choices=[('C', 'Csrc'), ('CPP', 'Cppsrc'), ('C#', 'Csharp'), ('CSS', 'Css'), ('Common Lisp', 'Common Lisp'), ('Dockerfile', 'Dockerfile'), ('Erlang', 'Erlang'), ('GO', 'Go'), ('Groovy', 'Groovy'), ('Haskell', 'Haskell'), ('HTML', 'Html'), ('Java', 'Java'), ('JavaScript', 'Javascript'), ('JSON', 'Json'), ('TypeScript', 'Typescript'), ('Kotlin', 'Kotlin'), ('Lua', 'Lua'), ('Markdown', 'Markdown'), ('Objective C', 'Objectivec'), ('Pascal', 'Pascal'), ('Perl', 'Perl'), ('PHP', 'Php'), ('PowerShell', 'Powershell'), ('ProtoBuf', 'Protobuf'), ('Python', 'Python'), ('R', 'Rsrc'), ('Ruby', 'Ruby'), ('reStructuredText', 'Rst'), ('Rust', 'Rustsrc'), ('Sass', 'Sass'), ('Scala', 'Scala'), ('SCSS', 'Scss'), ('Shell', 'Sh'), ('Swift', 'Swift'), ('SQL', 'Sql'), ('LaTeX', 'Stex'), ('TOML', 'Toml'), ('VB.NET', 'Vb'), ('Vue.js app', 'Vue'), ('XML', 'Xml'), ('WebAssembly Text Format', 'Webassembly'), ('YAML', 'Yaml')], max_length=30),
        ),
    ]
