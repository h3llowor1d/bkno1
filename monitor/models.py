# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Chengfa(models.Model):
    chengshu = models.IntegerField(u"乘数")
    beichengshu = models.IntegerField(u"被乘数")
    cfresult = models.IntegerField(u"结果")

def __unicode__(self):
    return "%d * %d = %d" %(self.chengshu, self.beichengshu,self.cfresult)