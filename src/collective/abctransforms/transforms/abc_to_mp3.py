# -*- coding: utf-8 -*-

import logging
from zope.interface import implements
from Products.PortalTransforms.interfaces import ITransform
from Products.CMFCore.utils import getToolByName
from plone import api

logger = logging.getLogger('collective.abctransforms')


class abc_to_mp3():
    implements(ITransform)

    __name__ = "abc_to_mp3"
    inputs = ('text/vnd.abc',)
    output = 'audio/mpeg'

    __version__ = '2015-10-31.01'

    def convert(self, abc, data, **kwargs):
        portal = api.portal.get()
        pt = getToolByName(portal, "portal_transforms")
        midi = pt.convertTo('audio/midi', abc)
        aiff = pt.convertTo('audio/x-aiff', midi.getData())
        mp3 = pt.convertTo('audio/mpeg', aiff.getData())
        data.setData(mp3.getData())
        return data


def register():
    return abc_to_mp3()
