from django.db import models

CHOICE = (('danger', 'high'),('warning', 'normal'),('primary', 'low'))

class Subscription(models.Model):
    magazine_name = models.CharField(max_length=100)
    link = models.URLField()
    monthly_fee = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    priority = models.CharField(
        max_length=100,
        choices= CHOICE,
        null=True
        )

    def __str__(self):
        return self.magazine_name
