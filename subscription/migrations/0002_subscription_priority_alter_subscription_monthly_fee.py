# Generated by Django 5.0 on 2023-12-22 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='priority',
            field=models.CharField(choices=[('danger', 'high'), ('warning', 'normal'), ('primary', 'low')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='monthly_fee',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
