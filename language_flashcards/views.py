from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def cards_list(request):
    return render(request, 'cards/list.html')

def add_card(request):
    return render(request, 'cards/add.html')

def lessons_list(request):
    return render(request, 'lessons/list.html')

def add_lesson(request):
    return render(request, 'lessons/add.html')

