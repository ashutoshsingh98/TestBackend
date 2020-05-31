from django.urls import path
from .views import activity_list, activity_detail

urlpatterns = [
    path('', activity_list),
    path('detail/<int:pk>/', activity_detail),
]

