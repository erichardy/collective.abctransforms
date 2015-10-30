# -*- coding: utf-8 -*-
"""
Uses the abc2midi
"""
import logging
import os
import tempfile as tf
import subprocess as sp
from StringIO import StringIO
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

    __version__ = '2015-10-29.01'

    binaryName = "abc2midi"
    binaryArgs = "%(infile)s -enc UTF-8 -"
    useStdin = False

    def convert(self, orig, data, **kwargs):
        # context = self.context
        # abc = context.abc
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
        # iomidi = StringIO()
        fmiditemp = open(miditemp, 'rb')
        buffmidi = fmiditemp.read()
        # iomidi.write(buffmidi)
        # iomidi.close()
        """
        title = context.title
        normalizer = getUtility(INormalizer)
        normalizedTitle = normalizer.normalize(title, locale='fr')
        midiFilename = unicode(normalizedTitle + '.mid')
        midiData = iomidi.getvalue()
        midiContentType = u'audio/mid'
        blobMidi = nbf(midiData,
                       contentType=midiContentType,
                       filename=midiFilename
                       )
        context.midi = blobMidi

        output, errors = p.communicate()
        logger.info(errors)
        """
        # logger.info(errors)
        # logger.info(output)
        os.unlink(abctemp)
        os.unlink(miditemp)
        # logger.info(miditemp)
        data.setData(buffmidi)
        return data
        # return iomidi


"""
        command = "%s %s" % (self.binary, self.binaryArgs)
        tmpname = None
        try:
            if not self.useStdin:
                # create tmp
                tmpfile, tmpname = tempfile.mkstemp(text=False)
                # write data to tmp using a file descriptor
                os.write(tmpfile, data)
                # close it so the other process can read it
                os.close(tmpfile)
                # apply tmp name to command
                command = command % {'infile': tmpname}

            cin, couterr = os.popen4(command, 'b')

            if self.useStdin:
                cin.write(data)

            status = cin.close()

            out = self.getData(couterr)
            couterr.close()

            cache.setData(out)
            return cache
        finally:
            if not self.useStdin and tmpname is not None:
                # remove tmp file
                os.unlink(tmpname)
"""


def register():
    return abc_to_midi()
