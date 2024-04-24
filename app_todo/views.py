from django.shortcuts import render, redirect
from .models import TodoItem


def todo_list(request):    #Retrieves and renders todo items sorted by creation date."
    todos = TodoItem.objects.order_by('-created_date')  
    return render(request, 'app_todo/todo_list.html', {'todos': todos})


def todo_add(request):   #Added functionality to handle POST requests for creating new todo items with optional description and due date and redirecting to the todo list afterwards.
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST.get('description', '') 
        due_date = request.POST.get('due_date', None)  
        new_todo = TodoItem.objects.create(title=title, description=description, due_date=due_date)
        return redirect('todo_list')  
    return render(request, 'app_todo/todo_add.html')

def todo_delete(request, todo_id):  #Deletes a todo item with the given ID if exists; redirects to todo list otherwise.
    try:
        todo = TodoItem.objects.get(pk=todo_id)
        todo.delete()
        return redirect('todo_list')
    except TodoItem.DoesNotExist:
        return redirect('todo_list')  

def todo_mark_complete(request, todo_id):  #Toggle completion status of a todo item and redirect to todo list if it exists otherwise redirect to todo list.
    try:
        todo = TodoItem.objects.get(pk=todo_id)
        todo.completed = not todo.completed  
        todo.save()
        return redirect('todo_list')
    except TodoItem.DoesNotExist:
        return redirect('todo_list')  
