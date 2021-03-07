from django.contrib import admin

# Register your models here.
from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from .models import Poem

class PoemAdmin(GuardedModelAdmin):
    list_display = ( 'author', 'title')
    search_fields = ('author', 'title')

admin.site.register(Poem, PoemAdmin)
