# -*- coding: utf-8 -*-
"""
Uses the abc2midi
"""
import logging
import os
import tempfile as tf
import subprocess as sp
# from StringIO import StringIO
# from plone.namedfile.file import NamedBlobFile as nbf
# from zope.component import getUtility
# from plone.i18n.normalizer.interfaces import INormalizer
from zope.interface import implements
from Products.PortalTransforms.interfaces import ITransform
from Products.PortalTransforms.libtransforms.commandtransform import (
    popentransform)

logger = logging.getLogger('collective.abctransforms')


class abc_to_midi(popentransform):
    implements(ITransform)

    __name__ = "abc_to_midi"
    inputs = ('text/vnd.abc',)
    output = 'audio/midi'
    # output_encoding = 'utf-8'

    __version__ = '2015-10-31.01'

    binaryName = "abc2midi"
    binaryArgs = ""
    useStdin = False

    def convert(self, orig, data, **kwargs):
        """"
        Even if a filename arg is passed, it is not copied in
        data metadata !
        Don't use this method directly !

        Instead, use :

        midi = portalTransformTool.convertTo('audio/x-midi',
                                abc,
                                filemane="DonaldBlue")

        and midi.getMetadata(), midi.getData()

        see the test abc_to_midi
        """
        abc = orig
        abctemp = tf.NamedTemporaryFile(mode='w+b',
                                        suffix='.abc',
                                        delete=False).name
        fabctemp = open(abctemp, 'w')
        for l in abc:
            fabctemp.write(l)
        fabctemp.write('\n\n')
        fabctemp.close()
        miditemp = tf.NamedTemporaryFile(mode='w+b',
                                         suffix='.mid',
                                         delete=False).name
        p = sp.Popen(["abc2midi", abctemp, '-o', miditemp],
                     stdout=sp.PIPE,
                     stderr=sp.PIPE
                     )
        p.wait()
        fmiditemp = open(miditemp, 'rb')
        buffmidi = fmiditemp.read()
        os.unlink(abctemp)
        os.unlink(miditemp)
        data.setData(buffmidi)
        return data


def register():
    return abc_to_midi()
