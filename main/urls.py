from django.urls import path

from main.views import contact

urlpatterns = [
    path('', contact)
]
