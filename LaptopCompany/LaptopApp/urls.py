from django.urls import path
from .import views

urlpatterns = [
    path('add/',views.addorderView,name='add_order'),
    path('show',views.showordersView,name='show_order'),
    path('delete/<int:i>/',views.deleteorderview,name='delete_order'),
    path('update/<int:i>/',views.updateorderview,name='update_order'),

]