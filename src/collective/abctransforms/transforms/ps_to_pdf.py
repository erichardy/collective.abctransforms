# -*- coding: utf-8 -*-
"""
Uses the ps2pdf
"""
import logging
from zope.interface import implements
from Products.PortalTransforms.interfaces import ITransform
from Products.PortalTransforms.libtransforms.commandtransform import (
    popentransform)
from collective.abctransforms.utils import from_to

logger = logging.getLogger('collective.abctransforms')


class ps_to_pdf(popentransform):
    implements(ITransform)

    __name__ = "ps_to_pdf"
    inputs = ('application/postscript',)
    output = 'application/pdf'

    __version__ = '2015-10-31.01'

    def convert(self, orig, data, **kwargs):
        ps2pdf = ["ps2pdf", "datain", "dataout"]
        pdf = from_to(orig, ps2pdf, logging=False)
        data.setData(pdf)
        return data


def register():
    return ps_to_pdf()
