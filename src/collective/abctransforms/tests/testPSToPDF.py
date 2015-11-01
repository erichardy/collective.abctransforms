# -*- coding: utf-8 -*-

import logging
from Products.CMFCore.utils import getToolByName
from collective.abctransforms.testing import COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING  # noqa
from utils import input_file_path, output_file_path
import unittest

logger = logging.getLogger('collective.abctransforms:tests')


class TestPStoPDF(unittest.TestCase):

    layer = COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.pt = getToolByName(self.portal, "portal_transforms")
        self.mtr = getToolByName(self.portal, "mimetypes_registry")

    def test_ps_to_pdf(self):
        """
        .. note: Because creation date, command line, filenames, etc...
            are part of postscript file, it isn't possible to compare
            files !!! ;-(
        """
        fdps = open(output_file_path('DonaldBlue.ps'), "rb")
        ps = fdps.read()
        fdps.close()

        got = self.pt.convertTo('application/pdf',
                                ps)
        got_meta = got.getMetadata()
        print 'metadata returned : ' + str(got_meta)
        # self.assertEqual(ps, got.getData())
        self.assertEqual(got_meta['mimetype'], 'application/pdf')
