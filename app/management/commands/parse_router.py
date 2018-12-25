# from ..commands import *
import csv
import re
from collections import namedtuple

from django.core.management.base import BaseCommand
from enum import Enum
from os import walk

from app.models.models import (
    Router,
    Card,
    Interface
)


class Commands(Enum):
    BRIEF = 'brief'
    NEIGHBOR = 'neighbor'
    PLATFORM = 'platform'


class Command(BaseCommand):
    def handle(self, *args, **options):
        files = []
        for (_, _, filenames) in walk('/Khurram/Others/Assignments/stc_django/app/Assignment/'):
            files.extend(filenames)

        for f_name in files:

            platform = False
            brief = False
            neighbor = False
            with open('/Khurram/Others/Assignments/stc_django/app/Assignment/' + f_name) as csv_file:
                csv_reader = csv.reader(csv_file)
                cards = []
                interface = {}
                for row in csv_reader:
                    if not row:
                        continue
                    if Commands.PLATFORM.value in row[0]:
                        platform = True
                        brief = False
                        neighbor = False
                        continue
                    elif Commands.BRIEF.value in row[0]:
                        brief = True
                        platform = False
                        neighbor = False
                        continue
                    elif Commands.NEIGHBOR.value in row[0]:
                        neighbor = True
                        platform = False
                        brief = False
                        continue

                    try:
                        column = re.split('\s+', row[0])
                        if platform:
                           if re.search(r'\d{1,3}X\d+G', column[1]):
                                cards.append({'slot_number': column[0].split('/')[1],
                                              'card_name': column[1],
                                              'interface': {}})

                            # cards.extend(Card(router=router, slot_number=column[0].split('/')[1], card_name=column[1]))
                               # Card.objects.bulk_create(cards)
                        elif brief:
                            if 'interface' in column[0].lower():
                                continue
                            inter = re.sub('[A-z]+', '', column[0]).strip()
                            slot_number = inter.split('/')[1]

                            slots = interface.get(slot_number)
                            if slots:
                                slots.update({inter: {'local_interface': column[0],
                                                      'status': column[2],
                                                      'remote_interface': None,
                                                      'connected_router': None}})
                                continue
                            interface.update({slot_number: {inter: {'local_interface': column[0],
                                                                     'status': column[2],
                                                                     'remote_interface': None,
                                                                     'connected_router': None}}
                                              })
                        elif neighbor:
                            if set(['device', 'router', 'repeater', 'wlan']) & set(map(lambda x: x.lower(), column)):
                                continue
                            inter_no = re.sub('[A-z]+', '', column[1]).strip()
                            slot_no = inter_no.split('/')[1]
                            inter = interface.get(slot_no, {}).get(inter_no)
                            if inter:
                                inter.update({'remote_interface': column[4],
                                              'connected_router': column[0][:column[0].find('.')]})

                    except IndexError:
                        continue
                # print f_name
                # print cards
                # print interface
                for card in cards:
                    slot_n = card.get('slot_number')
                    if slot_n:
                        card.update({'interface': interface.get(slot_n) or {}})

                router, _ = Router.objects.get_or_create(router_name=f_name)
                setattr(router, 'router_name', f_name.replace('.conf', ''))
                router.save()

                all_inter_obj = []
                for card in cards:
                    interface_obj = card.pop('interface', {})
                    card_obj, _ = Card.objects.get_or_create(router=router, **card)
                    for key, val in interface_obj.items():
                        all_inter_obj.append(Interface(card=card_obj, **val))
                Interface.objects.bulk_create(all_inter_obj)
