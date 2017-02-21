# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import six
from django.utils.encoding import python_2_unicode_compatible, force_text
from django.utils.functional import lazy
from django.utils.translation import ugettext_lazy as _

from aldryn_segmentation.models import SegmentBasePluginModel


@python_2_unicode_compatible
class WaffleSegmentPluginModel(SegmentBasePluginModel):
    flag = models.ForeignKey(
        'waffle.Flag',
        verbose_name=_('Flag'),
    )

    def __str__(self):
        if self.flag_id:
            return force_text(self.flag.name)
        else:
            return force_text(self.pk)


    @property
    def configuration_string(self):

        def wrapper():
            return _('Flag: {flag}').format(flag=self.flag)

        return lazy(
            wrapper,
            six.text_type
        )()
