# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.abctransforms.testing import COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING  # noqa
from Products.CMFCore.utils import getToolByName
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.abctransforms is properly installed."""

    layer = COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.abctransforms is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'collective.abctransforms'))

    def test_browserlayer(self):
        """Test that ICollectiveAbctransformsLayer is registered."""
        from collective.abctransforms.interfaces import (
            ICollectiveAbctransformsLayer)
        from plone.browserlayer import utils
        self.assertIn(ICollectiveAbctransformsLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['collective.abctransforms'])

    def test_product_uninstalled(self):
        """Test if collective.abctransforms is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'collective.abctransforms'))

    def test_browserlayer_removed(self):
        """Test that ICollectiveAbctransformsLayer is removed."""
        from collective.abctransforms.interfaces import ICollectiveAbctransformsLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICollectiveAbctransformsLayer, utils.registered_layers())

    def test_abc_removed(self):
        portal = api.portal.get()
        mtr = getToolByName(portal, 'mimetypes_registry')
        mimetypes = mtr.lookup('text/vnd.abc')
        self.assertEqual(len(mimetypes), 0)
