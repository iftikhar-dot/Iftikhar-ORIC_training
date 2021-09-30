from django.contrib import admin

from .models import Hostel


class HostelAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "is_published", "price", "list_date", "owner")
    list_display_links = ("id", "title")
    list_filter = ("owner",)
    list_editable = ("is_published",)
    search_fields = (
        "title",
        "description",
        "address",
        "city",
        "state",
        "zipcode",
        "price",
    )
    list_per_page = 25


admin.site.register(Hostel, HostelAdmin)
