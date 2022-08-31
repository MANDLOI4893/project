from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.index, name='home'),
  path('invite/', views.cart, name='cart'),
  path('viewcard/<str:slug>', views.viewcard, name='view'),
  path('contact/', views.contact_us, name='contact_us'),
   path('faq/', views.faqs, name='faq'),
]
