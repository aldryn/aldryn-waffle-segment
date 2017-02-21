# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0013_urlconfrevision'),
        ('waffle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WaffleSegmentPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='aldryn_waffle_segment_wafflesegmentpluginmodel', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('label', models.CharField(default='', max_length=128, verbose_name='label', blank=True)),
                ('flag', models.ForeignKey(verbose_name='Flag', to='waffle.Flag')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
