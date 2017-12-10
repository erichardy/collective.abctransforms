# -*- coding: utf-8 -*-
"""
Uses abcm2ps
"""
import logging
from Products.CMFCore.utils import getToolByName
from zope.interface import implements
from Products.PortalTransforms.interfaces import ITransform
from Products.PortalTransforms.libtransforms.commandtransform import (
    popentransform)
from plone import api

logger = logging.getLogger('collective.abctransforms')


class abc_to_ogg(popentransform):
    implements(ITransform)

    __name__ = "abc_to_ogg"
    inputs = ('text/vnd.abc',)
    output = 'audio/ogg'

    __version__ = '2015-10-31.01'

    def convert(self, orig, data, **kwargs):
        context = kwargs.get('context')
        annotate = kwargs.get('annotate')
        abc = orig
        portal = api.portal.get()
        pt = getToolByName(portal, 'portal_transforms')
        midi = pt.convertTo(
            'audio/midi',
            abc,
            context=context,
            annotate=annotate)
        ogg = pt.convertTo(
            'audio/ogg',
            midi.getData(),
            context=context,
            annotate=annotate)
        data.setData(ogg.getData())
        return data


def register():
    return abc_to_ogg()
