from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth.models import User


from .models import Candidate, Userprofiles, Subscription, Payment, PaymentHistory, UserSubscriptions, Categories
from .vote import Vote

#Show homepage
def homepage(request):
    return render (request, 'pages/homepage.html')

def category_details(request, slug):
    categories = get_object_or_404(Categories, slug=slug)
    candidates = categories.candidate.all()

    return render(request, 'pages/categories.html', {
        'categories' : categories,
        'candidates' : candidates
    })

#Show dashboard
def dashboard(request):

    subscription = Subscription.objects.all() [0:1]
    candidate = Candidate.objects.all() [0:1]
    categories = Categories.objects.all() [0:1]
    vote = Vote(request)

    return render (request, 'pages/voters-dashboard.html', {
        'subscription' : subscription,
        'candidate' : candidate,
        'categories' : categories,
        'vote': vote,
    })

#Show the candidates or voting components
def voters(request, modal_slug):
    candidate = Candidate.objects.all() [0:1]

    return render (request, '', {
        'candidate' : candidate,
    })

#Pay for subscription, upon subscription
def subscription(request):
    plan = request.GET.get('sub_plan')
    fetch_subscription = Subscription.objects.filter(subscription_type=plan).exists()
    if fetch_subscription == False:
        return redirect('subscription')
    subscription = Subscription.objects.get(subscription_type=plan)
    print(subscription)
    return render (request, 'pages/subscription.html')

#Renew subscription, for the votes
def renew(request):
    return render (request, 'pages/add-votes.html')

#checks for user subscription
def endsub(request):
    return render (request, 'pages/end-sub')


#Create user account on sign up
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)


        #checks for user forms and validates if user is using form to log in
        if form.is_valid():
            form.save()
            user = form.save()
            #obj = user.save()
            #login(request, user)

            userprofile = Userprofiles.objects.create(user=user)

            #connect the subscription to the user registration form
            get_subscription = Subscription.objects.get(subscription_type='Free')
            UserSubscriptions.objects.create(user=user, subscription=get_subscription)
            messages.success(request, "Registration successful." )

            #takes user to subscription page if successfully registered
            return redirect('dashboard')
        
    else:
        form = UserCreationForm()

    #returns user back to regiester if not or failed to register into account
    return render (request, 'pages/register.html', {
        'form': form,
    }) 

def createvote(request, vote_id):
    action = request.GET.get('action', '')

    if action:
        vote = 1

        vote_action = Vote(request)
        vote_action.add(vote_id, vote, True)

        return redirect('dashboard')

def vote(request, vote_id):
    vote_action = Vote(request)
    vote_action.add(vote_id)

    return redirect('dashboard')