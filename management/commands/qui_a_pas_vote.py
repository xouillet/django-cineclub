#-*- coding: utf-8 -*-
from cine.models import *
from datetime import date

soiree = Soiree.objects.filter(date__gte=date.today())[0]
for film in Film.objects.filter(categorie=soiree.categorie, vu=False):
    for dispo in DispoToWatch.objects.filter(dispo='O', soiree=soiree):
        vote = Vote.objects.get(cinephile=dispo.cinephile, film=film)
        if vote.choix == 9999:
            print u'%s n’a pas voté pour %s' % (dispo.cinephile, film)
