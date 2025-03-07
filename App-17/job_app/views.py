from django.shortcuts import render
from .forms import ApplicationForm
from .models import Form
from django.contrib import messages

def index(request):
    if request.method == "POST":
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["fname"]
            last_name = form.cleaned_data["lname"]
            email = form.cleaned_data["email"]
            date = form.cleaned_data["date"]
            occupation = form.cleaned_data["selections"]

            Form.objects.create(first_name=first_name, last_name=last_name, email=email, date=date, occupation=occupation)
            messages.success(request, "Application successfully created")
    return render(request, 'index.html')
