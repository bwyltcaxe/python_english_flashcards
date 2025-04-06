from django.shortcuts import render, redirect
from .forms import CardForm
from .models import Collection, Card

def home(request):
    return render(request, 'index.html')

def cards_list(request):
    return render(request, 'cards/list.html')


def add_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['word']
            explanation = form.cleaned_data['explanation']
            collection = form.cleaned_data['collection']
            new_collection = form.cleaned_data['new_collection']

            if new_collection:
                collection, created = Collection.objects.get_or_create(
                    name=new_collection
                )

            Card.objects.create(
                word=word,
                explanation=explanation,
                collection=collection
            )
            return redirect('add-card')
    else:
        form = CardForm()

    return render(request, 'cards/add.html', {
        'form': form,
        'collections': Collection.objects.all()
    })

def lessons_list(request):
    return render(request, 'lessons/list.html')

def add_lesson(request):
    return render(request, 'lessons/add.html')

