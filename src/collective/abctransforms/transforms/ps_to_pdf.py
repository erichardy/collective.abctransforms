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


class ps_to_pdf(popentransform):
    implements(ITransform)

    __name__ = "ps_to_pdf"
    inputs = ('application/postscript',)
    output = 'application/pdf'

    __version__ = '2015-10-31.01'

    def convert(self, orig, data, **kwargs):
        context = kwargs.get('context')
        annotate = kwargs.get('annotate')
        s_cmd = api.portal.get_registry_record(
            'ps_to_pdf',
            interface=IABCTransformsSettings)
        cmd = eval(s_cmd)
        pdf = from_to(
            orig,
            cmd,
            context=context,
            annotate=annotate,
            )
        data.setData(pdf)
        return data


def register():
    return ps_to_pdf()
