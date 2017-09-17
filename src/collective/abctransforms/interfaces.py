# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.supermodel import model
from zope.schema import TextLine
from collective.abctransforms import _


class ICollectiveAbctransformsLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IABCTransformsSettings(model.Schema):
    abc_to_midi = TextLine(
        title=_(u'abc To midi command'),
        description=_(u'python list of strings, with "datain" and "dataout"'),
        default=u'["abcm2ps", "datain", "-O", "dataout"]',
        required=True
        )
