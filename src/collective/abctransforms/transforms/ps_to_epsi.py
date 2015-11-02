# -*- coding: utf-8 -*-
"""
Uses the abc2midi
"""
import logging
from zope.interface import implements
from Products.PortalTransforms.interfaces import ITransform
from Products.PortalTransforms.libtransforms.commandtransform import (
    popentransform)
from collective.abctransforms.utils import from_to

logger = logging.getLogger('collective.abctransforms')


class ps_to_epsi(popentransform):
    implements(ITransform)

    __name__ = "ps_to_epsi"
    inputs = ('application/postscript',)
    output = 'image/x-eps'

    __version__ = '2015-10-31.01'

    def convert(self, orig, data, **kwargs):
        """
        origtemp = tf.NamedTemporaryFile(mode='w+b',
                                         delete=False).name
        forigtemp = open(origtemp, 'wb')
        forigtemp.write(orig)
        forigtemp.close()

        desttemp = tf.NamedTemporaryFile(mode='w+b',
                                         delete=False).name
        """
        ps2epsi = ["ps2epsi", "datain", "dataout"]
        pdf = from_to(orig, ps2epsi, logging=False)
        """
        p = sp.Popen(ps2pdf, stdout=sp.PIPE, stderr=sp.PIPE)
        p.wait()

        fdesttemp = open(desttemp, "rb")
        destdata = fdesttemp.read()
        fdesttemp.close()
        output, errors = p.communicate()
        logger.info(errors)
        logger.info(output)
        print origtemp
        print desttemp
        # os.unlink(origtemp)
        # os.unlink(desttemp)
        """
        data.setData(pdf)
        return data


def register():
    return ps_to_epsi()
