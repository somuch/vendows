from django.contrib import admin

# Register your models here.
from .models import EcommIntegration

@admin.register(EcommIntegration)
class EcommIntegrationAdmin(admin.ModelAdmin):

    fields = ('retailer_name', 'retailer_id', 'retailer_status', 'bigcommerce_status', 'woocommerce_status', 'shopify_status', 'update_at')
    list_display = ('retailer_name', 'retailer_id', 'retailer_active', 'bigcommerce', 'woocommerce', 'shopify')
    list_filter = ('retailer_status', 'bigcommerce_status', 'woocommerce_status', 'shopify_status')

    def retailer_active(self, obj):
        return obj.retailer_status
    retailer_active.short_description = 'Active?'
    retailer_active.boolean = True

    def bigcommerce(self, obj):
        return obj.bigcommerce_status
    bigcommerce.short_description = 'BigCommerce'
    bigcommerce.boolean = True

    def woocommerce(self, obj):
        return obj.woocommerce_status
    woocommerce.short_description = 'WooCommerce'
    woocommerce.boolean = True

    def shopify(self, obj):
        return obj.shopify_status
    shopify.short_description = 'Shopify'
    shopify.boolean = True



