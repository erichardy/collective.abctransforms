# -*- coding: utf-8 -*-

import logging
from zope.publisher.browser import BrowserView
from Products.CMFCore.utils import getToolByName
from plone import api
# from pdb import set_trace

logger = logging.getLogger('collective.abctransforms')

abc = """
X:1
%%MIDI chordvol 30
%%MIDI bassvol 30
P: A
Q:190
T: Donald Blue
M: 4/4
L: 1/8
R: reel
K: Dmaj
P: A
|:"D"dBAF A2 FA|dBAF"A"EFDA|"D"dBAF A2 FA|1"Bm"B2 BA B2 AB:|2"Bm"B2 BA B2 d2|
|:"D"ABde faaa|"G"g2fd"Em"edBd|"D"ABde fafd |1"Bm"B2BA B2 dB:|2"Bm"B2 BA B2 AB|

"""


class xxx(BrowserView):
    def __call__(self):
        portal = api.portal.get()
        pt = getToolByName(portal, "portal_transforms")
        midi = pt.convertTo(target_mimetype='audio/midi', orig=abc)
        logger.info(midi.getMetadata())
