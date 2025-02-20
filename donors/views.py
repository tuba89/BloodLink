from django.shortcuts import render, redirect
from .models import Donor
from .forms import DonorForm
from .utils import send_sms_to_donors, send_email_to_donors
from django.db.models import Q  # Import Q for case-insensitive search
from datetime import date, timedelta
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from .models import Donor, BloodRequest
from django.utils.timezone import now
from collections import Counter

def register_donor(request):
    if request.method == "POST":

        
        form = DonorForm(request.POST)
        if form.is_valid():
            print("✅ Form is valid, saving donor...")
            form.save()
            return redirect("home")
        else:
            print("🚨 Form Errors:", form.errors)  
    
    else:
        form = DonorForm()
    
    return render(request, "donors/register.html", {"form": form})


def search_donors(request):
    donors = None
    if request.method == "POST":
        blood_type = request.POST.get("blood_type")
        wilaya = request.POST.get("wilaya")
        donors = Donor.objects.filter(blood_type=blood_type, wilaya=wilaya)

    return render(request, "donors/search.html", {"donors": donors})


def request_blood(request):
    if request.method == "POST":
        blood_type = request.POST.get("blood_type")
        wilaya = request.POST.get("wilaya")

        # Save the blood request
        BloodRequest.objects.create(blood_type=blood_type, wilaya=wilaya)

        # Find eligible donors
        today = date.today()
        men_eligibility_date = today - timedelta(days=90)
        women_eligibility_date = today - timedelta(days=180)

        donors = Donor.objects.filter(
            Q(blood_type__iexact=blood_type) & 
            Q(wilaya__iexact=wilaya) &
            (
                (Q(gender="Male") & Q(last_donation__lte=men_eligibility_date)) |  
                (Q(gender="Female") & Q(last_donation__lte=women_eligibility_date))
            )
        )

        return render(request, "donors/blood_request_success.html", {"donors": donors})

    return render(request, "donors/request_blood.html")


def thank_you(request):
    return render(request, "donors/thank_you.html")

def home(request):
    # Get the most recent blood requests (last 5)
    recent_requests = BloodRequest.objects.order_by('-created_at')[:5]

    # Fetch all donors to get real-time updates
    donors = Donor.objects.all()

    # Count the number of available donors per blood type
    blood_availability_dict = dict(Counter(donor.blood_type for donor in donors))

    context = {
        "requests": recent_requests,
        "blood_availability": blood_availability_dict  # Ensure this updates dynamically
    }
    return render(request, "donors/home.html", context)


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = UserCreationForm()
    
    return render(request, "donors/signup.html", {"form": form})


def about(request):
    return render(request, "donors/about.html")

def logout_view(request):
    # logout(request)
    # return redirect("home")
    pass

def logout_view(request):
    # logout(request)
    # return redirect("home")  # Redirect to home page after logout
    pass