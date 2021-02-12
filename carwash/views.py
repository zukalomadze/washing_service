from django.db.models import Count, Sum
from django.http import Http404
from django.shortcuts import render
from carwash.models import Order
from user.models import User as Employee
from django.utils import timezone
from django.core.paginator import Paginator
import dateutil.relativedelta
from .models import Order, Car

from .forms import CarForm
# Create your views here.


def order_board(request):
    one_hour_ago = timezone.now() - timezone.timedelta(hours=1)
    orders = Order.objects.filter(end_date__gt=one_hour_ago) | Order.objects.filter(end_date=None)
    orders = orders.order_by('start_date')
    return render(
        request,
        'carwash/tickets.html',
        context={
            'orders': orders
        })


def employee_list(request):
    now = timezone.now()
    last_month = now + dateutil.relativedelta.relativedelta(months=-1)
    last_year = now + dateutil.relativedelta.relativedelta(years=-1)
    orders = {}
    employees = Employee.objects.filter(status=Employee.Status.washer)
    for emp in employees:
        emp_orders = Order.objects.filter(employee=emp,
                                          end_date__gt=timezone.now() - timezone.timedelta(weeks=1)).count()
        orders[emp] = [emp_orders]
        orders[emp].append(Order.objects.filter(employee=emp, end_date__gt=last_month).count())
        orders[emp].append(Order.objects.filter(employee=emp, end_date__gt=last_year).count())
    return render(
        request,
        'carwash/employee_list.html',
        context={
            'orders': orders,
        })


def washer_list(request):
    washers = Employee.objects.filter(status=Employee.Status.washer).annotate(washed_count=Count('orders'))
    return render(
        request,
        'carwash/washer_list.html',
        context={
            'washers': washers
        },
    )


def base(request):
    return render(
        request,
        'carwash/base.html',
        context={},
    )


def washer_detail(request, washer_id):
    length = request.GET.get('length')
    try:
        washer = Employee.objects.get(pk=washer_id)
        if length == 'week':
            orders = Order.objects.filter(employee=washer,
                                          end_date__gt=timezone.now() - timezone.timedelta(weeks=1))
        elif length == 'month':
            orders = Order.objects.filter(employee=washer,
                                          end_date__gt=timezone.now() - timezone.timedelta(days=30))
        elif length == 'year':
            orders = Order.objects.filter(employee=washer,
                                          end_date__gt=timezone.now() - timezone.timedelta(days=365))
        else:
            orders = Order.objects.filter(employee=washer)
        if len(orders):
            sum_prices = orders.aggregate(Sum('price'))['price__sum']

            commission = sum_prices * (washer.cut / 100)
        else:
            commission = 0
    except Employee.DoesNotExist:
        raise Http404("Question does not exist")
    return render(
        request,
        'carwash/employee_detail.html',
        context={
            'washer': washer,
            'length': length,
            'commission': commission,
            'orders': orders,
        }
    )


def car_list(request):
    cars_list = Car.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(cars_list, 10)
    cars = paginator.page(page)

    car_form = CarForm()
    if request.method == 'POST':
        car_form = CarForm(request.POST)
        if car_form.is_valid():
            car: Car = car_form.save(commit=False)
            car.save()
            car_form = CarForm()
    return render(request, 'carwash/cars.html', context={'cars': cars, 'form': car_form})
