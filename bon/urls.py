from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

from op import views
from bon import settings

urlpatterns = [
    path('', views.index, name='home'),
    path('check/', views.check, name='check'),
    path('checked/', views.checked, name='checked'),
    path('accounts/', include('allauth.urls')),
    #path('accounts/profile/', views.profile, name='profile'),

    path('logout/', views.logout_func, name='logout'),
    path('admin/', admin.site.urls),
    path('email/', views.email, name='email'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
