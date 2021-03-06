from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import price_choices, bedroom_choices, state_choices

from .models import Hostel


def index(request):
    hostels = Hostel.objects.order_by("-list_date").filter(is_published=True)

    paginator = Paginator(hostels, 6)
    page = request.GET.get("page")
    paged_hostels = paginator.get_page(page)

    context = {"hostels": paged_hostels}
    print(paged_hostels)
    return render(request, "hostels/hostels.html", context)


def hostel(request, hostel_id):
    hostel = get_object_or_404(Hostel, pk=hostel_id)

    context = {"hostel": hostel}

    return render(request, "hostels/hostel.html", context)


def search(request):
    queryset_list = Hostel.objects.order_by("-list_date")

    # Keywords
    if "keywords" in request.GET:
        keywords = request.GET["keywords"]
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City
    if "city" in request.GET:
        city = request.GET["city"]
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # State
    if "state" in request.GET:
        state = request.GET["state"]
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)

    # Bedrooms
    if "bedrooms" in request.GET:
        bedrooms = request.GET["bedrooms"]
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

    # Price
    if "price" in request.GET:
        price = request.GET["price"]
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        "state_choices": state_choices,
        "bedroom_choices": bedroom_choices,
        "price_choices": price_choices,
        "hostels": queryset_list,
        "values": request.GET,
    }

    return render(request, "hostels/search.html", context)
