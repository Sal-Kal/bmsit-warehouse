from django.contrib import admin

# Register your models here.

from .models import conference, journal, book

admin.site.register(conference)
admin.site.register(journal)
admin.site.register(book)