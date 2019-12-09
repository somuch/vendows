from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from django.utils.safestring import mark_safe

# Register your models here.
from .models import EcommIntegration

class AnyIntegrationFilter(admin.SimpleListFilter):
    pass

def disconnect_bigcommerce(modeladmin, request, queryset):
    queryset.update(bigcommerce_status=None)

disconnect_bigcommerce.short_description = 'Disconnect [ BigCommerce ] Connections'

def disconnect_woocommerce(modeladmin, request, queryset):
    queryset.update(woocommerce_status=None)

disconnect_woocommerce.short_description = 'Disconnect [ WooCommerce ] Connections'

def disconnect_shopify(modeladmin, request, queryset):
    queryset.update(shopify_status=None)

disconnect_shopify.short_description = 'Disconnect [ Shopify ] Connections'

def connect_bigcommerce(modeladmin, request, queryset):
    queryset.update(bigcommerce_status=True)

connect_bigcommerce.short_description = 'Connect [ BigCommerce ] Connections'

def connect_woocommerce(modeladmin, request, queryset):
    queryset.update(woocommerce_status=True)

connect_woocommerce.short_description = 'Connect [ WooCommerce ] Connections'

def connect_shopify(modeladmin, request, queryset):
    queryset.update(shopify_status=True)

connect_shopify.short_description = 'Connect [ Shopify ] Connections'

def send_to_slack(modeladmin, request, queryset):
    pass
send_to_slack.short_description = 'Send to Slack #ecommerce'

def send_to_email(modeladmin, request, queryset):
    pass
send_to_email.short_description = 'Send to Email ecommerce@vendhq.com'

admin.site.disable_action('delete_selected')

@admin.register(EcommIntegration)
class EcommIntegrationAdmin(admin.ModelAdmin):

    fields = ('retailer_name', 'retailer_id', 'retailer_status', 'bigcommerce_status', 'woocommerce_status', 'shopify_status', 'update_at')
    readonly_fields = fields
    list_display = ('retailer_name', 'retailer_id', 'retailer_active', 'bigcommerce', 'woocommerce', 'shopify')
    list_filter = ('retailer_status', 'bigcommerce_status', 'woocommerce_status', 'shopify_status')
    search_fields = ('retailer_name', 'retailer_id')
    list_per_page = 50
    actions = [
        disconnect_bigcommerce,
        disconnect_woocommerce,
        disconnect_shopify,
        connect_bigcommerce,
        connect_woocommerce,
        connect_shopify,
        send_to_slack,
        send_to_email
        ]
    def retailer_active(self, obj):
        return obj.retailer_status
    retailer_active.short_description = 'Active Retailer?'
    retailer_active.boolean = True
    retailer_active.admin_order_field = '-retailer_status'

    def bigcommerce(self, obj):
        return obj.bigcommerce_status
    bigcommerce.short_description = 'BigCommerce'
    bigcommerce.boolean = True
    bigcommerce.admin_order_field = '-bigcommerce_status'

    def woocommerce(self, obj):
        return obj.woocommerce_status
    woocommerce.short_description = 'WooCommerce'
    woocommerce.boolean = True
    woocommerce.admin_order_field = '-woocommerce_status'

    def shopify(self, obj):
        return obj.shopify_status
    shopify.short_description = 'Shopify'
    shopify.boolean = True
    shopify.admin_order_field = '-shopify_status'



