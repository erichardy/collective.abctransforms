# -*- coding: utf-8 -*-

import logging
from Products.CMFCore.utils import getToolByName
from collective.abctransforms.testing import COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING  # noqa
from utils import input_file_path, output_file_path
import unittest

logger = logging.getLogger('collective.abctransforms:tests')


class TestAbcToPS(unittest.TestCase):

    layer = COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.pt = getToolByName(self.portal, "portal_transforms")
        self.mtr = getToolByName(self.portal, "mimetypes_registry")

    def test_abc_to_ps(self):
        """
        .. note: Because creation date, command line, filenames, etc...
            are part of postscript file, it isn't possible to compare
            files !!! ;-(
        """
        fd = open(input_file_path('DonaldBlue.abc'), "r")
        abc = fd.read()
        fd.close()
        """
        fdps = open(output_file_path('DonaldBlue.ps'), "rb")
        ps = fdps.read()
        fdps.close()
        """
        got = self.pt.convertTo('application/postscript',
                                abc)
        got_meta = got.getMetadata()
        print 'metadata returned : ' + str(got_meta)
        # self.assertEqual(got.getData(), ps)
        self.assertEqual(got_meta['mimetype'], 'application/postscript')

    def test_abc_to_pdf(self):
        fd = open(input_file_path('DonaldBlue.abc'), "r")
        abc = fd.read()
        fd.close()
        got = self.pt.convertTo('application/pdf',
                                abc)
        got_meta = got.getMetadata()
        print 'metadata returned : ' + str(got_meta)
        # self.assertEqual(got.getData(), ps)
        self.assertEqual(got_meta['mimetype'], 'application/pdf')
