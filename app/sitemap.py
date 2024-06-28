from django.contrib import sitemaps
from django.urls import reverse
from .models import blog, blogCategory, travelGuideline


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"
    protocol = 'http'

    def items(self):
        return ["home", "about", "contact","travelguide",]

    def location(self, item):
        return reverse(item)

class BlogSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority=0.5
    protocol = 'http'
    
    def items(self):
        return blog.objects.all()
        
    def lastmod(self,obj):
        return obj.date
    
    def location(self, obj):
        return f"/{obj.category.slug}/{obj.slug}/"

class guidelineSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority=0.5
    protocol = 'http'
    
    def items(self):
        return travelGuideline.objects.all()
    
    def location(self, obj):
        return f"/{obj.slug}/"