from django.urls import path
from . import views

#URLconfig
urlpatterns = [
    #path("january", views.january),
    #if a request reaches january, then access the index function
    #path("february", views.february),
    
    path("<month>", views.monthly_challenge)
    #this way i handle all urls with any text after challenges/ will be handled ny views. class

]