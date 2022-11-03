from django.urls import path
from . import views

urlpatterns = [
    path('',views.lead_list,name='lead_list'),
    path('create/',views.lead_create),
    path('<int:pk>/',views.lead_details,name='lead_detail'),
    path('<int:pk>/update/',views.lead_update,name='lead_update'),
    path('<int:pk>/delete/',views.lead_delete,name='lead_update'),
]
