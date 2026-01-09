from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'phone', 'email', 'show',
    ordering = '-id', 'first_name', 'phone', 'last_name',
    # list_filter = 'created_date', 'phone',
    search_fields = 'first_name', 'last_name', 'phone', 'email',
    list_per_page = 10
    list_max_show_all = 20
    list_editable = 'first_name', 'last_name', 'show',
    # list_display_links = 'first_name',

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    ordering = '-id',
