from django.contrib import admin
from .models import ContactForm

#Django Admin View for Contact Form Model
class ContactFormkAdmin(admin.ModelAdmin):
    search_fields = ["pk","full_name"]
    list_filter = ["full_name"]
    list_display = [
        "pk",
        'created_at',
        "full_name",
        "email_id",
        "contact_number",
        "message",
    ]
    list_editable = ["full_name"]
 
#Register ContactForm in Admin view 
admin.site.register(ContactForm,ContactFormkAdmin)

