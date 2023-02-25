from django.contrib import admin

from document.models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    pass
