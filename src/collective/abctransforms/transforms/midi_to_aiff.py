# -*- coding: utf-8 -*-
"""
Uses timidity
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


class midi_to_aiff(popentransform):
    implements(ITransform)

    __name__ = "midi_to_aiff"
    inputs = ('audio/midi',)
    output = 'audio/x-aiff'

    __version__ = '2015-10-31.01'

    binaryName = "timidity"
    useStdin = False

    def convert(self, orig, data, **kwargs):
        s_cmd = api.portal.get_registry_record(
            'midi_to_aiff',
            interface=IABCTransformsSettings)
        cmd = eval(s_cmd)
        aiff = from_to(
            orig,
            cmd,
            inputsuffix='.mid',
            outputsuffix='.aiff'
            )
        data.setData(aiff)
        return data
        """
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
        """


def register():
    return midi_to_aiff()
