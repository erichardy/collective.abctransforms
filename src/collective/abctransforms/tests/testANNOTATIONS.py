# -*- coding: utf-8 -*-

import logging
from Products.CMFCore.utils import getToolByName
from zope.annotation.interfaces import IAnnotations
from collective.abctransforms.testing import COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING  # noqa
from utils import input_file_path, createScoreFiles, deleteScoreFiles
from utils import createFile, fileType
from utils import registryRecords
from plone import api
from collective.abctransforms.interfaces import IABCTransformsSettings
from os import system
import subprocess as sp
import unittest
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID

logger = logging.getLogger('collective.abctransforms:tests')


class TestANNOTATIONS(unittest.TestCase):

    layer = COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.pt = getToolByName(self.portal, "portal_transforms")
        self.mtr = getToolByName(self.portal, "mimetypes_registry")
        portal = api.portal.get()
        setRoles(portal, TEST_USER_ID, ['Manager'])
        self.doc = api.content.create(
            type='Document',
            title='My Content',
            container=portal)

    def tearDown(self):
        pass

    def test_annotations(self):
        f = open(input_file_path('DonaldBlue.abc'), 'r')
        datain = f.read()
        f.close()
        annot = IAnnotations(self.doc)
        if annot.get('abc2midi_OUTPUT'):
            annot['abc2midi_OUTPUT'] = ''
        if annot.get('abc2midi_ERRORS'):
            annot['abc2midi_ERRORS'] = ''
        convertedData = self.pt.convertTo(
            'audio/x-midi',
            datain,
            context=self.doc,
            annotate=True
            )
        print annot.get('abc2midi_OUTPUT')
        annot.get('abc2midi_ERRORS')
        self.assertGreater(annot.get('abc2midi_OUTPUT'), 0)
        self.assertGreater(annot.get('abc2midi_ERRORS'), 0)
