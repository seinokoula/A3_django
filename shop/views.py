from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render
from .models import Items, ItemsModel
from .forms import ItemsForm
# Create your views here.


def index(request):

    context = {"Items": Items.objects.all()}
    form = ItemsForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, 'index.html', context)


# view for single item page with id as parameter in url path
def single(request, id):
    context = {"Items": Items.objects.get(id=id)}
    return render(request, 'single.html', context)


def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(ItemsModel, id=id)

    # pass the object as instance in form
    form = ItemsForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_view.html", context)
