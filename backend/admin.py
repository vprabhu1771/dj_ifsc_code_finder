from multiprocessing.resource_tracker import register

from django.contrib import admin

from backend.models import Bank, Country, State, City, District


# Register your models here.
class BankAdmin(admin.ModelAdmin):
    list_display = ('name', 'code',)

    search_fields = ('name', 'code',)

admin.site.register(Bank, BankAdmin)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code',)

    search_fields = ('name', 'code',)

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('country', 'name', 'code',)

    search_fields = ('country', 'name', 'code',)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('state', 'name', 'code',)

    search_fields = ('state', 'name', 'code',)

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('city', 'name', 'code',)

    search_fields = ('city', 'name', 'code',)