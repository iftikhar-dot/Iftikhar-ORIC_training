from user.models import User
from rest_framework import fields, serializers
from hostels.models import Hostel, Utilities
from contacts.models import *
from contacts.admin import *
from owners.models import Owner


class HostelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hostel
        fields = "__all__"


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"


class ContactsAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactAdmin
        fields = "__all__"


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UtilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilities
        fields = "__all__"
