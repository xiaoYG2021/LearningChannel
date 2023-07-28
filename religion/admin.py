from django.contrib import admin

from .models import Token, Branch, Archbishop, Event

admin.site.register(Token)
admin.site.register(Branch)
admin.site.register(Archbishop)
admin.site.register(Event)
