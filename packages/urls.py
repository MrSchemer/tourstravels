from django.urls import path
from . import views

urlpatterns = [
    path('', views.packages, name='packages'),
    path('<int:pk>', views.details, name='package_details'),
    path('book/<int:pk>', views.book, name='book'),
    path('booking_success/<int:pk>', views.booking_success, name='booking_success'),
]