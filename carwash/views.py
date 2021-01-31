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
    employees = Employee.objects.all()
    for emp in employees:
        emp_orders = Order.objects.filter(washer=emp, end_date__gt=timezone.now()-timezone.timedelta(weeks=1)).count()
        orders[emp] = [emp_orders]
        orders[emp].append(Order.objects.filter(washer=emp, end_date__gt=last_month).count())
        orders[emp].append(Order.objects.filter(washer=emp, end_date__gt=last_year).count())
    return render(
        request,
        'carwash/employee_list.html',
        context={
            'orders': orders,
        })
