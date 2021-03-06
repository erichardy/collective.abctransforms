# -*- coding: utf-8 -*-
"""
Uses lame
"""
import logging
from zope.interface import implementer
from Products.PortalTransforms.interfaces import ITransform
from Products.PortalTransforms.libtransforms.commandtransform import (
    popentransform)
from plone import api
from collective.abctransforms.utils import from_to
from collective.abctransforms.interfaces import IABCTransformsSettings

logger = logging.getLogger('collective.abctransforms')


@implementer(ITransform)
class aiff_to_mp3(popentransform):

    __name__ = "aiff_to_mp3"
    inputs = ('audio/x-aiff',)
    output = 'audio/mpeg'
    # output_encoding = 'utf-8'

    __version__ = '2015-10-31.01'

    binaryName = "lame"
    # binaryArgs = "--quiet=9 -A 400 -EFchorus=2,50 -EFreverb=2 -Oa -o- \
    # %(infile)s"
    # binaryArgs = "--quiet=9 -A 400 -EFchorus=2,50 -EFreverb=2 -Oa -o- -"
    useStdin = False

    def convert(self, orig, data, **kwargs):
        """
        Convert AIFF to MP3
        """
        context = kwargs.get('context')
        annotate = kwargs.get('annotate')
        s_cmd = api.portal.get_registry_record(
            'aiff_to_mp3',
            interface=IABCTransformsSettings)
        cmd = eval(s_cmd)
        mp3 = from_to(
            orig,
            cmd,
            context=context,
            annotate=annotate,
            )
        data.setData(mp3)
        return data
        """
        origtemp = tf.NamedTemporaryFile(mode='w+b',
                                         delete=False).name
        forigtemp = open(origtemp, 'wb')
        forigtemp.write(orig)
        forigtemp.close()

        desttemp = tf.NamedTemporaryFile(mode='w+b',
                                         delete=False).name
        lame = ["lame",
                '--cbr',
                '-b 32',
                '-f',
                '--quiet',
                origtemp,
                desttemp]

        p = sp.Popen(lame, stdout=sp.PIPE, stderr=sp.PIPE)
        p.wait()

        fdesttemp = open(desttemp, "rb")
        destdata = fdesttemp.read()
        fdesttemp.close()
        output, errors = p.communicate()
        logger.info(errors)
        logger.info(output)
        os.unlink(origtemp)
        os.unlink(desttemp)
        data.setData(destdata)
        return data
        """


def register():
    return aiff_to_mp3()
