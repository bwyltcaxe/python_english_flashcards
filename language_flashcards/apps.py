"""Language flashcards app configuration is handled here"""
from django.apps import AppConfig

class LanguageFlashcardsConfig(AppConfig):
    """Configuration for language_flashcards app"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'language_flashcards'
    verbose_name = 'Language Flashcards'
