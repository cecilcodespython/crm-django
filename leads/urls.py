from django.urls import path
from . import views

urlpatterns = [
    path('',views.lead_list,name='lead_list'),
    path('<pk>/',views.lead_details)
]
