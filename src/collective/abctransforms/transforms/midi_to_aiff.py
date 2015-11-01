# -*- coding: utf-8 -*-
"""
Uses timidity
"""
import logging
import os
import tempfile as tf
import subprocess as sp
from zope.interface import implements
from Products.PortalTransforms.interfaces import ITransform
from Products.PortalTransforms.libtransforms.commandtransform import (
    popentransform)

logger = logging.getLogger('collective.abctransforms')


class midi_to_aiff(popentransform):
    implements(ITransform)

    __name__ = "midi_to_aiff"
    inputs = ('audio/midi',)
    output = 'audio/x-aiff'
    # output_encoding = 'utf-8'

    __version__ = '2015-10-31.01'

    binaryName = "timidity"
    # binaryArgs = "--quiet=9 -A 400 -EFchorus=2,50 -EFreverb=2 -Oa -o- \
    # %(infile)s"
    # binaryArgs = "--quiet=9 -A 400 -EFchorus=2,50 -EFreverb=2 -Oa -o- -"
    useStdin = False

    def convert(self, orig, data, **kwargs):
        mididata = orig
        miditemp = tf.NamedTemporaryFile(mode='w+b',
                                         suffix='.mid', delete=False).name
        fmiditemp = open(miditemp, 'w')
        fmiditemp.write(mididata)
        fmiditemp.close()

        aifftemp = tf.NamedTemporaryFile(mode='w+b',
                                         suffix='.aiff', delete=False).name
        timidity = ["timidity",
                    '-A 400',
                    '-EFchorus=2,50',
                    '-EFreverb=2',
                    miditemp,
                    '-o', aifftemp,
                    '-Oa']

        p = sp.Popen(timidity, stdout=sp.PIPE, stderr=sp.PIPE)
        p.wait()

        faifftemp = open(aifftemp, "rb")
        aiffdata = faifftemp.read()
        faifftemp.close()
        output, errors = p.communicate()
        logger.info(errors)
        logger.info(output)
        os.unlink(aifftemp)
        os.unlink(miditemp)
        data.setData(aiffdata)
        return data


def register():
    return midi_to_aiff()
