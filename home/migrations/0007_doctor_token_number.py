# Generated by Django 2.2.3 on 2019-07-11 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20190712_0011'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='token_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Token number'),
        ),
    ]