# -*- coding: utf-8 -*-

import logging
from Products.CMFCore.utils import getToolByName
# from plone import api
# from StringIO import StringIO

from collective.abctransforms.testing import COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING  # noqa
# from collective.abctransforms.transforms.abc_to_midi import abc_to_midi
from utils import input_file_path, output_file_path
import unittest

logger = logging.getLogger('collective.abctransforms:tests')


class TestMidiToAiff(unittest.TestCase):

    layer = COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.pt = getToolByName(self.portal, "portal_transforms")
        self.mtr = getToolByName(self.portal, "mimetypes_registry")

    def test_midi_to_aiff(self):
        fd = open(output_file_path('DonaldBlue1.mid'), "rb")
        mid = fd.read()
        Aiff = open(output_file_path('DonaldBlue1.aiff'), "rb")
        aiff = Aiff.read()
        Aiff.close()
        got = self.pt.convertTo('audio/x-aiff',
                                mid,
                                filemane="DonaldBlue")
        got_meta = got.getMetadata()
        print 'metadata returned : ' + str(got_meta)
        self.assertEqual(got.getData(), aiff)
        self.assertEqual(got_meta['mimetype'], 'audio/x-aiff')
        """
        fgot = open(output_file_path('got.aiff'), "wb")
        fgot.write(got.getData())
        fgot.close()
        """