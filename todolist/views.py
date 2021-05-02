from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item
def todoview(request):
    all_items = Item.objects.all()
    return render(request, 'home.html', {'all_item': all_items})

def addtodo(request):
    new_item = Item(added_list  = request.POST["added_list"])
    new_item.save()
    return HttpResponseRedirect('/todoList/')

def deleteTodo(request, todo_id):
    Item_todelete = Item.objects.get(id = todo_id)
    Item_todelete.delete()
    return HttpResponseRedirect('/todoList/')
