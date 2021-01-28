from django.contrib import admin
from carwash.models import CarWash, Employee, Booth, Location, Car, Supplier, Inventory, Orders
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

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


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


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    ordering = ('start_time',)
    readonly_fields = ['price']
    list_display = ('booth', 'washer', 'start_time', 'end_time', 'car', 'price')
