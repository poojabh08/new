# Generated by Django 2.2.3 on 2019-07-11 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190711_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_name',
            field=models.CharField(max_length=30, null=True, unique=True, verbose_name='Patient name'),
        ),
    ]