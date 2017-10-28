from django.apps import AppConfig

class AppnameConfig(AppConfig):
    name = 'appname'
    init = True

    def ready(self):
        pass
