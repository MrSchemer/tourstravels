from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import Contact
from blog.models import Post
from packages.models import package


def index(request):
    posts = Post.objects.all().order_by("-created_date")
    packages = package.objects.all().order_by("-created_date")
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            contact = form.save()

            # Send an email
            send_mail(
                subject=f"New Contact Form Submission from {contact.first_name} {contact.last_name}",
                message=f"Message:\n{contact.message}\n\nEmail: {contact.email}\nPhone: {contact.phone}",
                from_email='himalayenrasuwa@gmail.com',
                recipient_list=['bishal.lamichhane342@gmail.com'],
                fail_silently=False,
            )

            return redirect('success')
    else:
        form = Contact()
    return render(request, 'home/index.html', {'posts': posts, 'packages': packages, 'form': form})

def success_view(request):
    return render(request, 'home/success.html')
