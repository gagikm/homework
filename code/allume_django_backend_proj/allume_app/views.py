from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .forms import SignupForm, FAQForm, TestimonialForm
from .models import Testimonial, FrequentlyAskedQuestion

# Create your views here.
def signup(request):
    if request.user.is_authenticated():
        return redirect('/faq/add/')

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password1'])
            login(request, user)
            return HttpResponseRedirect("/faq/add/")
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})

def add_to_faq(request):
    if not request.user.is_authenticated():
        return redirect('/login/')

    if request.method == "POST":
        form = FAQForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FAQForm()
    return render(request, 'addfaq.html', {'form': form})

def add_testimonial(request):
    if not request.user.is_authenticated():
        return redirect('/login/')

    if request.method == "POST":
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TestimonialForm()
    return render(request, 'addtestimonial.html', {'form': form})

def testimonials(request):
    all_testimonials = Testimonial.objects.all();
    context = {'all_testimonials': all_testimonials}
    return render(request, 'testimonials.html', context)

def faq(request):
    all_faq = FrequentlyAskedQuestion.objects.all();
    context = {'all_faq': all_faq}
    return render(request, 'faq.html', context)