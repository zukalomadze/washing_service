from django.urls import path

from carwash.views import order_board, employee_list, base, washer_list

urlpatterns = [
    path('', order_board, name='carwash'),
    path('employees/', employee_list, name='employee_list'),
    path('base/', base, name='base'),
    path('base/washer_list', washer_list, name='washer_list')
]
