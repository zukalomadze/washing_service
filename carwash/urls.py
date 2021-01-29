from django.urls import path

from carwash.views import order_board, employee_list

urlpatterns = [
    path('', order_board, name='carwash'),
    path('employees', employee_list, name='employee_list')
]
