from django.db import models

# Create your models here.

class Quote(models.Model):
    quote_author = models.CharField(max_length=50)
    quote_body = models.TextField()
    context = models.CharField(blank=True, max_length=240)
    source = models.CharField(blank=True, max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.quote_author
    