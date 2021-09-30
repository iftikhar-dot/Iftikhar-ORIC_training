from django.shortcuts import render
from django.http import HttpResponse
from hostels.choices import price_choices, bedroom_choices, state_choices

from hostels.models import Hostel
from owners.models import Owner


def index(request):
    hostels = Hostel.objects.order_by("-list_date").filter(is_published=True)[:3]

    context = {
        "hostels": hostels,
        "state_choices": state_choices,
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
    }

    return render(request, "pages/index.html", context)


def about(request):
    # Get all owners
    owners = Owner.objects.order_by("-hire_date")

    # Get MVP
    mvp_owners = Owner.objects.all().filter(is_mvp=True)

    context = {"owners": owners, "mvp_owners": mvp_owners}

    return render(request, "pages/about.html", context)
