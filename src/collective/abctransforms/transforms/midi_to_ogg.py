# -*- coding: utf-8 -*-
"""
Uses timidity
"""
import logging
from zope.interface import implementer
from Products.PortalTransforms.interfaces import ITransform
from Products.PortalTransforms.libtransforms.commandtransform import (
    popentransform)
from plone import api
from collective.abctransforms.utils import from_to
from collective.abctransforms.interfaces import IABCTransformsSettings

logger = logging.getLogger('collective.abctransforms')


@implementer(ITransform)
class midi_to_ogg(popentransform):

    __name__ = "midi_to_ogg"
    inputs = ('audio/midi',)
    output = 'audio/ogg'

    __version__ = '2015-10-31.01'

    binaryName = "timidity"
    useStdin = False

    def convert(self, orig, data, **kwargs):
        """
        Convert MIDI to OGG
        """
        context = kwargs.get('context')
        annotate = kwargs.get('annotate')
        s_cmd = api.portal.get_registry_record(
            'midi_to_ogg',
            interface=IABCTransformsSettings)
        cmd = eval(s_cmd)
        ogg = from_to(
            orig,
            cmd,
            inputsuffix='.mid',
            outputsuffix='.ogg',
            context=context,
            annotate=annotate,
            )
        data.setData(ogg)
        return data


def register():
    return midi_to_ogg()
