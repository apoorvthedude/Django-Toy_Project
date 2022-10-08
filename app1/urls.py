from django.urls import path
from .views import HomePage,contact,AboutPage

urlpatterns = [
    path('',HomePage,name = 'home'),
    path('about/',AboutPage,name = 'about'),
    path("contact-us/",contact,name = 'contact'),
]
