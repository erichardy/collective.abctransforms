from Products.CMFCore.utils import getToolByName
from plone import api

from collective.abctransforms.testing import COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING  # noqa

import unittest


class TestMimetype(unittest.TestCase):

    layer = COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING

    def test_abc_present(self):
        portal = api.portal.get()
        mtr = getToolByName(portal, 'mimetypes_registry')
        mimetypes = mtr.lookup('text/vnd.abc')
        self.assertEqual(len(mimetypes), 1)
