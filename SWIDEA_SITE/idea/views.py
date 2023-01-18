from django.shortcuts import render, redirect
from .models import Idea

# Create your views here.
def home(request):
    idea = Idea.objects.all()
    context = {
        "idea" : idea
    }
    
    return render(request, template_name="idea/home.html", context=context)


    
    
def create(request):
    dev = request.GET.get('devtool')
    if request.method == 'POST':
        title = request.POST["title"]
        image = request.FILES["image"]
        content = request.POST["content"]
        interest = request.POST["interest"]
        devtool = request.POST["devtool"]
        
        Idea.objects.create(title=title, image=image, content=content, interest=interest, devtool=devtool)
        return redirect("/")
    
    context = {}
    return render(request, template_name="idea/create.html", context=context)

def detail(request, id):
    idea = Idea.objects.get(id=id)
    context = {
        "idea" : idea
    }
    return render(request, template_name="idea/detail.html", context=context)

def update(request, id):
    if request.method == 'POST':
        title = request.POST["title"]
        image = request.FILES["image"]
        content = request.POST["content"]
        interest = request.POST["interest"]
        devtool = request.POST["devtool"]
        
        Idea.objects.filter(id=id).update(title=title, image=image, content=content, interest=interest, devtool=devtool)
        return redirect(f"/idea/{id}")
    
    idea = Idea.objects.get(id=id)
    context = {
        "idea":idea
    }
    
    return render(request, template_name="idea/update.html", context=context)


def delete(request, id):
    Idea.objects.filter(id=id).delete()
    return redirect("/")