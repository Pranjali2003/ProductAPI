from django.db import models
from django.utils import timezone
import uuid
# Create your models here.

class ProductTable(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,serialize=False)
    sku=models.CharField(unique=True,max_length=10,editable=False,blank=False)
    name=models.CharField(max_length=100,blank=False)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2,blank=False)
    category=models.CharField(max_length=100,blank=False)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
