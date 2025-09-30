from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,Http404
from django.urls import reverse
from .models import post
from django.core.paginator import Paginator
from .forms import FeedbackForm

# posts=[
#     {'id':1,'Author':'Venkat','title':'Post 1','content':"Hello this post 1"},
#     {'id':2,'Author':'Nadhiya','title':'Post 2','content':"Hello this post 2"},
#     {'id':3,'Author':'Gopi','title':'Post 3','content':"Hello this post 3"},
#     {'id':4,'Author':'Amudha','title':'Post 4','content':"Hello this post 4"},
#     {'id':5,'Author':'Malai','title':'Post 5','content':"Hello this post 5"},
#     {'id':6,'Author':'Kural','title':'Post 6','content':"Hello this post 6"}
# ]
posts=post.objects.all()


def index(request):
    return HttpResponse("Hello Venkat, you are doing great.")


def login(request):
    # return redirect(reverse("blogapp:register_page"))
    return render(request,"login.html")

def register(request):
    return render(request,"register.html")

def main(request):
    all_posts=post.objects.all()

    paginator=Paginator(all_posts,6)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    return render(request,"main.html",{'page_obj':page_obj})

def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        
    
        return render(request, 'contact.html', {'form': form})
    
    return render(request, 'contact.html')



def pageDetail(request,slug):
    try:
        post_obj = post.objects.get(slug=slug)
        related_posts=post.objects.filter(category=post_obj.category).exclude(pk=post_obj.post_id)
        
    except Http404 as e:
        raise Http404("Post Not Found")
    
    return render(request, 'pageDetail.html', {"posts": post_obj,"related_posts": related_posts})