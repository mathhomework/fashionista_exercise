# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fashionista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=75)),
                ('phone_number', models.CharField(max_length=15)),
                ('fb', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('blog', models.URLField(blank=True)),
                ('desc', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
