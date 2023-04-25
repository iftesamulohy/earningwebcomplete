from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from datetime import date

from myapp.models import Deposit, User,Withdraw,PackageOrder,CompleteTask

@receiver(post_save, sender=Deposit)
def update_balance(sender, instance, **kwargs):
    if instance.status == 'Complete':
        balance = User.objects.get(username=instance.user.username)
        print(balance)
        balance.balance += instance.amount
        balance.save()

@receiver(post_save, sender=Withdraw)
def update_balance(sender, instance, **kwargs):
    if instance.status == 'Complete':
        balance = User.objects.get(username=instance.user.username)
        print(balance)
        balance.balance -= instance.amount
        balance.save()
@receiver(post_save, sender=PackageOrder)
def update_balance_on_purchase(sender, instance, **kwargs):
    if instance.status == 'Activate':
        balance = User.objects.get(username=instance.user.username)
        print(balance)
        balance.balance -= instance.package.amount
        balance.save()

@receiver(post_save, sender=CompleteTask)
def update_balance_on_purchase(sender, instance, **kwargs):
    if instance.status == 'Approved':
        balance = User.objects.get(username=instance.user.username)
        print(balance)
        balance.balance += instance.work.reaward_amount
        balance.save()

@receiver(post_save, sender=PackageOrder)
def update_balance_on_purchase(sender, instance, **kwargs):
    if instance.status == 'Activate' and instance.user.refferedby:
        balance = User.objects.get(username=instance.user.refferedby)
        print(balance)
        balance.balance += instance.package.refer_bonus
        balance.save()

