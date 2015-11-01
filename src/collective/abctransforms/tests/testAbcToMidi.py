# -*- coding: utf-8 -*-

import logging
from Products.CMFCore.utils import getToolByName
from collective.abctransforms.testing import COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING  # noqa
from utils import input_file_path, output_file_path
import unittest

logger = logging.getLogger('collective.abctransforms:tests')


class TestAbcToMidi(unittest.TestCase):

    layer = COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.pt = getToolByName(self.portal, "portal_transforms")
        self.mtr = getToolByName(self.portal, "mimetypes_registry")

    def test_abc_to_midi(self):
        fd = open(input_file_path('DonaldBlue.abc'), "r")
        abc = fd.read()
        mi = open(output_file_path('DonaldBlue1.mid'), "rb")
        midi = mi.read()
        mi.close()
        got = self.pt.convertTo('audio/x-midi',
                                abc,
                                filemane="DonaldBlue")
        got_meta = got.getMetadata()
        print 'metadata returned : ' + str(got_meta)
        self.assertEqual(got.getData(), midi)
        self.assertEqual(got_meta['mimetype'], 'audio/midi')
