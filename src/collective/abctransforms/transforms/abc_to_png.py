# -*- coding: utf-8 -*-
"""
Uses the convert from ImageMagick package
"""
import logging
from Products.CMFCore.utils import getToolByName
from plone import api
from zope.interface import implementer
from Products.PortalTransforms.interfaces import ITransform
from collective.abctransforms.interfaces import IABCTransformsSettings
from collective.abctransforms.utils import from_to
from Products.PortalTransforms.libtransforms.commandtransform import (
    popentransform)
# from collective.abctransforms.interfaces import IABCTransformsSettings
# from collective.abctransforms.utils import from_to

logger = logging.getLogger('collective.abctransforms')


@implementer(ITransform)
class abc_to_png(popentransform):

    __name__ = "abc_to_png"
    inputs = ('text/vnd.abc',)
    output = 'image/png'

    __version__ = '2015-10-31.01'

    def convert(self, orig, data, **kwargs):
        """
        Convert ABC to PS -> EPSI -> PNG

        actualy, doesn't work because of the yet available
        transform image/* to image/png which seems not working with EPS
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
            annotate=annotate
            )
        epsi = pt.convertTo(
            'image/x-eps',
            ps.getData(),
            context=context,
            annotate=annotate
            )
        s_cmd = api.portal.get_registry_record(
            'epsi_to_png',
            interface=IABCTransformsSettings
            )
        cmd = eval(s_cmd)
        png = from_to(
             epsi.getData(),
             cmd,
             inputsuffix=".epsi",
             outputsuffix='.png',
             context=context,
             annotate=annotate
             )

        """
        We call the yet available transform image/* to image/png
        but seems not working with epsi !
        png = pt.convertTo(
            target_mimetype='image/png',
            orig=epsi.getData(),
            context=context,
            annotate=annotate)
        """
        data.setData(png)
        return data


def register():
    return abc_to_png()
