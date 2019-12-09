from django.db import models

# Create your models here.

class EcommIntegration(models.Model):
    STATUS_CHOICES = [
        (True, 'Healthy Connection'),
        (False, 'Unhealthy Connection'),
        (None, 'No Connection'),
    ]
    retailer_name = models.CharField(max_length=100)
    retailer_id = models.CharField(max_length=150)
    retailer_status = models.BooleanField(default=True)
    bigcommerce_status = models.BooleanField(default=None, null=True, blank=True, choices=STATUS_CHOICES)
    woocommerce_status = models.BooleanField(default=None, null=True, blank=True, choices=STATUS_CHOICES)
    shopify_status = models.BooleanField(default=None, null=True, blank=True, choices=STATUS_CHOICES)
    update_at = models.DateTimeField()

    def __str__(self):
        return self.retailer_name
