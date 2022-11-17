from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from decouple import config
from celery.schedules import crontab

# setting the Django settings module.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'theClassified.settings')
app = Celery('fintank')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Looks up for task modules in Django applications and loads them
app.autodiscover_tasks()


app.conf.beat_schedule = {
    # 'multiply-task-crontab': {
    #     'task': 'multiply_two_numbers',
    #     'schedule': crontab(hour=7, minute=30, day_of_week=1), # every Monday at 7:30 am 
    #     'args': (16, 16),
    # },
    # 'multiply-task-crontab': {
    #     'task': 'multiply_two_numbers',
    #     'schedule': crontab(minute=0, hour='*/3'), # runs every 3 hours
    #     'args': (16, 16),
    # },
    'economic_news': {
        'task': 'get_economic_articles',
        'schedule': crontab(minute='*/15'), # runs every 15 minutes
        'args': ()
    },
    'market_news': {
        'task': 'get_market_articles',
        'schedule': crontab(minute='*/15'), # runs every 15 minutes
        'args': ()
    },
    'tech_news': {
        'task': 'get_tech_articles',
        'schedule': crontab(minute='*/15'), # runs every 15 minutes
        'args': ()
    },
    'inflation_news': {
        'task': 'get_inflation_articles',
        'schedule': crontab(minute='*/15'), # runs every 15 minutes
        'args': ()
    },
    'politics_news': {
        'task': 'get_politics_articles',
        'schedule': crontab(minute='*/15'), # runs every 15 minutes
        'args': ()
    },
    'energy_news': {
        'task': 'get_energy_articles',
        'schedule': crontab(minute='*/15'), # runs every 15 minutes
        'args': ()
    },
    'us_news': {
        'task': 'get_us_news_articles',
        'schedule': crontab(minute='*/15'), # runs every 15 minutes
        'args': ()
    },
    'china_news': {
        'task': 'get_china_news_articles',
        'schedule': crontab(minute='*/15'), # runs every 15 minutes
        'args': ()
    },
    'russia_news': {
        'task': 'get_russia_news_articles',
        'schedule': crontab(minute='*/15'), # runs every 15 minutes
        'args': ()
    },
    'mid_east_news': {
        'task': 'get_mid_east_articles',
        'schedule': crontab(minute='*/15'), # runs every 15 minutes
        'args': ()
    },
    'german_news': {
        'task': 'get_german_news_articles',
        'schedule': crontab(minute='*/15'), # runs every 15 minutes
        'args': ()
    },
    'japan_news': {
        'task': 'get_japan_news_articles',
        'schedule': crontab(minute='*/15'), # runs every 15 minutes
        'args': ()
    },'africa_news': {
        'task': 'get_africa_news_articles',
        'schedule': crontab(minute='*/15'), # runs every 15 minutes
        'args': ()
    },'south_am_news': {
        'task': 'get_south_am_articles',
        'schedule': crontab(minute='*/15'), # runs every 15 minutes
        'args': ()
    },'oil_news': {
        'task': 'get_oil_articles',
        'schedule': crontab(minute='*/15'), # runs every 15 minutes
        'args': ()
    },'war_news': {
        'task': 'get_war_articles',
        'schedule': crontab(minute='*/15'), # runs every 15 minutes
        'args': ()
    },
    'multiply-every-5-seconds': {
        'task': 'multiply_two_numbers',
        'schedule': 5.0, #in seconds
        'args': (16, 16)
    },
    'multiply-every-5-seconds': {
        'task': 'multiply_two_numbers',
        'schedule': crontab(minute='*/15'), # runs every 15 minutes
        'args': (16, 16)
    },
    'add-every-30-seconds': {
        'task': 'sum_two_numbers',
        'schedule': 30.0,
        'args': (16, 16)
    },
}

# celery -A theClassified worker --beat

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))