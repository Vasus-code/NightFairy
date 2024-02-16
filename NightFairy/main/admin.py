from django.contrib import admin
from .models import Db, Rubric

class DbAdmin(admin.ModelAdmin):
	list_display = ('title', 'content', 'price', 'published', 'rubric')
	list_display_links = ('title', 'content', 'price')
	search_fields = ('title', 'content')


admin.site.register(Db, DbAdmin)
admin.site.register(Rubric)
