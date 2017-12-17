# -*- coding: utf-8 -*-

import logging
from Products.CMFCore.utils import getToolByName
from collective.abctransforms.testing import COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING  # noqa
from utils import input_file_path, createScoreFiles, deleteScoreFiles
from utils import createFile, fileType
from utils import registryRecords
from plone import api
from collective.abctransforms.interfaces import IABCTransformsSettings
from os import system
import subprocess as sp
import unittest

logger = logging.getLogger('collective.abctransforms:tests')


class TestSCORES(unittest.TestCase):

    layer = COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.pt = getToolByName(self.portal, "portal_transforms")
        self.mtr = getToolByName(self.portal, "mimetypes_registry")
        # creation des fichiers son
        createScoreFiles()
        system('ls -l ' + input_file_path('.'))

    def tearDown(self):
        # suppression des fichiers son
        deleteScoreFiles()
        system('ls -l ' + input_file_path('.'))

    def test_abc_to_ps(self):
        """
        Generated PS file contains informations specific to the
        input file, date, etc... it is not possible to compare...
        So we verify that the output is not empty and the content
        is postcript
        """
        f = open(input_file_path('DonaldBlue.abc'), 'r')
        datain = f.read()
        f.close()
        f = open(input_file_path('DonaldBlue.ps'), 'r')
        f.close()
        convertedData = self.pt.convertTo(
            'application/postscript',
            datain,
            )
        #
        self.assertGreater(convertedData.getData(), 0)
        #
        psps = createFile(convertedData.getData(), 'ps.ps')
        out_type = fileType(psps)
        ps_type = fileType('DonaldBlue.ps')
        #
        self.assertEqual(ps_type, out_type)

    def test_ps_to_epsi(self):
        f = open(input_file_path('DonaldBlue.ps'), 'r')
        datain = f.read()
        f.close()
        convertedData = self.pt.convertTo(
            'image/x-eps',
            datain,
            )
        #
        self.assertGreater(convertedData.getData(), 0)
        #
        epsiepsi = createFile(convertedData.getData(), 'epsi.epsi')
        out_type = fileType(epsiepsi)
        epsi_type = fileType('DonaldBlue.epsi')
        #
        self.assertEqual(epsi_type, out_type)

    """
    def test_epsi_to_png(self):
        f = open(input_file_path('DonaldBlue.epsi'), 'r')
        datain = f.read()
        f.close()
        convertedData = self.pt.convertTo(
            'image/png',
            datain,
            )
        #
        self.assertGreater(convertedData.getData(), 0)
        #
        epsiepsi = createFile(convertedData.getData(), 'png.png')
        out_type = fileType(epsiepsi)
        png_type = fileType('DonaldBlue.png')
        #
        self.assertEqual(png_type, out_type)
    """

    def test_ps_to_pdf(self):
        f = open(input_file_path('DonaldBlue.ps'), 'r')
        datain = f.read()
        f.close()
        convertedData = self.pt.convertTo(
            'application/pdf',
            datain,
            )
        #
        self.assertGreater(convertedData.getData(), 0)
        #
        pdfpdf = createFile(convertedData.getData(), 'pdf.pdf')
        out_type = fileType(pdfpdf)
        pdf_type = fileType('DonaldBlue.pdf')
        #
        self.assertEqual(pdf_type, out_type)

