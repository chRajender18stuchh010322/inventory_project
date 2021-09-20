from main.models import *
from django.contrib import admin



admin.site.site_header='INVENTORY MANAGEMENT SYSTEM'
admin.site.site_title='INVENTORY MANAGEMENT SYSTEM'
admin.site.welcome_sign= "Welcome to the library",
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    search_fields=['customer_name__icontains']
    list_display=['customer_name','customer_mobile']

admin.site.register(Customer,CustomerAdmin)

class VendorAdmin(admin.ModelAdmin):
    search_fields=['full_name__icontains']
    list_display=['full_name','mobile']
admin.site.register(Vendor,VendorAdmin)


admin.site.register(Unit)


class ProductAdmin(admin.ModelAdmin):
    search_fields=['title__icontains']
    list_display=['title','unit']
admin.site.register(Product,ProductAdmin)


class InventoryAdmin(admin.ModelAdmin):
    search_fields=['product__title','product__unit__title']
    list_display=['id','product','pur_qty','sale_qty','total_bal_qty','product_unit','pur_date','sale_date',]
admin.site.register(Inventory,InventoryAdmin)


class PurchaseAdmin(admin.ModelAdmin):
    search_fields=['product__icontains']
    list_display=['id','product','qty','price','total_amount','vender','pur_date']
admin.site.register(Purchase,PurchaseAdmin)

class SaleAdmin(admin.ModelAdmin):
    search_fields=['product__icontains','qty__icontains']
    list_display=['id','customer','product','qty','price','total_amount','sale_date']
admin.site.register(Sale,SaleAdmin)

