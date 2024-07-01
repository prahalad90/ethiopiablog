from django.shortcuts import render
from .models import page, travelGuideline, blogCategory, blog

# Create your views here.
def home(request):
    seo = page.objects.get(name = 'Home')
    category = blogCategory.objects.all()
    context = {
        'seo':seo,
        'category':category,
    }
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blogcate(request,slug):
    seo = page.objects.get(name = 'Blog')
    allcat = blogCategory.objects.all()
    category = blogCategory.objects.get(slug = slug)
    posts = blog.objects.filter(category = category )
    context = {
        'seo':seo,
        'category':category,
        'allcat':allcat,
        'posts':posts,
    }
    return render(request, 'blogcat.html',context)

def post(request,catslug,slug):
    post = blog.objects.get(slug=slug)
    allcat = blogCategory.objects.all()
    allpost = blog.objects.filter(category = post.category)
    context = {
        'post': post,
        'allcat': allcat,
        'allpost':allpost,
    }
    return render(request, 'post.html',context)

def travelguide(request):
    try:
        seo = page.objects.get(name__contains = 'Travel')
    except:
        seo = None
    guideline = travelGuideline.objects.all()
    context = {
        'seo':seo,
        'guideline':guideline,
    }
    return render(request, 'travelguide.html',context)

def guidelinepage(request,slug):
    guideline = travelGuideline.objects.get(slug=slug)
    guidelines = travelGuideline.objects.all()
    context = {
        'guideline':guideline,
        'guidelines':guidelines,
    }
    return render(request, 'guideline.html',context)

def error404(request, exception):
    return render(request, 'error.html')