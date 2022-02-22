from django.apps import AppConfig


class RefLinkConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ref_link'

    def ready(self):
        import ref_link.signals

     
