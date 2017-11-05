# -*- coding: utf-8 -*-
"""
Uses timidity
"""
import logging
from zope.interface import implements
from Products.PortalTransforms.interfaces import ITransform
from Products.PortalTransforms.libtransforms.commandtransform import (
    popentransform)
from plone import api
from collective.abctransforms.utils import from_to
from collective.abctransforms.interfaces import IABCTransformsSettings

logger = logging.getLogger('collective.abctransforms')


class midi_to_ogg(popentransform):
    implements(ITransform)

    __name__ = "midi_to_ogg"
    inputs = ('audio/midi',)
    output = 'audio/ogg'

    __version__ = '2015-10-31.01'

    binaryName = "timidity"
    useStdin = False

    def convert(self, orig, data, **kwargs):
        s_cmd = api.portal.get_registry_record(
            'midi_to_ogg',
            interface=IABCTransformsSettings)
        cmd = eval(s_cmd)
        ogg = from_to(
            orig,
            cmd,
            inputsuffix='.mid',
            outputsuffix='.ogg'
            )
        data.setData(ogg)
        return data


def register():
    return midi_to_ogg()
