# Generated by Django 2.2.26 on 2022-01-08 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]