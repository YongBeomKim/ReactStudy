from .models import Person
import django_tables2 as tables

class PersonTable(tables.Table):
    first_name = tables.Column(linkify=True)
    last_name  = tables.Column(linkify=True)

    class Meta:
        model = Person
        template_name = "django_tables2/bootstrap.html"
