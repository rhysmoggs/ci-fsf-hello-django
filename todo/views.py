from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    """To do this all we need to say is if request.method='POST':
    we want to set a variable for the name and a variable for done.
    And remember we can get these values using the name attributes from our
    form. So to get the items name we just need to look up request.post.get()
    And the name of that attribute which in our case was 'item_name'
    For the checkbox it's a little bit different. Since it's just a boolean
    value but in order to check if the item is done. All we have to do is check
    whether the post data actually has a done property in it. By checking
    whether done in request.post At this point we should have everything
    we need to actually create a new item. We've already got our item model
    imported from .models up here at the top. And to create an item is
    actually extremely simple. All we need to do is call item.objects.create
    and give it these two variables. So name=name, done=done. And that's it.
    finally we need to return a redirect back to the get_todo_list URL name.
    And in order to do that we're going to need to import redirect from the
    Django shortcuts.
    """
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm()
    context = {
        'form': form

    }
    return render(request, 'todo/add_item.html', context)


def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)


def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    # Change it's done status to the opposite by using not.
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')
