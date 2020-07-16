from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import ContactForm

def portfolio(request):
    return render(request,'portfolio/portfolio.html')

def about(request):
    return render(request,'portfolio/about.html')

def contact(request):
    return render(request,'portfolio/contact.html')

def contact_form_submit(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        email_id = request.POST['email_id']
        contact_number = request.POST['contact_number']
        message = request.POST['message']
        ContactForm.objects.create(full_name=full_name,
                                   email_id=email_id,
                                   contact_number=contact_number,
                                   message=message
                                   )
    return HttpResponseRedirect(reverse('portfolio:contact'))

def all_data(request):
    contact_data = ContactForm.objects.all()
    data = {'contact_data':contact_data}
    return render(request,'portfolio/all_data.html',data)
