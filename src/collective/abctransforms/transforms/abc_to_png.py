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
from collective.abctransforms.utils import from_to

logger = logging.getLogger('collective.abctransforms')


class abc_to_png(popentransform):
    implements(ITransform)

    __name__ = "abc_to_png"
    inputs = ('text/vnd.abc',)
    output = 'image/png'

    __version__ = '2015-10-31.01'

    def convert(self, orig, data, **kwargs):
        abc = orig
        portal = api.portal.get()
        pt = getToolByName(portal, 'portal_transforms')
        ps = pt.convertTo('application/postscript', abc)
        ps2epsi = ["ps2epsi", "datain", "dataout"]
        epsi = from_to(ps.getData(), ps2epsi, logging=False)
        # png = pt.convertTo('image/png', epsi)
        convert = ["convert",
                   "-filter",
                   "Catrom",
                   "-resize",
                   "600",
                   "datain",
                   "dataout"]
        png = from_to(epsi,
                      convert,
                      toappend=None,
                      logging=False,
                      inputsuffix=".epsi",
                      outputsuffix=".png")

        data.setData(png)
        return data


def register():
    return abc_to_png()
