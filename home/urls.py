from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [

    #Homepage redirects to login and sign up page
    path('homepage/', views.homepage, name='homepage'),

    #Login user into account on form fill
    path('login/', auth_views.LoginView.as_view(template_name='pages/index.html'), name='login'),

    #logs out user when requested on click
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    #registers user on account creation
    #check views for authentication and form contribution
    path('register/', views.register, name='register'),

    #redirects to user to dashboard after login or signup
    #check views for authentication and form contribution
    path('dashboard/', views.dashboard, name='dashboard'),

    #redirects to the subscription page if not subscribed
    path('subscription/', views.subscription, name='subscription'),

    #redirects to the vote renew page and lets you purchase more votes
    path('renew/', views.renew, name='renew'), 

    #Checks for user subscription and confirms if your subscribed or not, it als ends the subscription
    path('endsub/', views.endsub, name='endsub'),

    #add votes to the voted button when the user adds clicks vote
    path('vote/int:vote_id/', views.vote, name='vote'),

    #Create vote for every user who clicks the votes
    path('createvote/str:vote_id/', views.createvote, name='createvote'),

    #create a path for the categories in the homepage
    path('<slug:slug>/', views.category_details, name="category_details"),
] 