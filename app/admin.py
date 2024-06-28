from django.contrib import admin

# Register your models here.
from app.models import page, enquiry, blog, blogCategory, author, subscriber, travelGuideline, counter, aboutGallery

# Register your models here.
@admin.register(page)
class pageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
@admin.register(blog)
class blogAdmin(admin.ModelAdmin):
    list_display = ('title','date')
    
@admin.register(enquiry)
class enquityAdmin(admin.ModelAdmin):
    list_display = ('name','date')
    
@admin.register(blogCategory)
class blogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
@admin.register(author)
class authorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    
@admin.register(subscriber)
class subscriberAdmin(admin.ModelAdmin):
    list_display = ('email',)
    
@admin.register(travelGuideline)
class travelAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(counter)
class counterAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(aboutGallery)
class galleryAdmin(admin.ModelAdmin):
    list_display = ('name',)