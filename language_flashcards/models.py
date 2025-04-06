from django.db import models

class Collection(models.Model):
    name = models.CharField(max_length=128, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Card(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    word = models.CharField(max_length=128)
    explanation = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'language_flashcards'

    def __str__(self):
        return f"{self.word} - {self.explanation[:50]}..."

