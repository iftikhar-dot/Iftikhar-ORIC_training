from django.urls import path,include

from . import views

urlpatterns = [
  path('contact', views.contact, name='contact'),
  path('contactsEp/', include('api.urls')),
]