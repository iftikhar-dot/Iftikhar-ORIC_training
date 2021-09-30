from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


def contact(request):
    if request.method == "POST":
        hostel_id = request.POST["hostel_id"]
        hostel = request.POST["hostel"]
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        user_id = request.POST["user_id"]
        owner_email = request.POST["owner_email"]

        #  Check if user has made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                hostel_id=hostel_id, user_id=user_id
            )
            if has_contacted:
                messages.error(
                    request, "You have already made an inquiry for this hostel"
                )
                return redirect("/hostels/" + hostel_id)

        contact = Contact(
            hostel=hostel,
            hostel_id=hostel_id,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id,
        )

        contact.save()

        # Send email
        # send_mail(
        #   'Property hostel Inquiry',
        #   'There has been an inquiry for ' + hostel + '. Sign into the admin panel for more info',
        #   'traversy.brad@gmail.com',
        #   [owner_email, 'techguyinfo@gmail.com'],
        #   fail_silently=False
        # )

        messages.success(
            request,
            "Your request has been submitted, a owner will get back to you soon",
        )
        return redirect("/hostels/" + hostel_id)
