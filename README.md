


Table of Contents

Testing
    - Manual/Auto? by created test files and functions e.g. test_forms.py for forms, test_views.py for views etc
    - Coverage - tool to check % tested. install it:
        - check: Full Stack Frameworks With Django > Hello Django > Testing > Coverage







taken from django first tutorial CI "Hello Django  Getting Set Up  Getting Set Up"


use CI template https://github.com/Code-Institute-Org/gitpod-full-template

type ```pip3 install django==3.2``` (for the tutorial)....OR ```pip3 install django``` (for latest version of django)


So now that we've got Django installed. We're ready to create our first django project.
Django comes with the built-in admin command for things like starting projects
and other core functionality.

Type ```django-admin startproject django_todo .```   OR ```django-admin startproject <project_name_wareva> .```
Remember to put a dot at the end of the command - this will signify that we want to create this project in the current directory.
If we look in the file explorer now we'll see we have two new items we've got `Django_todo/project_name` And `manage.py`
This is our project directory. The django_todo folder.
manage.py is a management utility we'll need throughout the project.
In the django_todo folder:

```__init__.py``` file - automatically created, tell our project that this is a directory we can import from.

settings.py contains the global settings for our entire Django project.

urls.py contains the routing information that allows our users to type a specific
URL into their address bar. And hit a specific Python function.
So this is analogous to app.root in flask.

wsgi.py which contains the code that allows our web server to communicate with our Python application.

in CLI to run project, type ```python3 manage.py runserver```

new items automatically generated when first ran project e.g. ``__pycache``` (- which contains complied python code) and ```db.sqlite3```, dont touch this one - acts as our databse for the project - do not delete or adjust. 

APPS
Create apps

CLI- ```python3 manage.py startapp todo``` - creates an app called todo. new folder appears
with lots of files in it. 

views.py = 
update view.py to look like:

```
from django.shortcuts import render, HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse("Hello!")
```

make it available to web browser via url.py
in url.py, import the function you made in views.py (say_hello in this example). so, in the section with:

```
from django.contrib import admin
from django.urls import path
```
just add ```from todo.views import say_hello``` underneath them
```
and add ```path('hello/', say_hello, name='hello')``` in the url patterns.
looks like this overall:
```
from django.contrib import admin
from django.urls import path
from todo.views import say_hello

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', say_hello, name='hello')
]
```
run it again, and in url on top of browser (should show error on-screen), just type /hello in top url.

"Django provides a templating system which allows us
to create HTML files in a template directory inside of each app.
And then we render those templates with our Python functions instead of rendering
simple HTTP responses or long drawn-out strings of HTML like this."

create `templates` folder in the `todo` app folder.
create `todo` folder in the newly created `templates` folder.
create `todo_list.html` FILE in newly created todo folder.

"The reason that we're creating this secondary todo folder inside the templates directory
is because when Django looks for templates inside of these apps it will always return the first one that it finds.
So by separating it into a folder that matches its app name.
We can ensure that we're getting the right template even if there's another template of the same name in a different app."

in the  `todo_list.html` template, type ```html``` here and arrow down to the "html:5" item and press enter.
this will generate the basic boilerplate. gitpod shortcut.

witin the <body> add  <h1>Things I need to do</h1>


In the views.py, replace ```return HttpResponse("Hello!")``` with ```return render(request, 'todo/todo_list.html')```

The render function (render is  imported into the views.py file when we created our app originally) takes an HTTP request and a template name as it's two arguments

rename function from ```say_hello``` to ```get_todo_list``` and delete the HttpResponse at the top of the imports.

In urls.py - 
"First of all this hello URL is actually kind of annoying
because when we launched the project without that URL we get the page not found error
that you've seen at the beginning of this video and the end of the last one.
It also doesn't really apply to what we're doing so I'm gonna actually wipe it out completely.
And instead, I'm gonna replace it with just an empty string.
This means that we don't need to specify any particular URL in order to hit that Python function
so this is gonna act as our home page.
I'm also gonna update the view function that this path returns to our new get_todo_list function
And I'm gonna rename it so that the name matches the function it returns.
So we'll change this to get to do list as well.
Since this is our home page we could also call this something like home."#

then update imports, so everything should now look like:
```
from django.contrib import admin
from django.urls import path
from todo.views import get_todo_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_todo_list, name='get_todo_list')
]
```

go to settings.py under our project django_todo folder, and add add our "todo" app to the list of installed apps.
And this is going to allow Jango to know to look inside of that app folder for a templates directory. should look something like: ~ add our app to the bottom:

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'todo'
]
```

run the app if it's not already running. Cool.

MIGRATIONS: see bookmarked ms4> initial django setup vids- hello dhango part3
Save all files first, then put code in CLI:

step 1 - Make migrations --dry-run
```python3 manage.py makemigrations --dry-run```
Note: Runs a test migration run. 

step 2 - Show migrations
```python3 manage.py showmigrations ```
Note: Optional 

step 3 - Make migrations
```python3 manage.py makemigrations```

step 4 - Migrate
```python3 manage.py migrate --plan```
Note: Optional 

step 5 - Migrate
```python3 manage.py migrate```

"Now that that's done. there's one more thing I want to accomplish here.
And that's giving us a way to actually log in and look at the tables in our database
And potentially make changes to them if we need to.
To do that I'm going to use the command ```python3 manage.py createsuperuser```
And it's going to ask me for a username which I'll fill in as `ckz8780`
An email address which I'll leave blank.
And a password which I'll fill out and confirm 
And we can see the superuser was created successfully."

run the app with ```python3 manage.py runserver```
and type "/admin" in url of browser. log in page appears. type the log in details.

done.


Models
Re-Watch "Full Stack Frameworks With Django > Hello Django > Models > Models Part 1"

"For now just remember that if you need functionality from one class to be available in another.
All you need to do is inherit the one you need."

In the "models.py" file inside of the "todo" app, define the following class:

```
class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)
```

"The `null=false` attribute prevents items from being created without a name programmatically
and `blank=false` will make the field required on forms.
This way we're certain that a todo item can't be created without a name
whether it's done in Python code or by a user in a web form or even an administrator in the admin panel."

That's the Item class created, now we need to actually create the table in the database

stop server if running, ctrl+c
in CLI write, ```python3 manage.py makemigrations --dry-run``` to check what it's going to do first.
check, if happy, write ```python3 manage.py makemigrations``` to actually do it.
check, to see migrations by writing ```python3 manage.py showmigrations```
migrate the newly made file by writing ```python3 manage.py migrate --plan``` to check what'll be done first
then run ```python3 manage.py migrate``` to actually do it



"Even though the items table has been created and we could start creating
items programmatically now, we won't be able to see our items in the admin until we expose them.
To do that we need to register our model in the "todo" apps "admin.py" file."

in the `admin.py` file import our Item model from .models, at the top of the page. we're going to use the `admin.site.register` function to actually register our item model.sooooooo, it looks like:
```
from django.contrib import admin
from .models import Item

admin.site.register(Item)
```

save and run project. in browser, open up /admin again. you can see a new Items table added there.
to create a new item in the table, click Items, then "Add item" on top far-right and fill out form with

-Create Item class, tick the "done" checkbox and save. create another item by "Add item" button again, and add
-Register Item model, tick the "done" checkbox and save.

"And we can see that these items have been created but they don't have very friendly names.
So let's make one last change to our model just to clean that up.
The item object value in the admin is actually coming from the fact that we
inherited the base Django model class. When we created our item model.
By default all models that inherit this base model class will use its built-in string
method to display their class name followed by the word object.
Just so that there's sort of a generic way to display them.
And you can actually see this method defined in the base model class in django.db.models.base.
If you want to take a look. You can see the string method right here."

        https://github.com/django/django/blob/main/django/db/models/base.py

        ```
        def __str__(self):
                return "%s object (%s)" % (self.__class__.__name__, self.pk)
        ```

to change this, we need to override the django default naming convention soooooo....,

in models.py type:
```
def __str__(self):
        return self.name
```

so that models.py now looks like: 

```
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name
```

"And this is going to take in self. Which is the class itself as its own argument.
And all it's going to do is just return self.name.
So this is going to return the item class's name attribute which in our case
is going to be the name that we put into the form.
So this is the beauty of class inheritance we still get all of the default functionality
of the default Django model class.
But we can override this string method just to change how our items are displayed.
Doing this will make sure that in the admin we see our item names instead of item object."

save, run again and go go to admin in browser,

"We'll see that the items that we've created now display their names. Instead of the generic values that were displayed before."
-----


Rendering Data
"we set up our item model and put a couple of items in the database.
The next thing we need is a way to display that to our users.
So we need to find a way to get those items from the database into a template."

in view.py, write ```from .models import Item``` under the other imports


"We need access to the Item model in this file so the first thing I'm going to do is right at the top: ```from .models import Item```.
That's going to allow us to use the Item model in our views.
In the `get_todo_list` function, we can then get what's called a query set of all the items in the database.
By creating a variable. Let's call it `item = item.objects.all()`
And since this is going to return multiple items let's call it `items`.

Next I'm going to create a variable called `context`. Which is just going to be a dictionary with all of our items in it.
So it needs a key of 'items'. And that value is going to be our items variable that we just created.
And finally I'm going to add that context as a third argument to the render function.
And this will ensure that we have access to it in our todo_list.html template."

so....everything should now look like:
```
from django.shortcuts import render
from .models import Item

def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)
```

run app again via CLI, ```python3 manage.py runserver```, and make sure you're on the homepage.

there won't be any notieceable changes because we haven't altered the template file yet.

in templates > todo > `todo_list.html` enter a template variable (double curly brakets ```{{}}```), under the heading.

"We can render the items key from the context dictionary that we just created using this double curly bracket syntax."

so, in the todo_list.html file add:

```{{ items }}``` under the h1 heading added earlier.

Refresh browser. it shows, but a bit messy.

"We can adjust the syntax slightly to turn it into a loop that will iterate through our items.
In Django templates any template variables we'll use this double curly bracket syntax.
And any other kinds of functionality like for loops, for example, wi'll use this
opening and closing curly bracket % sign syntax which looks like this, for example: 
{% for item in items %}
{% endfor %}"

sooooo...delete the previously added item variable, in the body of html, and just add this instead, under the h1.

```
    <table>
        {% for item in items %}
            <tr>
                <td>{{ item.name }}</td>
                <td>{{ item.done }}</td>
            </tr>
        {% endfor %}
    </table>
```

add it to be this now:

```
    <table>
        {% for item in items %}
            <tr>
                {% if item.done %}
                    <td><strike>{{ item.name }}</strike></td>
                {% else %}
                    <td>{{ item.name }}</td>
                {% endif %}
            </tr>
        {% endfor %}
    </table>
```

double check if the info on the homepage mirror the data in the /admin database. in Items > Register item model...untick the Done box and Save.
refresh homepage, should now only have 1 of 2 crosssed out.

"There's one last thing i'd like to add here and that's to handle what should
happen if our database doesn't have any todo items in it.
To handle that we can use a special tag called empty. Right before the endfor tag."
```
    <table>
        {% for item in items %}
            <tr>
                {% if item.done %}
                    <td><strike>{{ item.name }}</strike></td>
                {% else %}
                    <td>{{ item.name }}</td>
                {% endif %}
            </tr>
        {% empty %}
        <tr><td>You have nothing to do.</td></tr>
        {% endfor %}
    </table>
```

" go back to the admin. Open up the items table. Delete all the items. Refresh homepage.
Our template will now show us that we have nothing to do."

"users of our todo list app still don't have a way to actually interact with that data such as the ability to create their own todo
items or mark them as complete. In this video we're going to cover the first part of a concept known as CRUD. Which stands for create, read, update, and delete.
By giving users the ability to create their own to-do items. Generally, with crud, you'll want different templates for different operations.
Our home page at the moment represents the read operation in crud. 
To give users the ability to create an item - duplicate the todo_list.html template.
Rename it to add_item.html. Then we'll open this new template."

just delete most of the body html and leave just a heading saying ```<h1>Add a Todo item:</h1>```

back in the todo_list.html file, add a link to link from this to the newly created add_item.html by updating the file to have ```<a href="/add">Add an Item</a>```
just under the table.

we need a view (function) to display this template. so go to views.py, add this to the bottom:
```
def add_item(request):
    return render(request, 'todo/add_item.html')
```

"Lastly we need a new URL to access this template because right now
if we click the link to add an item we'll get a page not found error."

so, go to urls.py, update it to look:
```
from django.contrib import admin
from django.urls import path
from todo.views import get_todo_list, add_item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_todo_list, name='get_todo_list'),
    path('add', add_item, name='add')
]
```

back in add_item.html template, time to create the html to add an item. Under the h1, type:

```
    <form method="POST" action="add">
        <div>
            <p>
                <label for="id_name">Name: </label>
                <input type="text" id="id_name" name="item_name">
            </p>
        </div>
        <div>
            <p>
                <label for="id_done">Done: </label>
                <input type="checkbox" id="id_done" name="done">
            </p>
        </div>
        <div>
            <p>
                <button type="submit">Add Item</button>
            </p>
        </div>
    </form>
```

"we do need to add a special template tag to the form as a security measure.
Just inside the opening form tag whenever we're posting information in Django.
We need to add the CSRF or cross-site request forgery token.
This token is a randomly generated unique value which will be added
to the form as a hidden input field when the forms submitted.
And works to guarantee that the data we're posting is actually coming from our
todo list app and not from another website."

soooo, add ```{% csrf_token %}``` just under the form method="post" etc line of what we just added.

go to views.py, update add_item part to look like:
```

```
and also add "redirect" to the list of django.shortcuts imports (after rednder. no need for new line. just ", redirect")

open app and add item in browser, test it.

--
Create a new file called forms.py in the todo directory and fill it with:
```
from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'done']

```

go to view.py, write ```from .forms import ItemForm``` and update the add_item to be:
```
    if request.method == 'POST':
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('get_todo_list')
    form = ItemForm()
    context = {
        'form': form

    }
    return render(request, 'todo/add_item.html', context)
```

"This means that in the add item template we can now go delete all the fields we created ourselves.
And instead render the form just like we would any other template variable."
sooooo, go to add_item.html and just deelte the form section (the div and under) to look like this:
```
    <form method="POST" action="add">
        {% csrf_token %}
        {{ form }}
        <div>
            <p>
                <button type="submit">Add Item</button>
            </p>
        </div>
    </form>
```

run the app, try to add an item. it should produce an error. fix this by going to view.py and update the add_item to look like:
```
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
```

"You probably notice that when we removed our own form elements we
lost the vertical layout.
To get that back Django forms actually have a number of built-in methods we can use in the template.
Such as. As p which will render the fields as paragraphs. And as table. Which will render them as a table.
I'll use as p here to get our vertical styling back."

soooo, to do the above - go to add_item.html and update the form variable {{ form }} to {{ form.as_p }}



edit - CRUD element

in the todo_list.html file, update to look like:
```
<body>
    <h1>Things I need to do:</h1>
    <table>
        {% for item in items %}
            <tr>
                {% if item.done %}
                    <td><strike>{{ item.name }}</strike></td>
                {% else %}
                    <td>{{ item.name }}</td>
                {% endif %}
                <td>
                    <a href="/edit/{{ item.id }}">
                        <button>Edit</button>
                    </a>
                </td>
            </tr>
        {% empty %}
        <tr><td>You have nothing to do.</td></tr>
        {% endfor %}
    </table>
    <a href="/add">Add an Item</a>
</body>
```
"The href on the link will point to a new URL we'll create in a moment.
We'll also append the items_id which is automatically generated by Django."

in views.py, add a new view to the bottom:
```
def edit_item(request, item_id):
    return render(request, 'todo/edit_item.html')
```
"Along with taking in the request, this view will also take in an 'item_id' parameter.
And that's the 'item_id' we just attached to the Edit link.
Also, this view will return a different template called edit_item.html
Let's save this for now and create the edit_item template."

duplicate add_item.html template. Rename it to edit_item.html. Update the html to look like:

```
<body>
    <h1>Edit a Todo item:</h1>
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <div>
            <p>
                <button type="submit">Update Item</button>
            </p>
        </div>
    </form>
</body>
```

in urls.py, update to look like:
```
from django.contrib import admin
from django.urls import path
from todo.views import get_todo_list, add_item, edit_item

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_todo_list, name='get_todo_list'),
    path('add', add_item, name='add'),
    path('edit/<item_id>', edit_item, name='edit')
]
```
"This angular bracket syntax ```<item_id>``` is common in Django URLs.
It's the mechanism by which the item_id makes its way from links or forms
in our templates, through the URL and into the view which expects it as a parameter."

go to views.py and in the edit_item view, update it to look like:
```
def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)
```
also, import `get_object_or_404` at the very top, add it to the list after ", redirect"

"Let's first get a copy of the item from the database. We can do this using a built in 
django shortcut called "get_object_or_404" which we'll use to say we want to get an instance of the item model.
With an id=item_id that was passed into the view via the URL.
This method will either return the item if it exists. Or a 404 page not found if not.
Then just like above we'll create an instance of our item form and return it to the template in the context.
To pre-populate the form with the items current details.
We can pass an instance argument to the form.
Telling it that it should be prefilled with the information for the item we just got from the database."

save and run the app again...

"But when we update it. it still doesn't actually update because we haven't written a post handler 
in the Edit item view. copy the entire handler from the add_item view and paste it in here.
Making only one small change and that's to give our form the specific item instance we want to update."

update the edit_view view to now be:
```
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
```

in todo_list.html, update the html to just add a toggle option:
```
<body>
    <h1>Things I need to do:</h1>
    <table>
        {% for item in items %}
            <tr>
                {% if item.done %}
                    <td><strike>{{ item.name }}</strike></td>
                {% else %}
                    <td>{{ item.name }}</td>
                {% endif %}
                <td>
                    <a href="/toggle/{{ item.id }}">
                        <button>Toggle</button>
                    </a>
                </td>
                <td>
                    <a href="/edit/{{ item.id }}">
                        <button>Edit</button>
                    </a>
                </td>
            </tr>
        {% empty %}
        <tr><td>You have nothing to do.</td></tr>
        {% endfor %}
    </table>
    <a href="/add">Add an Item</a>
</body>
```

go to urls.py and update to:
```
from django.contrib import admin
from django.urls import path
from todo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_todo_list, name='get_todo_list'),
    path('add', views.add_item, name='add'),
    path('edit/<item_id>', views.edit_item, name='edit'),
    path('toggle/<item_id>', views.toggle_item, name='toggle')
]
```
"You might notice now that if we import the toggle item view.
Our list of imports here at the top is getting quite long.
So let's change this slightly just to clean it up.
Instead of importing each view individually.
I'll just remove them all and change the import to from to do import views.
Now I can simply add views dot in front of all the views.
And everything is exactly the same. But a little less verbose."

go to views.py:
"This one won't even have a template because it's just going to toggle the item status.
And then redirect back to the to-do list."
and add this:

```
def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    # Change it's done status to the opposite by using not.
    item.done = not item.done
    item.save()
    return redirect('get_todo_list')
```

Delete CRUD functionality.

still in views.py, add:
```
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')
```

go to urls.py and update to add this at the bottom:
```
path('delete/<item_id>', views.delete_item, name='delete'),
```

and in the todo_list.html, add another button by:
```
                <td>
                    <a href="/delete/{{ item.id }}">
                        <button>Delete</button>
                    </a>
                </td>
```

DONE.


TESTING.
WATCH testing videos: Full Stack Frameworks With Django > Hello Django > Testing > Django Testing



DEPLOYMENT:

login to heroku via CLI: `heroku login -i`

"we'll use an add-on for Heroku Which will allow us to use a server-based database called Postgres.
This will be separated from our application, so it'll survive even if the application 
server is destroyed. To use Postgres in our application. We need to install a package called
psycopg2, Which we can do with `pip3 install psycopg2-binary`
Later on, we'll add the Heroku add-on to set it up, but this will take care of the Django side."

W"e'll also need a package called gunicorn. Or green unicorn.
This will replace our development server once the app is deployed to Heroku.
Gunicorn will act as our web server. Install it using `pip3 install gunicorn`"

`pip3 freeze --local > requirements.txt`
This requirements file is how Heroku will know what it needs to install for our app to work.
Specifically, it'll tell Heroku all the packages it needs to install using pip.

create a heroku app:
make sure you're looged in on the CLI, `heroku login -i`
`heroku apps:create ckz8790-django-todo-app --region eu`
(or name it anything you want)
"--region eu" specifies EU region (it will automatically choose US if you leave this out):

`heroku apps` should list your newly created app

heroku website. go to Resources > Add Ons, search Postgres and choose Heroku Postgres.
Make sure your plan name is correct (free, in this case) and confirm (Submit Order Form button)

("It's worth mentioning that if you wanted to do this with MySql instead of Postgres, uou 
would follow an almost identical process but use an add-on called "clearDB" instead.")

Config Vars
go to heroku website > Settings tab > Reveal Config Vars button. There should be
a DATABASE_URL automatically generated by heroku after the last step.



Setup django to connect to our remote database

in gitpod CLI: `pip3 install dj_database_url` then `pip3 freeze --local > requirements.txt`
then `heroku config` (same as getting it from config vars in heroku)

go to settings.py
copy and paste the DATABASES info right below the original, then comment out the original.
update the newly made(pasted) DATABASES to be:
```
DATABASES = {
    'default': dj_database_url.parse('<copy_database_url_here')
}
```
...and add "import dj_database_url" towards the top with the other imports/from styff

"Since we're now using a different database the one that exists on heroku (postres, 
in heroku, unless you installed mysql earlier instead). It won't have any of our models 
or user information in it. So to get it all set up to match the sqlite3 database 
(here in gitpod). We need to run migrations. There's no need to make migrations in 
this case since they've already been made. But we can run them as usual with 
`python3 manage.py migrate` Even though our code hasn't even been deployed.
The fact that we're now able to run these migrations on the remote database
means that everything is set up correctly so far."

push to github by:
`git remote -v` to check. we want to push to origin, not heroku

create ".gitignore" file in root, if it's not already there (with CI template, it should)
add `*.sqlite3` to add all files with an sqlite3 extension and `__pycache__/` to ".gitignore"

ready to push: 
git add . (to add all)
git commit -m "prepared to deploy to heroku"
git push origin main

next, deploy to heroku:
git push heroku main
I had an error first time, so type this in CLi, if related
`heroku config:set DISABLE_COLLECTSTATIC=1` OR
`heroku config:set DISABLE_COLLECTSTATIC=1 --app ckz8790-django-todo-app`
(replace ckz...etc with your app name)
I suppose the same can be done in Config Vars through heroku.

try opening app through heroku (Open App button on top-right). itll failt.
`heroku logs --tail` back in gitpod cli. list fo errors, handy for future use. can search google e.g "heroku error code h14"

create Procfile in root. type: `web: gunicorn django_todo.wsgi:application` in it

git add Prcfile
git commit -m "Added Procfile"
git push heroku main

open app through heroku again. it'll load, but with an error.

read the error, then in settings.py, add it to look like:

`ALLOWED_HOSTS = ['ckz8790-django-todo-app.herokuapp.com']`

git add django_todo/settings.py (or git add .)
git commit -m "fixed allowed hosts"
git push heroku main

then, push to own repo:
git push origin main

open app in heroku again, and test. should work fine.


Connecting Heroku to Github (automated deployment unavaiable atm due to heroku security issues)
add `import os` to the top settings.py file, with the other imports (no need on older versions, already there)
and the secret_key section to be:

`SECRET_KEY = os.environ.get('SECRET_KEY', 'your_default_value_here')`
where your_default_value_here is the one in settings.py already. some jumbled code.
and...update ALLOWED_HOSTS to be:
`ALLOWED_HOSTS = [os.environ.get('HEROKU_HOSTNAME')]`

and...update DATABASES to be:
```
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
}
```

go to heroku, and add the environment variable in the config vars:
```
HEROKU_HOSTNAME: ckz8790-django-todo-app.herokuapp.com (your app address without the http:// and / at the end)
```

go to "todo_list.html" and change title at top to Todo List instead of app. Do the same to "edit_item.html" but
Edit Item as title, and Add Item in "add_item.html".

git add .
git commit -m "Set up environment variables and deployment"
git push origin main