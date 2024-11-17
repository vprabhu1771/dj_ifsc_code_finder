from multiprocessing.resource_tracker import register

from django.contrib import admin

from backend.models import Bank, Country


# Register your models here.
class BankAdmin(admin.ModelAdmin):
    list_display = ('name', 'code',)

    search_fields = ('name', 'code',)

admin.site.register(Bank, BankAdmin)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code',)

    search_fields = ('name', 'code',)