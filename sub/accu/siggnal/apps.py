from django.apps import AppConfig

class SiggnalC(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'siggnal'

    def ready(self):
        import siggnal.signals
