from twilio.rest import Client
from django.core.mail import send_mail
from .models import Donor  # Import the Donor model

# Twilio credentials (replace with real ones)
ACCOUNT_SID = "your_account_sid"
AUTH_TOKEN = "your_auth_token"
TWILIO_PHONE = "+123456789"  # Your Twilio number

def send_sms_to_donors(blood_type, wilaya, message):
    """Find eligible donors and send SMS notifications"""
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    
    # Find donors with the requested blood type and wilaya
    donors = Donor.objects.filter(blood_type=blood_type, wilaya=wilaya)
    
    for donor in donors:
        client.messages.create(
            body=message,
            from_=TWILIO_PHONE,
            to=donor.phone
        )
    
    print(f"✅ SMS sent to {donors.count()} donors in {wilaya}")

def send_email_to_donors(blood_type, wilaya, subject, message):
    """Find eligible donors and send email notifications"""
    donors = Donor.objects.filter(blood_type=blood_type, wilaya=wilaya)
    
    recipient_emails = [donor.email for donor in donors]  # Collect emails
    
    send_mail(
        subject,
        message,
        "your_email@example.com",  # Your email
        recipient_emails,
        fail_silently=False,
    )

    print(f"✅ Email sent to {len(recipient_emails)} donors in {wilaya}")
