# -*- coding: utf-8 -*-

import logging
from Products.CMFCore.utils import getToolByName
from collective.abctransforms.testing import COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING  # noqa
from utils import registryRecords
from plone import api
from collective.abctransforms.interfaces import IABCTransformsSettings
import unittest

logger = logging.getLogger('collective.abctransforms:tests')


class TestRegistryRecords(unittest.TestCase):

    layer = COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.pt = getToolByName(self.portal, "portal_transforms")
        self.mtr = getToolByName(self.portal, "mimetypes_registry")

    def test_getRegistryRecords(self):
        for k in registryRecords.keys():
            rec = api.portal.get_registry_record(
                k,
                interface=IABCTransformsSettings)
            self.assertEqual(registryRecords[k], rec)
