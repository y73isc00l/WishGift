"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import include,url
from django.contrib import admin
import views
import login
from django.contrib.sitemaps.views import sitemap
import dashboard
urlpatterns =[
##      url(r'^home/$',home),
        url(r'^$',views.home),
        url(r'^index/$',views.index),
        url(r'^time/plus/(\d{1,2})/$',views.timeafter),
	url(r'^welcome/user/$',dashboard.Dashboard01),
	url(r'^contactus/$',views.contactus),
	url(r'^display_meta/$',views.display_meta),
	url(r'^login/$',login.login),
	url(r'^signup/$',login.signup),
	url(r'^user/addwish/$',dashboard.Dashboard01addwish),
	url(r'^user/logout/$',dashboard.logout_view),
##      url(r'^polls/',include('polls.url')),##not working 
        url(r'^admin/', admin.site.urls),
        url(r'^sitemap\.xml$', sitemap),
        url(r'^robots\.txt$', include('robots.urls')),
]
