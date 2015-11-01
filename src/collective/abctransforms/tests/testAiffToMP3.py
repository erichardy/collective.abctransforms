# -*- coding: utf-8 -*-

import logging
from Products.CMFCore.utils import getToolByName
from collective.abctransforms.testing import COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING  # noqa
from utils import output_file_path
import unittest

logger = logging.getLogger('collective.abctransforms:tests')


class TestMidiToAiff(unittest.TestCase):

    layer = COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.pt = getToolByName(self.portal, "portal_transforms")
        self.mtr = getToolByName(self.portal, "mimetypes_registry")

    def test_aiff_to_mp3(self):
        fdAiff = open(output_file_path('DonaldBlue1.aiff'), "rb")
        aiff = fdAiff.read()
        fdMP3 = open(output_file_path('DonaldBlue1.mp3'), "rb")
        mp3 = fdMP3.read()
        fdMP3.close()
        got = self.pt.convertTo('audio/mpeg',
                                aiff)
        got_meta = got.getMetadata()
        print 'metadata returned : ' + str(got_meta)
        self.assertEqual(got.getData(), mp3)
        self.assertEqual(got_meta['mimetype'], 'audio/mpeg')
        """
        fgot = open(output_file_path('got.mp3'), "wb")
        fgot.write(got.getData())
        fgot.close()
        """
