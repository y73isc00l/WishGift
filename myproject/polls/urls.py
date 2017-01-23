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
from django.contrib.sitemaps.views import sitemap
import login
import views
import dashboard
import pool
urlpatterns =[
#url leads to the home page of the site
        url(r'^$',views.home),
	#url not yet implemented
        url(r'^index/$',views.index),
	#a feature to be discovered by the users
        url(r'^time/plus/(\d{1,2})/$',views.timeafter),
	#urls leads to  login page
	url(r'^login/$',login.login),
	#url leads to signup page
	url(r'^signup/$',login.signup),
	#displays metadata of the site
  #url leads to contact page
	url(r'^contactus/$',views.contactus),
	url(r'^display_meta/$',views.display_meta),
	###start Dashboard
	#leads to the dashboard
	url(r'^welcome/user/$',dashboard.Dashboard01),
	#dashboard url that displays search results
	url(r'search/',dashboard.Dashboard01search),
	#dashboard url that adds wishes and login is required for this feature
	url(r'^user/addwish/$',dashboard.Dashboard01addwish),
	#url to delete wishes
	url(r'user/deletewish/(\w+)/$',dashboard.Dashboard01delwish),
	#url to edit wishes
	url(r'user/editwish/(\w+)/$',dashboard.Dashboard01editwish),
	#url to grant wish to a person while viewing profile,login is required,without login the user will stay on the page with a error message
	url(r'^user/grantwish/(\w+)/(\w+)/$',dashboard.Dashboard01grantwish),
	#url to add friend'
	url(r'^user/addfriend/(\w+)/$',dashboard.Dashboard01addfriend),
	###end Dashboard
	###start poolgift
	##poolgifting welcome page
	url(r'^/poolgift/welcome/$',pool.welcome),		
	###end poolgift
	#dashboard feature that allows users to logout and login is required and redirects to login page
	url(r'^user/logout/$',dashboard.logout_view),
	#url that allows users to view the profile of other users
	url(r'^view/(\w+)/$',dashboard.person_viewprofile),
  #django url that opens the admin dite
  url(r'^admin/', admin.site.urls),
	#url to submit the sitemap xml file that is auto generated
  url(r'^sitemap\.xml$', sitemap),
	#url for webcrawler instruction
        url(r'^robots\.txt$', include('robots.urls')),
]

