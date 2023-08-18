from django.db import models
from django.contrib.auth import get_user_model

from django.utils.translation import gettext_lazy as _
# Create your models here.

User = get_user_model()

class Medicine(models.Model):
    order = models.IntegerField(verbose_name='number',default=0,null=True)
    name = models.TextField(verbose_name='medicine_name',null=True,default='')
    classification = models.TextField(verbose_name='medi_classification',null=True,default='')
    Ingredients_amount = models.TextField(verbose_name='Ingredients_amount',default='',null=True)
    efficacy = models.TextField(verbose_name='efficacy',null=True)
    infomation = models.TextField(verbose_name='infomation',default='',null=True)
    warning = models.TextField(verbose_name='warning',null=True,default='')
    storage = models.TextField(verbose_name='storage',null=True,default='')
    doping = models.TextField(verbose_name='doping',null=True,default='')
    usage = models.TextField(verbose_name='usage',null=True,default='')


class Scrap(models.Model):


    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='scrap',
        null=True,
        blank=True,
    )

    user_email = models.CharField(
        verbose_name=_('user email'),
        max_length=50,
        null=True,
        blank=True,
    )


    medi_id = models.IntegerField(
        default=0
        )
    
    medi_name = models.TextField(
        null=True,
        blank=True,
        default=''
    )
