"""skimread URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from skimread import views
from django.conf.urls.static import static
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings
from django.contrib.sitemaps import GenericSitemap # new
from django.contrib.sitemaps.views import sitemap # new
from blog.models import BlogPost

info_dict = {
    'queryset': BlogPost.objects.all(),
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('portfolio/abhishek',views.portfoliok,name="portfoliok"),
    path('summernote/', include('django_summernote.urls')),
    path("contact/",views.contact, name='contact'),
    path("about-us/",views.aboutus,name="about-us"),
    path("inquiry/",views.inquiry,name="inquiry"),
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),
    path('sitemap.xml', sitemap, 
        {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
        name='django.contrib.sitemaps.views.sitemap'),
    path("<str:title>",views.view_blog, name='view_blog'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
