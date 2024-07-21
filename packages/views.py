from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.core.mail import send_mail
from .models import package, booking
from .forms import Booking

def packages(request):
    packages = package.objects.all().order_by("-created_date")
    return render(request, 'packages/packages.html', {"packages": packages})

def details(request, pk):
    packages = get_object_or_404(package, pk=pk)
    other_packages = package.objects.exclude(pk=pk).order_by("-created_date")
    return render(request, 'packages/detail.html', {"package": packages, "other_packages": other_packages})

def book(request, pk):
    packages  = get_object_or_404(package, pk=pk)
    
    if request.method == 'POST':
        
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        pickup_location = request.POST.get('pickup_location')
        number_of_people = int(request.POST.get('number_of_people'))
        additional_preference = request.POST.get('additional_preference')
        date_start_trip = request.POST.get('date_start_trip')
        
        # Calculate total price

        total_price = number_of_people * packages.price
        if number_of_people > 5:
            total_price *= 0.9  # Apply 10% discount
        
        book = booking.objects.create(
            package=packages,
            Firstname=first_name,
            middle_name=middle_name,
            lastname=last_name,
            email=email,
            phone=phone,
            address=address,
            pickup_location=pickup_location,
            total_person=number_of_people,
            total_price=total_price,
            additional_prefrences=additional_preference
        )

        send_mail(
            subject=f"New Booking for {packages.title}",
            message=f"Name: {first_name} {middle_name} {last_name}\nEmail: {email}\nPhone: {phone}\nAddress: {address}\nPickup Location: {pickup_location}\nNumber of People: {number_of_people}\nTotal Price: {total_price}\nAdditional Preferences: {additional_preference}\nDate of Trip: {date_start_trip}",
            from_email='himalayenrasuwa@gmail.com',
            recipient_list=['bishal.lamichhane342@gmail.com'],
            fail_silently=False)

        
        return redirect(reverse('booking_success', args=[book.id]))
    
    return render(request, 'packages/form.html', { 'package': packages})

def booking_success(request, pk):
    booking1 = get_object_or_404(booking, pk=pk)
    return render(request, 'packages/success.html', {'booking': booking1})
