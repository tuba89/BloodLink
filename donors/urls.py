from django.urls import path
from .views import request_blood, register_donor, thank_you, home, about
from .views import about, signup, logout_view
urlpatterns = [
    path("", home, name="home"),
    path("request-blood/", request_blood, name="request_blood"),
    path("register/", register_donor, name="register_donor"),
    path("thank-you/", thank_you, name="thank_you"), 
    path("about/", about, name="about"),  # Add About Us page
    # path("signup/", signup, name="signup"),  # Add Signup page
    # path("logout/", logout_view, name="logout"),

]
