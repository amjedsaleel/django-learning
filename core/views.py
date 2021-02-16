from django.shortcuts import render, redirect
from .models import Language, Programmer
from django.forms import modelformset_factory, inlineformset_factory


# Create your views here.


def index(request, programmer_id):
    programmer = Programmer.objects.get(pk=programmer_id)
    # language_formset = modelformset_factory(Language, fields=('name',))
    language_formset = inlineformset_factory(Programmer, Language, fields=(
        'name',), extra=2, validate_min=3,)  # Parent model, Chilled model (Programmer, Language), field name is of parent

    if request.method == 'POST':
        # formset = language_formset(request.POST, queryset=Language.objects.filter(programmer__id=programmer.id))
        formset = language_formset(request.POST, instance=programmer)

        if formset.is_valid():
            formset.save()
            # instances = formset.save(commit=False)

            # for instance in instances:
            #     instance.programmer_id = programmer.id
            #     instance.save()
            #     return redirect('index', programmer_id=programmer_id)

    # formset = language_formset(queryset=Language.objects.filter(programmer__id=programmer.id))
    formset = language_formset(instance=programmer)

    return render(request, 'index.html', {'formset': formset, 'programmer_id': programmer_id})
