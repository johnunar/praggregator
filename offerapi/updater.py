from apscheduler.schedulers.background import BackgroundScheduler

import offerapi.offerapi


def start():
    """
    The Offer updater calls the update_product function every minute to keep the offers up-to-date.
    """
    scheduler = BackgroundScheduler()
    scheduler.add_job(offerapi.offerapi.update_product, 'interval', minutes=1)
    scheduler.start()
