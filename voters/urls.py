from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from home.views import homepage
#from . import views
urlpatterns = [
    path('', homepage, name='homepage'),
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
