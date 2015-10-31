# -*- coding: utf-8 -*-

import logging
from zope.interface import implements
from Products.PortalTransforms.interfaces import ITransform
from Products.CMFCore.utils import getToolByName
from plone import api
# from Products.PortalTransforms.interfaces import IChain
# from Products.PortalTransforms.transforms.abc_to_midi import abc_to_midi
# from Products.PortalTransforms.transforms.midi_to_aiff import midi_to_aiff
# from Products.PortalTransforms.transforms.aiff_to_mp3 import aiff_to_mp3
# from Products.PortalTransforms.chain import chain

logger = logging.getLogger('collective.abctransforms')


# class abc_to_mp3(chain):
class abc_to_mp3():
    implements(ITransform)

    __name__ = "abc_to_mp3"
    inputs = ('text/vnd.abc',)
    output = 'audio/mpeg'
    # output_encoding = 'utf-8'

    __version__ = '2015-10-31.01'

    def convert(self, abc, data, **kwargs):
        """
        self.registerTransform(abc_to_midi())
        self.registerTransform(midi_to_aiff())
        self.registerTransform(aiff_to_mp3())
        """
        portal = api.portal.get()
        pt = getToolByName(portal, "portal_transforms")
        midi = pt.convertTo('audio/midi', abc)
        aiff = pt.convertTo('audio/x-aiff', midi.getData())
        mp3 = pt.convertTo('audio/mpeg', aiff.getData())
        data.setData(mp3)
        return data


def register():
    return abc_to_mp3()
