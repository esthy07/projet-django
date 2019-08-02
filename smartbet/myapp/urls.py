from django .urls import path
from django.contrib import admin

from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('connexion', views.connexion, name="connexion"),
    path('mylogin/', views.mylogin, name="mylog"),
    path('mylogout/', views.mylogout, name="mylogout"),
    path('scrap', views.scrap),
    path('pari', views.pari, name="pari"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)