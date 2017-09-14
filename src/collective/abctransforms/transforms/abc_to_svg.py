# -*- coding: utf-8 -*-
"""
Uses abcm2ps
"""
import logging
from zope.interface import implements
from Products.PortalTransforms.interfaces import ITransform
from Products.PortalTransforms.libtransforms.commandtransform import (
    popentransform)
from collective.abctransforms.utils import from_to

logger = logging.getLogger('collective.abctransforms')


class abc_to_svg(popentransform):
    implements(ITransform)

    __name__ = "abc_to_svg"
    inputs = ('text/vnd.abc',)
    output = 'image/svg+xml'

    __version__ = '2015-10-31.01'

    def convert(self, orig, data, **kwargs):

        # EPS command = ["abcm2ps", "datain", '-E', '-O', "dataout"]
        command = ["abcm2ps", "datain", '-g', '-O', "dataout"]
        ps = from_to(orig,
                     command,
                     outputsuffix='svg',
                     delsrc=False,
                     deldst=False,
                     logging=True)
        data.setData(ps)
        return data


def register():
    return abc_to_svg()


"""
application/postscript
image/x-eps
image/png
application/pdf
"""
