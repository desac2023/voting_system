from django.contrib import admin
from .models import Categories, Candidate, Userprofiles, Subscription, Payment, PaymentHistory, UserSubscriptions, Subscribers

admin.site.register(Categories)
admin.site.register(Candidate)
admin.site.register(Userprofiles)
admin.site.register(Subscription)
admin.site.register(Payment)
admin.site.register(PaymentHistory)
admin.site.register(UserSubscriptions)
admin.site.register(Subscribers)



# Register your models here.
