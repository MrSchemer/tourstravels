from django.db import models

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='static/blog/images/', blank=True, null=True)
    created_date = models.DateTimeField()
    IsFeatured = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title
    
    
