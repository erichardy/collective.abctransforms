# -*- coding: utf-8 -*-

import logging
from Products.CMFCore.utils import getToolByName
from collective.abctransforms.testing import COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING  # noqa
from utils import input_file_path, createScoreFiles, deleteScoreFiles
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
        # deleteScoreFiles()
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
        fout = open(input_file_path('ps.ps'), 'w')
        fout.write(convertedData.getData())
        fout.close()
        cmd = ['file', input_file_path('ps.ps')]
        p = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
        p.wait()
        c_output, c_errors = p.communicate()
        cmd = ['file', input_file_path('DonaldBlue.ps')]
        p = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
        p.wait()
        o_output, o_errors = p.communicate()
        #
        self.assertEqual(c_output.split(':')[1], o_output.split(':')[1])

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
        fout = open(input_file_path('epsi.epsi'), 'w')
        fout.write(convertedData.getData())
        fout.close()
        cmd = ['file', input_file_path('epsi.epsi')]
        p = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
        p.wait()
        c_output, c_errors = p.communicate()
        cmd = ['file', input_file_path('DonaldBlue.epsi')]
        p = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
        p.wait()
        o_output, o_errors = p.communicate()
        #
        self.assertEqual(c_output.split(':')[1], o_output.split(':')[1])

    """
    def test_epsi_to_png(self):
        f = open(input_file_path('DonaldBlue.epsi'), 'r')
        datain = f.read()
        f.close()
        f = open(input_file_path('DonaldBlue.png'), 'r')
        dataout = f.read()
        f.close()
        convertedData = self.pt.convertTo(
            'image/png',
            datain,
            )
        #
        self.assertEqual(dataout, convertedData.getData())
        #
        fout = open(input_file_path('png.png'), 'w')
        fout.write(convertedData.getData())
        fout.close()
        cmd = ['file', input_file_path('png.png')]
        p = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
        p.wait()
        c_output, c_errors = p.communicate()
        cmd = ['file', input_file_path('DonaldBlue.png')]
        p = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
        p.wait()
        o_output, o_errors = p.communicate()
        #
        self.assertEqual(c_output.split(':')[1], o_output.split(':')[1])
    """

    def test_ps_to_pdf(self):
        f = open(input_file_path('DonaldBlue.ps'), 'r')
        datain = f.read()
        f.close()
        f = open(input_file_path('DonaldBlue.pdf'), 'r')
        dataout = f.read()
        f.close()
        convertedData = self.pt.convertTo(
            'application/pdf',
            datain,
            )
        #
        self.assertEqual(dataout, convertedData.getData())
        #

