from todo.forms import todo_form
from django.shortcuts import redirect, render

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from .models import Todo
def home(request):
    if request.method=='POST':
        todo=Todo()
        todo.title=request.POST.get('title')
        todo.desc=request.POST.get('desc')
        todo.save()
        allTodo  = Todo.objects.all()   
        context = {
            'allTodo': allTodo
        }
        return render(request,'views.html',context)
    else:
        return render(request,'index.html')
def view(request):
    allTodo  = Todo.objects.all()
    context = {
        'allTodo': allTodo,
    }
    return render(request,'views.html',context)

def delete_todo(request,sno):
    todo = Todo.objects.filter(sno=sno)
    todo.delete()
    return redirect('view')



def edit_todo(request, sno):
    task = get_object_or_404(Todo, pk = sno)
    if request.method == 'POST':
        form = todo_form(request.POST, instance = task)
        if form.is_valid():
            task = form.save(commit = False)
            task.save()
            return redirect('view')
    else:
        form = todo_form(instance = task)

    return render(request, template_name = 'update.html', context = { 'form': form })

    
