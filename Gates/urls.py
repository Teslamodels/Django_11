from django.urls import path
from .views import Bill, Gates

urlpatterns = [
    path('', Bill.as_view(), name='bill'),
    path('gates/', Gates.as_view(), name='gates'),
]