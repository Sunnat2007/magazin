from django.urls import path
from . import views

urlpatterns = [
    path('' , views.base , name='base'),
    path('iPhone/' , views.iphones , name='iphones'),
    path('iPhone/<slug:slug>/', views.iphone, name='iphone'),

    path('Nokia/' , views.nokias , name='nokias'),
    path('Nokia/<slug:slug>/', views.nokia, name='nokia'),

    path('Redmi/' , views.redmis , name='redmis'),
    path('Redmi/<slug:slug>/', views.redmi, name='redmi'),

    path('Other/' , views.others , name='others'),
    path('Other/<slug:slug>/', views.other, name='other'),
]