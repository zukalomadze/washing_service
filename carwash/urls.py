from django.urls import path

from carwash.views import order_board, employee_list, base, washer_list, washer_detail

urlpatterns = [
    path('', order_board, name='carwash'),
    path('employees/', employee_list, name='employee_list'),
    path('base/', base, name='base'),
    path('base/washer_list', washer_list, name='washer_list'),
    path('base/washer/<int:washer_id>/', washer_detail, name='washer_detail')
]
