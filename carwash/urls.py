from django.urls import path

from carwash.views import order_board, employee_list, base, washer_list, washer_detail, car_list

urlpatterns = [
    path('', order_board, name='carwash'),
    path('employees/', employee_list, name='employee_list'),
    path('base/', base, name='base'),
    path('base/washer_list', washer_list, name='washer_list'),
    path('base/washer/<int:washer_id>/', washer_detail, name='washer_detail'),
    path('base/car_list', car_list, name='car_list')
]
