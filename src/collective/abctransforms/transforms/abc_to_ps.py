# -*- coding: utf-8 -*-
"""
Uses abcm2ps
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


class abc_to_ps(popentransform):
    implements(ITransform)

    __name__ = "abc_to_ps"
    inputs = ('text/vnd.abc',)
    output = 'application/postscript'

    __version__ = '2015-10-31.01'

    def convert(self, orig, data, **kwargs):
        """
        Convert ABC to PS
        """
        context = kwargs.get('context')
        annotate = kwargs.get('annotate')
        s_cmd = api.portal.get_registry_record(
            'abc_to_ps',
            interface=IABCTransformsSettings)
        cmd = eval(s_cmd)
        # EPS command = ["abcm2ps", "datain", '-E', '-O', "dataout"]
        ps = from_to(
            orig,
            cmd,
            context=context,
            annotate=annotate
            )
        data.setData(ps)
        return data


def register():
    return abc_to_ps()


"""
application/postscript
image/x-eps
image/png
application/pdf
"""
