# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _
from cms.plugin_pool import plugin_pool

import waffle
from aldryn_segmentation.cms_plugins import SegmentPluginBase

from . import models


class WaffleSegmentPlugin(SegmentPluginBase):
    '''
    Plugin that shows or hides content based on a django-waffle flag. 
    '''
    model = models.WaffleSegmentPluginModel
    name = _('Segment by Waffle Flag')

    def is_context_appropriate(self, context, instance):
        request = context['request']
        return waffle.flag_is_active(request, instance.flag)


plugin_pool.register_plugin(WaffleSegmentPlugin)
