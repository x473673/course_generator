from ics import Calendar, Event

import datetime
import random

from generator import course

t=datetime.date.today()
d=t+datetime.timedelta(days=(0-t.weekday())%7) # finds next monday (today if it is monday)
c = Calendar()

for i in range(5):
    s=6 # 8:00 CET is 6:00 UTC
    l=random.randrange(1,4)
    c.events.add(Event(name=str(course(3)), begin='{} {:02d}:00:00'.format(d,s), end='{} {:02d}:50:00'.format(d,s+l-1)))
    s=s+l
    while s<18:
        l=random.randrange(1,4)
        c.events.add(Event(name=str(course(3)), begin='{} {:02d}:00:00'.format(d,s), end='{} {:02d}:50:00'.format(d,s+l-1)))
        s=s+l
    d=d+datetime.timedelta(days=1)

with open('Rozvrh_ucitelstvi_na_pristi_tyden.ics', 'w') as my_file:
    my_file.writelines(c)
