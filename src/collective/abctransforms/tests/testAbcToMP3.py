# -*- coding: utf-8 -*-

import logging
from Products.CMFCore.utils import getToolByName

from collective.abctransforms.testing import COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING  # noqa
from utils import input_file_path, output_file_path
import unittest

logger = logging.getLogger('collective.abctransforms:tests')


class TestAbcToMP3(unittest.TestCase):

    layer = COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.pt = getToolByName(self.portal, "portal_transforms")
        self.mtr = getToolByName(self.portal, "mimetypes_registry")

    def test_abc_to_mp3(self):
        fd = open(input_file_path('DonaldBlue.abc'), "r")
        abc = fd.read()
        # print self.mtr.classify(abc)
        fdmp3 = open(output_file_path('DonaldBlue1.mp3'), "rb")
        mp3 = fdmp3.read()
        fdmp3.close()
        got = self.pt.convertTo('audio/mpeg',
                                abc)
        got_meta = got.getMetadata()
        print 'metadata returned : ' + str(got_meta)
        self.assertEqual(mp3, got.getData())
        self.assertEqual(got_meta['mimetype'], 'audio/mpeg')
        """
        fgot = open(output_file_path('got.mp3'), "wb")
        fgot.write(got.getData())
        fgot.close()
        """
