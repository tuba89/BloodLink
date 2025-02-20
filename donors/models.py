from django.db import models

class Donor(models.Model):
    GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
    BLOOD_TYPES = [('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')]

    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPES)
    wilaya = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    last_donation = models.DateField()

    def is_eligible(self):
        from datetime import date, timedelta
        today = date.today()
        if self.gender == "Male":
            return today - self.last_donation >= timedelta(days=90)
        else:
            return today - self.last_donation >= timedelta(days=180)

    def __str__(self):
        return f"{self.name} ({self.blood_type}) - {self.wilaya}"


# ADD THE BLOOD REQUEST MODEL BELOW
class BloodRequest(models.Model):
    blood_type = models.CharField(max_length=3)
    wilaya = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp

    def __str__(self):
        return f"{self.blood_type} needed in {self.wilaya} on {self.created_at}"
