from django.contrib import admin
from .models import Donor, BloodRequest

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ("name", "blood_type", "wilaya", "phone", "last_donation", "is_eligible") 
    list_filter = ("blood_type", "wilaya") 
    search_fields = ("name", "phone")

    def is_eligible(self, obj):
        """Check if the donor is eligible based on last donation date."""
        return obj.is_eligible()
    
    is_eligible.boolean = True  # Shows True/False as icons in Django Admin


# Add BloodRequest to Django Admin
@admin.register(BloodRequest)
class BloodRequestAdmin(admin.ModelAdmin):
    list_display = ("blood_type", "wilaya", "created_at")  # Show fields in Admin
    list_filter = ("blood_type", "wilaya")  # Add filters
    search_fields = ("wilaya",)  # Allow searching by wilaya
    ordering = ("-created_at",)  # Show latest requests first
