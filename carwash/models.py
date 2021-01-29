from django.db import models
from carwash.choices import CarChoice


# Create your models here.
class CarWash(models.Model):
    name = models.CharField(verbose_name="Company Name", max_length=255)
    location = models.OneToOneField(to="carwash.Location", on_delete=models.PROTECT, related_name='company')
    supplier = models.ManyToManyField(to='carwash.Supplier', related_name='company')

    class Meta:
        verbose_name = 'Car Wash'
        verbose_name_plural = 'Car Washes'

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(verbose_name="Name", max_length=255)
    company = models.ForeignKey(to="carwash.CarWash", on_delete=models.CASCADE, related_name='employee')
    salary = models.DecimalField(default=0.0, decimal_places=2, max_digits=5)

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'

    def __str__(self):
        return self.name

    def salary_display(self):

        return '${0}'.format(self.salary)

    salary_display.short_description = 'Salary'


class Booth(models.Model):
    booth_number = models.CharField(verbose_name="Booth Number", max_length=255)  # ბოქსების სახელი იწერება 01
    occupied = models.BooleanField(verbose_name="Occupied", default=False)
    company = models.ForeignKey(to="carwash.CarWash", on_delete=models.CASCADE, related_name='booth')

    class Meta:
        verbose_name = 'Booth'
        verbose_name_plural = 'Booths'
        unique_together = ('company', 'booth_number')

    def __str__(self):
        return self.booth_number


class Car(models.Model):
    brand = models.CharField(verbose_name="Car Brand", max_length=255)
    license_plate = models.CharField(verbose_name="License Plate", max_length=255)
    car_type = models.PositiveSmallIntegerField(choices=CarChoice.choices, default=CarChoice.Sedan)

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return f'{self.brand}: {self.license_plate.upper()}'


class Location(models.Model):
    city = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    zip = models.CharField(max_length=7)

    class Meta:
        verbose_name = 'Location'
        verbose_name_plural = 'Locations'

    def __str__(self):
        return f'{self.city} : {self.street_address}: {self.zip}'


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    location = models.OneToOneField(to="carwash.Location", on_delete=models.PROTECT, related_name='supplier')

    class Meta:
        verbose_name = 'Supplier'
        verbose_name_plural = 'Suppliers'

    def __str__(self):
        return self.name


class Inventory(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=8)
    company = models.ForeignKey(to='carwash.Supplier', related_name='inventory', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Inventory'
        verbose_name_plural = 'Inventories'

    def __str__(self):
        return self.name


class Orders(models.Model):

    booth = models.ForeignKey(to='carwash.Booth', related_name='orders', on_delete=models.CASCADE)
    start_time = models.DateTimeField(verbose_name='Start time')
    end_time = models.DateTimeField(verbose_name='End time', blank=True, null=True)
    car = models.ForeignKey(to='carwash.Car', on_delete=models.CASCADE, related_name="orders")
    price = models.DecimalField(default=0.0, decimal_places=2, max_digits=5)
    washer = models.ForeignKey(to='carwash.Employee', on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    create_time = models.DateTimeField(verbose_name="Create time", auto_now_add=True)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = " Orders"

    def __str__(self):
        return f"order: {self.pk}"

    def save(self, *args, **kwargs):
        self.price = self.car.car_type
        super(Orders, self).save(*args, **kwargs)
