"""fhx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from blog import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^admin/', admin.site.urls,name="admin"),
    url(r'^$',views.home,name="home"),
    url(r'^about/',views.about),
    url(r'^signup/',views.signup),
    url(r'^logout/',views.logout_view),
    url(r'^user/',views.information,name='dengji'),
	url(r'^login/$',views.login),
    #聪爸爸写的
    url(r'^post/$',views.post),
	
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

