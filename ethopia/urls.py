"""
URL configuration for ethopia project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include, re_path
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from app.sitemap import StaticViewSitemap, BlogSitemap, guidelineSitemap
from django.views.static import serve


sitemaps = {
    "static": StaticViewSitemap,
    'blog':BlogSitemap,
    'guideline':guidelineSitemap,
}


urlpatterns = [    
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
    path(
        "sitemap.xml/",sitemap,{"sitemaps": sitemaps},name="django.contrib.sitemaps.views.sitemap",),

]
handler404 = 'app.views.error404'