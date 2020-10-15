from django.apps import AppConfig


class OfferapiConfig(AppConfig):
    name = 'offerapi'

    def ready(self):
        from offerapi import updater, signals  # Signals are imported, so the register_product signal can work
        updater.start()
