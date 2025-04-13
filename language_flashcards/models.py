"""Cards models for language flashcards application"""
from django.db import models

class Collection(models.Model):
    """Collection of flashcards grouped by a common theme"""

    name = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name}"

class Card(models.Model):
    """Card contains a word and its explanation (with respect to a collection)"""

    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    word = models.CharField(max_length=128)
    explanation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f"{self.word} - {self.explanation}"
