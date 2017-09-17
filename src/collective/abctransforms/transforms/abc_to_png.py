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
        epsi = pt.convertTo('image/x-eps', ps.getData())
        png = pt.convertTo('image/png', epsi.getData())
        data.setData(png)
        return data


def register():
    return abc_to_png()
