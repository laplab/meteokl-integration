from peewee import *

db = SqliteDatabase('weather.db')


class Entry(Model):
    time = DateTimeField()
    inner_temperature = IntegerField()
    outer_temperature = IntegerField()
    pressure = IntegerField()
    humidity = IntegerField()
    wind_speed = IntegerField()
    wind_direction = IntegerField()

    class Meta:
        database = db
        order_by = ('-time',)
