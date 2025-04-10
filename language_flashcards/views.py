from django.shortcuts import render, redirect
from .forms import CardForm
from .models import Collection, Card

def home(request):
    return render(request, 'index.html')

def cards_list(request):
    collection_id = request.GET.get('collection_id')

    if collection_id and collection_id != 'all':
        selected_collection = Collection.objects.get(id=collection_id)
        cards = Card.objects.filter(collection=selected_collection)
    else:
        selected_collection = 'Все карточки'
        cards = Card.objects.all()

    return render(request, 'cards/list.html', {
        "collections": Collection.objects.all(),
        "cards": cards,
        "selected_collection": selected_collection
    })

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

def edit_card(request, card_id):
    card = Card.objects.get(id=card_id)

    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card.word = form.cleaned_data['word']
            card.explanation = form.cleaned_data['explanation']
            card.save()
            return redirect('cards-list')

    return render(request, 'cards/edit.html', {'card': card})

