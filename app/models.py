from django.db import models

index = [
    ("index","index"),
    ("noindex","noindex")]
    
follow = [
    ("follow","follow"),
    ("nofollow","nofollow")]    

choice = [
        ('1',"Draft"),
        ('2',"Published"),
    ]
# Create your models here.    
class page(models.Model):
    name = models.CharField(max_length=20)
    page_title = models.CharField(max_length=200)
    meta = models.CharField(max_length=300)
    slug = models.CharField(max_length=100)
    index = models.CharField(max_length=8, choices=index, default="index")
    follow = models.CharField(max_length=8, choices=follow, default="follow")
    bannerImage = models.ImageField(upload_to='./', blank=True)
    bannerImageAlt = models.CharField(max_length = 150,blank=True)
    bannerHeading = models.CharField(max_length=100, blank=True)
    aboutSection = models.CharField(max_length = 100, verbose_name="About Field",blank=True)
    aboutbgImage = models.ImageField(upload_to='./', verbose_name="Background Image",blank=True)
    aboutContent = models.CharField(max_length = 2000,blank=True)
        
    def __str__(self):
        return self.name

class enquiry(models.Model):
    date = models.DateTimeField(auto_now=True)
    name  = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    mobile = models.CharField(max_length=20)
    message = models.CharField(max_length = 1000)
    
    def __str__(self):
        return self.email

class blogCategory(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length=1000,blank=True)
    image = models.ImageField(upload_to='./blog')
    altTag = models.CharField(max_length=100, blank=True)
    slug = models.CharField(max_length=50)
    page_title = models.CharField(max_length=100, blank=True)
    meta = models.CharField(max_length=200, blank=True)
    index = models.CharField(max_length=8, choices=index, default="index")
    follow = models.CharField(max_length=8, choices=follow, default="follow")
    
    def __str__(self):
        return self.name

class author(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    image = models.ImageField(upload_to='./author') 
    altTag = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.name
    
class blog(models.Model):
    category = models.ForeignKey(blogCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length = 1000)
    bannerImage = models.ImageField(upload_to='./blog')
    altTag = models.CharField(max_length=100, blank=True)
    date = models.DateField(auto_now=False)
    content = models.TextField()
    author = models.ForeignKey(author, on_delete=models.CASCADE)
    slug = models.SlugField(max_length = 50)
    page_title = models.CharField(max_length=200)
    meta = models.CharField(max_length=400)
    status = models.CharField(max_length=2, choices=choice, default=1)
    index = models.CharField(max_length=8, choices=index, default="index")
    follow = models.CharField(max_length=8, choices=follow, default="follow")
    featured = models.CharField(max_length=10, blank=True)
    image1 = models.ImageField(upload_to='./blog',blank=True)
    image2 = models.ImageField(upload_to='./blog',blank=True)
    image3 = models.ImageField(upload_to='./blog',blank=True)
    image4 = models.ImageField(upload_to='./blog',blank=True)
    image5 = models.ImageField(upload_to='./blog',blank=True)
    def __str__(self):
        return self.title
    
    def post(cat):
        catname = blogCategory.objects.get(slug = cat)
        posts = blog.objects.filter(category = catname)
        return posts
    
class travelGuideline(models.Model):
    name = models.CharField(max_length = 50)
    heading = models.CharField(max_length=100)
    content = models.TextField()
    icon = models.ImageField(upload_to='./guideline')
    altTag = models.CharField(max_length=100, blank=True)
    bannerImage = models.ImageField (upload_to='./guideline')
    banneraltTag = models.CharField(max_length=100, blank=True)
    slug = models.CharField(max_length=20)
    page_title = models.CharField(max_length=100, blank=True)
    meta = models.CharField(max_length=200, blank=True)
    index = models.CharField(max_length=8, choices=index, default="index")
    follow = models.CharField(max_length=8, choices=follow, default="follow")
    
    def __str__(self):
        return self.name
    
class subscriber(models.Model):
    email = models.EmailField()
    
    def __str__(self):
        return self.email

class counter(models.Model):
    name = models.CharField(max_length = 150)
    count = models.IntegerField()
    icon = models.ImageField(upload_to='./counter/')
    iconAlt =  models.CharField(max_length = 50)

    def __str__(self):
        return self.name

class aboutGallery(models.Model):
    name = models.CharField(max_length = 50)
    image1 = models.ImageField(upload_to='./Gallery/')
    
    def __str__(self):
        return self.name
