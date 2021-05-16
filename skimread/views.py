from django.shortcuts import render
from blog.models import BlogPost, Inquiry
from datetime import datetime
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.

def home(request):
    blogs = BlogPost.objects.all()
    return render(request,'home.html',{'blogs':blogs});

def portfoliok(request):
    return render(request,'portfoliok.html');

def view_blog(request, title):
    blog_title = title.replace('-',' ')
    blog = BlogPost.objects.filter(title__iexact = blog_title).first()
    FeaturedBlogs = BlogPost.objects.filter(featured=True)
    return render(request, 'view_blog.html',{'blog': blog,'featureds':FeaturedBlogs});

def contact(request):
    return render(request,'contact.html')

def aboutus(request):
    return render(request,'aboutus.html')

def inquiry(request):
    iname = request.POST.get('inquiry-name')
    iemail = request.POST.get('inquiry-email')
    icontact = request.POST.get('inquiry-contact')
    imessage = request.POST.get('inquiry-message')
    idate = datetime.now()
    inquiry = Inquiry(name=iname, email=iemail, contact=icontact, message=imessage, date_created=idate)
    inquiry.save()
    messages.success(request, 'Thankyou for contacting us. Your message has been received. ')
    return redirect('contact')