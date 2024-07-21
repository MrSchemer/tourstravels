from django.db import models

class package(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200, default="Nepal")
    difficulty = models.CharField(max_length=200, default="Easy")
    itinerary = models.TextField(null=True, blank=True)
    price = models.IntegerField()
    image = models.ImageField(upload_to='static/packages/images/', blank=True, null=True)
    created_date = models.DateTimeField()
    IsFeatured = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class booking(models.Model):
    id = models.AutoField(primary_key=True)
    package = models.ForeignKey(package, on_delete=models.CASCADE)
    Firstname = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    pickup_location = models.CharField(max_length=200, default="Kathmandu")
    booking_date = models.DateTimeField(auto_now_add=True)
    total_person = models.IntegerField()
    total_price = models.IntegerField()
    additional_prefrences = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=200, default="Pending")

    def __str__(self):
        return f"{self.Firstname} {self.lastname}, {self.email}"
