# admin.py

from django.contrib import admin
from .models import Customer, Brand, Model, Item, Complaint, Engineer
from django.db.models import Sum

class HiddenModelAdmin(admin.ModelAdmin):
    def has_module_permission(self, request):
        return False

    def get_model_perms(self, request, obj=None):
        return {}
    
class ComplaintInline(admin.TabularInline):  # You can also use admin.StackedInline for a different layout
    model = Complaint
    extra = 0

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email_id', 'address', 'total_billed_amount')
    search_fields = ('name', 'phone_number', 'email_id', 'address')
    inlines = [ComplaintInline]
    def total_billed_amount(self, obj):
        total_amount = obj.complaint_set.aggregate(Sum('bill_amount'))['bill_amount__sum']
        return total_amount if total_amount is not None else 0

    total_billed_amount.short_description = 'Total Billed Amount'

class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name',)
    search_fields = ('brand_name',)

class ModelAdmin(admin.ModelAdmin):
    list_display = ('model_name',)
    search_fields = ('model_name',)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_name',)  # Use custom methods
    list_filter = ('item_name',)
    search_fields = ('item_name',)

    def get_brand_name(self, obj):
        return obj.brand.brand_name if obj.brand else None

    def get_model_name(self, obj):
        return obj.model.model_name if obj.model else None

    get_brand_name.admin_order_field = 'brand__brand_name'  # Allow sorting by brand name
    get_model_name.admin_order_field = 'model__model_name'  # Allow sorting by model name

class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_phone_number', 'customer_bill_amount')
    
    def customer_name(self, obj):
        return obj.customer.name if obj.customer else None
    
    def customer_phone_number(self, obj):
        return obj.customer.phone_number if obj.customer else None
    
    def customer_bill_amount(self, obj):
        return obj.bill_amount if obj.complaint else None  # Use obj.bill_amount directly
    
    customer_name.short_description = 'Customer Name'
    customer_phone_number.short_description = 'Customer Phone Number'
    customer_bill_amount.short_description = 'Amount Billed'


class EngineerAdmin(admin.ModelAdmin):
    inlines = [ComplaintInline]




# Register the models in the desired order
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Engineer, EngineerAdmin)
#hidden models
admin.site.register(Item, HiddenModelAdmin)
admin.site.register(Model, HiddenModelAdmin)
admin.site.register(Brand, HiddenModelAdmin)