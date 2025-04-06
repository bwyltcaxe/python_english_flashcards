from django import forms
from .models import Collection

class CardForm(forms.Form):
    word = forms.CharField(max_length=128, widget=forms.TextInput(attrs={
        'placeholder': 'Введите слово',
        'class': 'form-control'
    }))
    explanation = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Введите объяснение',
        'class': 'form-control',
        'rows': 3
    }))
    collection = forms.ModelChoiceField(
        queryset=Collection.objects.all(),
        empty_label="Выберите коллекцию",
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    new_collection = forms.CharField(
        max_length=128,
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Или создать новую коллекцию',
            'class': 'form-control'
        })
    )

    def clean(self):
        cleaned_data = super().clean()

