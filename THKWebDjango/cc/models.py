# -*- coding: utf-8 -*-
from django.db import models
import datetime
from django.utils.timezone import utc


class ChainEvent(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=64)
    rank_type = models.IntegerField(default=0)
    pts = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    timestamp = models.DateTimeField(default=datetime.datetime.today().replace(tzinfo=utc))

    class Meta:
        db_table = 'chain_event'

    @staticmethod
    def get_rank_type():
        return {
            '0': u'',
            '1': u'第1名',
            '2': u'第1000名',
            '3': u'第5000名',
            '4': u'第20000名',
            '5': u'第50000名',
            '6': u'第80000名',
            '7': u'第100000名',
            '8': u'第200000名',
        }

    @staticmethod
    def get_rank_list():
        return {
            '1': 1,
            '2': 1000,
            '3': 5000,
            '4': 20000,
            '5': 50000,
            '6': 80000,
            '7': 100000,
            '8': 200000,
        }

