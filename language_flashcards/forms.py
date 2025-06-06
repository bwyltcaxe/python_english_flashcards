"""Forms handling for language flashcard service"""
import re
from django import forms
from .models import Collection

class CardForm(forms.Form):
    """
    Card form. It's usable to add and edit new cards.
    Also, the whole validation is handled here (in 'clean' method).
    """

    word = forms.CharField(max_length=32, widget=forms.TextInput(attrs={
        'placeholder': 'Введите слово',
        'class': 'form-control'
    }))
    explanation = forms.CharField(max_length=128, widget=forms.Textarea(attrs={
        'placeholder': 'Введите объяснение',
        'class': 'form-control',
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

        word = cleaned_data.get('word', '').strip()
        explanation = cleaned_data.get('explanation', '').strip()
        new_collection = cleaned_data.get('new_collection', '').strip()

        if not word:
            raise forms.ValidationError('Слово должно быть длиной от 1 до 32 символов')

        if not explanation:
            raise forms.ValidationError('Объяснение должно быть длиной от 1 до 128 символов')

        cleaned_data['word'] = word
        cleaned_data['explanation'] = explanation
        cleaned_data['new_collection'] = new_collection

        if not re.fullmatch(r'[a-zA-Zа-яА-ЯёЁ\s\-]+', word):
            raise forms.ValidationError(
                'Слово может содержать только русские или английские буквы.'
            )

        if not cleaned_data.get('collection') and not new_collection:
            raise forms.ValidationError('Пожалуйста, выберите коллекцию или введите новую')

        if new_collection and not re.fullmatch(r'^[a-zA-Zа-яА-ЯёЁ\s\-]+$', new_collection):
            raise forms.ValidationError(
                'Коллекция может содержать только русские или английские буквы, пробелы и дефисы.'
            )

        return cleaned_data
