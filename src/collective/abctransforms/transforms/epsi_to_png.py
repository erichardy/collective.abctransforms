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


class epsi_to_png(popentransform):
    implements(ITransform)

    __name__ = "epsi_to_png"
    inputs = ('image/x-eps',)
    output = 'image/png'

    __version__ = '2015-10-31.01'

    def convert(self, orig, data, **kwargs):
        epsitemp = tf.NamedTemporaryFile(mode='w+b',
                                    suffix='.epsi', delete=False).name
        fepsitemp = open(epsitemp, "wb")
        fepsitemp.write(orig)
        
        pngtemp = tf.NamedTemporaryFile(mode='w+b',
                                    suffix='.png', delete=False).name
        p = sp.Popen(["convert",
                      epsitemp,
                      '-filter',
                      'Catrom',
                      '-resize',
                      '600',
                      pngtemp], stdout=sp.PIPE, stderr=sp.PIPE)
        p.wait()
        iopng = StringIO()
        fpngtemp = open(pngtemp, 'r')
        buff_score = fpngtemp.read()
        fpngtemp.close()
        data.setData(buff_score)
        return data
"""
        convert = ["convert",
                   "-filter Catrom",
                   "-resize 600",
                   "datain",
                   "dataout"]
        print convert
        png = from_to(orig,
                      convert,
                      toappend=None,
                      logging=False,
                      inputsuffix=".epsi",
                      outputsuffix=".png")
        data.setData(png)
        return data
"""

def register():
    return epsi_to_png()
