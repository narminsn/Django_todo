from django.contrib import admin
from .models import TodoModel
# Register your models here.

class ModelsAdmin(admin.ModelAdmin):
    list_display=("title","description","status")

admin.site.register(TodoModel, ModelsAdmin)