# -*- coding: utf-8 -*-

from Products.CMFCore.utils import getToolByName
from plone import api
from utils import input_file_path
from collective.abctransforms.testing import COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING  # noqa

import unittest


class TestMimetype(unittest.TestCase):

    layer = COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.mtr = getToolByName(self.portal, "mimetypes_registry")

    def test_abc_present(self):
        portal = api.portal.get()
        mtr = getToolByName(portal, 'mimetypes_registry')
        mimetypes = mtr.lookup('text/vnd.abc')
        self.assertEqual(len(mimetypes), 1)

    def test_mimetype_abc(self):
        fd = open(input_file_path('DonaldBlue.abc'), "r")
        abc = fd.read()
        self.assertEqual(self.mtr.classify(abc), 'text/vnd.abc')
