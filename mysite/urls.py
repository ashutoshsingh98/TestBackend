from django.urls import path
from .views import activity_list, activity_detail

urlpatterns = [
    path('activity/', activity_list),
    path('detail/<int:pk>/', activity_detail),
]

# urlpatterns = [
#     path('', views.home, name='home'),
# ]