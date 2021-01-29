from django.shortcuts import render
from carwash.models import Orders, Employee
from django.utils import timezone
import dateutil.relativedelta
# Create your views here.


def order_board(request):
    one_hour_ago = timezone.now()-timezone.timedelta(hours=1)
    orders = Orders.objects.filter(end_time__gt=one_hour_ago) | Orders.objects.filter(end_time=None)
    orders = orders.order_by('start_time')
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
        emp_orders = Orders.objects.filter(washer=emp, end_time__gt=timezone.now()-timezone.timedelta(weeks=1)).count()
        orders[emp] = [emp_orders]
        orders[emp].append(Orders.objects.filter(washer=emp, end_time__gt=last_month).count())
        orders[emp].append(Orders.objects.filter(washer=emp, end_time__gt=last_year).count())
    return render(
        request,
        'carwash/employee_list.html',
        context={
            'orders': orders,
        })
