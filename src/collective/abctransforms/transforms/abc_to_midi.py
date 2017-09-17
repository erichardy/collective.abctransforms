# -*- coding: utf-8 -*-
"""
Uses the abc2midi
"""
import logging
import os
import tempfile as tf
import subprocess as sp
from zope.interface import implements
from Products.PortalTransforms.interfaces import ITransform
from Products.PortalTransforms.libtransforms.commandtransform import (
    popentransform)
from plone import api
from collective.abctransforms.utils import from_to
from collective.abctransforms.interfaces import IABCTransformsSettings

logger = logging.getLogger('collective.abctransforms')


class abc_to_midi(popentransform):
    implements(ITransform)

    __name__ = "abc_to_midi"
    inputs = ('text/vnd.abc',)
    output = 'audio/midi'

    __version__ = '2015-10-31.01'

    binaryName = "abc2midi"
    binaryArgs = ""
    useStdin = False

    def convert(self, orig, data, **kwargs):
        """"
        Don't use this method directly !
        Instead, use :
        midi = portalTransformTool.convertTo('audio/x-midi',
                                             abc)
        and midi.getMetadata(), midi.getData()
        see the test abc_to_midi
        """
        s_cmd = api.portal.get_registry_record(
            'abc_to_midi',
            interface=IABCTransformsSettings)
        cmd = eval(s_cmd)
        midi = from_to(
            orig,
            cmd,
            outputsuffix='.mid'
            )
        data.setData(midi)
        return data
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
        """


def register():
    return abc_to_midi()
