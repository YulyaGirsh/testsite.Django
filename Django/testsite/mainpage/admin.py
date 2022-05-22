from django.contrib import admin
from .models import Places, Categories


class PlacesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'creates_at', 'is_published', 'category']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'content']
    list_editable = ['is_published']
    list_filter = ['is_published', 'category']


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', ]
    list_display_links = ['id', 'title']
    search_fields = ['id', 'title']


admin.site.register(Places, PlacesAdmin)
admin.site.register(Categories, CategoriesAdmin)
