from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login, name = 'login'),
    path('home/', views.index, name='ShopHome'),  
    path('about/', views.about, name='about'),  
    path('contact/', views.contact, name='contact'),  
    path('tracker/', views.tracker, name='tracker'),  
    path('logout/', views.logout, name = 'logout'),
    path('search/', views.search, name='search'),  
    path('products/<int:myid>', views.productView, name='productView'),
    path('checkout', views.checkout, name='checkout'),
    
]