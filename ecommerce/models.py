from django.db import models

# Create your models here.

class EcommIntegration(models.Model):
    STATUS_CHOICES = [
        (True, True),
        (False, False),
        (None, None),
    ]
    retailer_name = models.CharField(max_length=100)
    retailer_id = models.CharField(max_length=150)
    retailer_status = models.BooleanField(default=True)
    bigcommerce_status = models.BooleanField(default=None, null=True, blank=True)
    woocommerce_status = models.BooleanField(default=None, null=True, blank=True)
    shopify_status = models.BooleanField(default=None, null=True, blank=True)
    update_at = models.DateTimeField()

    def __str__(self):
        return self.retailer_name
