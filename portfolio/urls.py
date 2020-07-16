from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    # path('contact_form',views.contact_form,name='contact_form'),
    path('',views.all_data,name='all_data'),
    path('about/',views.about,name='about'),
    path('portfolio/',views.portfolio,name='portfolio'),
    path('contact',views.contact,name='contact'),
    path('contact_form_submit',views.contact_form_submit,name='contact_form_submit'),
]





