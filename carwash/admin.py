from django.contrib import admin
from carwash.models import CarWash, Employee, Booth, Location, Car, Supplier, Inventory
# Register your models here.


class BoothInline(admin.TabularInline):
    model = Booth
    extra = 0
    readonly_fields = ['occupied']
    list_display = ('booth_number', 'occupied', 'washer', 'car')


class InventoryInLine(admin.TabularInline):
    model = Inventory
    extra = 1
    list_display = ('name', 'price')


@admin.register(CarWash)
class CarWashAdmin(admin.ModelAdmin):
    inlines = [BoothInline]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'salary_display', 'company')


@admin.register(Booth)
class BoothAdmin(admin.ModelAdmin):
    readonly_fields = ['occupied']


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    inlines = [InventoryInLine]


@admin.register(Car, Location, Inventory)
class LocationAdmin(admin.ModelAdmin):
    pass
