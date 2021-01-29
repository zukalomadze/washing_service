from django.shortcuts import render
from carwash.models import Orders
from django.utils import timezone

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


# def employee_list(request):
#     orders = Orders.objects.all()
#     return render(
#         request,
#         'carwash/tickets.html',
#         context={
#             'orders': orders
#         })
