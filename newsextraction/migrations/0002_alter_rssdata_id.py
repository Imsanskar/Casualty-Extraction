# Generated by Django 3.2.4 on 2021-07-06 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsextraction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rssdata',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]