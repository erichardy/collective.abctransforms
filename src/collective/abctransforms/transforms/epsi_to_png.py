# -*- coding: utf-8 -*-
"""
Uses the ps2pdf
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


class epsi_to_png(popentransform):
    implements(ITransform)

    __name__ = "ps_to_epsi"
    inputs = ('image/x-eps',)
    output = 'image/png'

    __version__ = '2015-10-31.01'

    def convert(self, orig, data, **kwargs):
        """
        Convert EPSI to PNG
        """
        context = kwargs.get('context')
        annotate = kwargs.get('annotate')
        s_cmd = api.portal.get_registry_record(
            'epsi_to_png',
            interface=IABCTransformsSettings)
        cmd = eval(s_cmd)
        png = from_to(
            orig,
            cmd,
            inputsuffix=".epsi",
            outputsuffix=".png",
            context=context,
            annotate=annotate,)
        data.setData(png)
        return data


def register():
    return epsi_to_png()
