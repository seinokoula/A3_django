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


def single(request, id):
    context = {"Items": Items.objects.get(id=id)}
    return render(request, 'single.html', context)


def update_view(request, id):

    context = {}

    obj = get_object_or_404(ItemsModel, id=id)

    form = ItemsForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)

    context["form"] = form

    return render(request, "update_view.html", context)


def delete_view(request, id):

    context = {}

    obj = get_object_or_404(ItemsModel, id=id)

    form = ItemsForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.delete()
        return HttpResponseRedirect("/"+id)

    context["form"] = form

    return render(request, "delete_view.html", context)


def update(request, id):
    context = {"Items": Items.objects.get(id=id)}
    return render(request, 'update.html', context)
