from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from hostels.models import Hostel
from contacts.models import *
from contacts.admin import *
from rest_framework import fields, serializers
from owners.models import Owner
from user.models import User

# Create your views here.
class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactsSerializer


class HostelList(generics.ListCreateAPIView):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer


class HostelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer


class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactsSerializer


class OwnerList(generics.ListCreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class OwnerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UtilitiesList(generics.ListCreateAPIView):
    queryset = Utilities.objects.all()
    serializer_class = UtilitiesSerializer


class UtilitiesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Utilities.objects.all()
    serializer_class = UtilitiesSerializer
