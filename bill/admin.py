from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(productDetail)

@admin.register(Detail)
class DetailAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'address', 'email_address', 'phone', 'invoice_number', 'joined_date')
    # readonly_fields make fields in django admin panel editable false or disable
    readonly_fields = ['invoice_number']
    search_fields=['name']