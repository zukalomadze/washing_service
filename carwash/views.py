from django.db.models import Count
from django.shortcuts import render
from carwash.models import Order
from user.models import User as Employee
from django.utils import timezone
import dateutil.relativedelta
# Create your views here.


def order_board(request):
    one_hour_ago = timezone.now()-timezone.timedelta(hours=1)
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
        emp_orders = Order.objects.filter(employee=emp, end_date__gt=timezone.now()-timezone.timedelta(weeks=1)).count()
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
