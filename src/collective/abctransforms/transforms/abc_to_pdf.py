# -*- coding: utf-8 -*-

import logging
from zope.interface import implements
from Products.PortalTransforms.interfaces import ITransform
from Products.CMFCore.utils import getToolByName
from plone import api

logger = logging.getLogger('collective.abctransforms')


class abc_to_pdf():
    implements(ITransform)

    __name__ = "abc_to_pdf"
    inputs = ('text/vnd.abc',)
    output = 'application/pdf'

    __version__ = '2015-10-31.01'

    def convert(self, abc, data, **kwargs):
        portal = api.portal.get()
        pt = getToolByName(portal, "portal_transforms")
        ps = pt.convertTo('application/postscript', abc)
        pdf = pt.convertTo('application/pdf', ps.getData())
        data.setData(pdf.getData())
        return data


def register():
    return abc_to_pdf()
