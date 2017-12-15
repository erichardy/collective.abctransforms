# -*- coding: utf-8 -*-
"""
Uses the convert from ImageMagick package
"""
import logging
from Products.CMFCore.utils import getToolByName
from plone import api
from zope.interface import implements
from Products.PortalTransforms.interfaces import ITransform
from Products.PortalTransforms.libtransforms.commandtransform import (
    popentransform)
from collective.abctransforms.interfaces import IABCTransformsSettings
from collective.abctransforms.utils import from_to

logger = logging.getLogger('collective.abctransforms')


class abc_to_png(popentransform):
    implements(ITransform)

    __name__ = "abc_to_png"
    inputs = ('text/vnd.abc',)
    output = 'image/png'

    __version__ = '2015-10-31.01'

    def convert(self, orig, data, **kwargs):
        """
        Convert ABC to PS -> EPSI -> PNG
        """
        context = kwargs.get('context')
        annotate = kwargs.get('annotate')
        abc = orig
        portal = api.portal.get()
        pt = getToolByName(portal, 'portal_transforms')
        ps = pt.convertTo(
            'application/postscript',
            abc,
            context=context,
            annotate=annotate)
        epsi = pt.convertTo(
            'image/x-eps',
            ps.getData(),
            context=context,
            annotate=annotate)
        # the convert from epsi to png does't work
        # png = pt.convertTo('image/png', epsi.getData())
        s_cmd = api.portal.get_registry_record(
            'epsi_to_png',
            interface=IABCTransformsSettings)
        cmd = eval(s_cmd)
        png = from_to(
            epsi.getData(),
            cmd,
            inputsuffix=".epsi",
            outputsuffix='.png',
            context=context,
            annotate=annotate
            )
        data.setData(png)
        return data


def register():
    return abc_to_png()
