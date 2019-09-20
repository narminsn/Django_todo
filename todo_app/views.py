# from django.shortcuts import render, redirect
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from .models import TodoModel
# from django.contrib import messages
# import json
# from .forms import TodoForm


# # Create your views here.


# @csrf_exempt
# def home_page(request):
    
#     # return HttpResponse("<h1>Hello World</h1>")
#     if request.method == 'POST':
#         # table_data = TodoModel.objects.all()[::-1]

#         # # table_data=TodoModel.objects.get(id=6)
       
#         context={
#             "table_data": TodoForm
#         }
       
#         return render(request,"todo_form.html", context)
        
# #     elif request.method=='DELETE':
# #         return HttpResponse("delete")
# #     else:
       
# #         name=request.POST['title']
# #         description=request.POST['description']
# #         a=TodoModel(title=name, description=description)
# #         a.save()
# #         messages.success(request, "Added Successfully")
# #         response = redirect('home')
# #         return response
        

# # def data_page(request):
# #     table_data = TodoModel.objects.all()
# #     # data={
# #     #     "title":table_data.title
# #     # }
# #     data=[]
# #     for obj in table_data:
# #         data.append({
# #             "title": obj.title,
# #             "description": obj.description
# #         })

    
#     # return HttpResponse(data)
#     # return JsonResponse(data, safe=False)


# # def update(request, id):
# #     pass
    

# # def delete(request, id):
# #     pass

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TodoForm
from .models import TodoModel
from django.views.decorators.csrf import csrf_exempt
# from django.db.
# Create your views here.

def home_page(request):
    if "search" in request.GET:
        query=request.GET.get('search')
        TodoModel.objects.filter(

        ) 
        return HttpResponse(query)

    else:
        
        data=TodoModel.objects.all().order_by("-id")
        context={}
        context["data"]=data
    
    # return HttpResponse(a.description)
    return render(request, "todo.html", context)
@csrf_exempt
def create_todo(request):
    if request.method =="POST":
        data = request.POST
        form = TodoForm(data)
        if form.is_valid():  #eger form duzgundurse
            form.save()
            return redirect("home")
        else:  #eger form yanlisdirsa
            context = {}
            context["form"] = TodoForm()
            return render(request, "todo_form.html", context)
    else:
        context = {}
        context["form"] = TodoForm()
        return  render(request, "todo_form.html", context)

@csrf_exempt
def update_view(request,id):
    todo=TodoModel.objects.filter(id=id).last()
    if request.method=="GET":
        
        if todo:
            form=TodoForm(instance=todo)
            context={}
            context['form']=form
            return render(request,"todo_form.html", context)
        else:
            return HttpResponse("bele bir object yoxdur")

    else:
        form=TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("home")

        else:
            context={}
            context['form']=form
            return render(request,'todo_form.html', context)


def delete_view(request,id):
    todo=TodoModel.objects.filter(id=id).last()
    if request.method=="GET":
        context={}
        context['todo']=todo
        return render(request,'delete_todo.html', context)

    else:
        todo.delete()
        return redirect('home')


def show_view(request,id):
    todo=TodoModel.objects.filter(id=id).last()
    
   
    context={}
    context['todo']=todo
    return render(request,"todo_detail.html", context)
        