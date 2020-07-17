from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
from .forms import ContactModelForm


def index(request):
    form = ContactModelForm()
    # if request.method == 'POST':
    #     form = ContactModelForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/')

    if request.is_ajax():
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'msg': 'Success'
            })

    context = {
        'form': form
    }

    return render(request, 'index.html', context)
