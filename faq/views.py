
from django.shortcuts import render, redirect

# Create your views here.
from faq.forms import FashionistaForm


def home(request):
    if request.method == 'POST':
        fashionista_form = FashionistaForm(request.POST)
        if fashionista_form.is_valid():
            fashionista_form.save()
            return redirect("home")
    else:
        fashionista_form = FashionistaForm()

    return render(request, "home.html", {'fashionista_form': fashionista_form})