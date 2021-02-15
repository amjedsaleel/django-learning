from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from . models import Example

# Create your views here.


def index(request):
    example_formset = modelformset_factory(Example, fields=('name', 'location'), extra=2)

    if request.method == 'POST':
        print('post')
        form = example_formset(request.POST)
        if form.is_valid():

            instances = form.save(commit=False)
            for instance in instances:
                instance.save()

            print('valid')
            # form.save()
            return redirect('index')
    print('get')
    form = example_formset(queryset=Example.objects.none())

    return render(request, 'index.html', {'form': form})
