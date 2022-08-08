from django.shortcuts import render
from django import forms

tasks = ["foo", "bar", "baz"]

class AddTaskForm(forms.Form):
    task = forms.CharField(label='New Task', max_length=50)
    # priority = forms.IntegerField(label='Priority', min_value=1, max_value=10)

# Create your views here.
def index(request):
    if request.method == "POST":
        form = AddTaskForm(request.POST)
        if form.is_valid():
            tasks.append(form.cleaned_data["task"])
            # return render(request, "tasks/index.html", {'tasks': tasks})
    return render(request, 'tasks/index.html', {'tasks': tasks})

def add(request):
    return render(request, "tasks/add.html", {'form': AddTaskForm()})