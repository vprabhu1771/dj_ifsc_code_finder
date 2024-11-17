from django.contrib import admin

from backend.models import Bank


# Register your models here.
class BankAdmin(admin.ModelAdmin):
    list_display = ('name', 'code',)

    search_fields = ('name', 'code',)

admin.site.register(Bank, BankAdmin)