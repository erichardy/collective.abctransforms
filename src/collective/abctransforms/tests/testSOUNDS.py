# -*- coding: utf-8 -*-

import logging
from Products.CMFCore.utils import getToolByName
from collective.abctransforms.testing import COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING  # noqa
from utils import input_file_path, createSoundFiles, deleteSoundFiles
from utils import registryRecords
from plone import api
from collective.abctransforms.interfaces import IABCTransformsSettings
from os import system
import subprocess as sp
import unittest

logger = logging.getLogger('collective.abctransforms:tests')


class TestSOUNDS(unittest.TestCase):

    layer = COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.pt = getToolByName(self.portal, "portal_transforms")
        self.mtr = getToolByName(self.portal, "mimetypes_registry")
        # creation des fichiers son
        createSoundFiles()
        system('ls -l ' + input_file_path('.'))

    def tearDown(self):
        # suppression des fichiers son
        deleteSoundFiles()
        system('ls -l ' + input_file_path('.'))

    def test_abc_to_midi(self):
        f = open(input_file_path('DonaldBlue.abc'), 'r')
        datain = f.read()
        f.close()
        f = open(input_file_path('DonaldBlue.mid'), 'r')
        dataout = f.read()
        f.close()
        convertedData = self.pt.convertTo(
            'audio/x-midi',
            datain,
            )
        self.assertEqual(dataout, convertedData.getData())

    def test_abc_to_mp3(self):
        f = open(input_file_path('DonaldBlue.abc'), 'r')
        datain = f.read()
        f.close()
        f = open(input_file_path('DonaldBlue.mp3'), 'r')
        dataout = f.read()
        f.close()
        convertedData = self.pt.convertTo(
            'audio/mpeg',
            datain,
            )
        self.assertEqual(
            convertedData.getMetadata()['mimetype'],
            'audio/mpeg')

    def test_abc_to_ogg(self):
        f = open(input_file_path('DonaldBlue.abc'), 'r')
        datain = f.read()
        f.close()
        f = open(input_file_path('DonaldBlue.mp3'), 'r')
        dataout = f.read()
        f.close()
        convertedData = self.pt.convertTo(
            'audio/ogg',
            datain,
            )
        self.assertEqual(
            convertedData.getMetadata()['mimetype'],
            'audio/ogg')

    def test_midi_to_aiff(self):
        # because it seems not possible to compare the two files,
        # we compare theire size and theire type
        f = open(input_file_path('DonaldBlue.mid'), 'r')
        datain = f.read()
        f.close()
        f = open(input_file_path('DonaldBlue.aiff'), 'r')
        dataout = f.read()
        f.close()
        convertedData = self.pt.convertTo(
            'audio/x-aiff',
            datain,
            )
        self.assertEqual(len(dataout), len(convertedData.getData()))
        fout = open(input_file_path('aiff.aiff'), 'w')
        fout.write(convertedData.getData())
        fout.close()
        cmd = ['file', input_file_path('aiff.aiff')]
        p = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
        p.wait()
        c_output, c_errors = p.communicate()
        cmd = ['file', input_file_path('DonaldBlue.aiff')]
        p = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
        p.wait()
        o_output, o_errors = p.communicate()
        self.assertEqual(c_output.split(':')[1], o_output.split(':')[1])

    def test_aiff_to_mp3(self):
        f = open(input_file_path('DonaldBlue.aiff'))
        datain = f.read()
        f.close()
        f = open(input_file_path('DonaldBlue.mp3'))
        dataout = f.read()
        f.close()
        convertedData = self.pt.convertTo(
            'audio/mpeg',
            datain,
            )
        self.assertEqual(dataout, convertedData.getData())

    def test_midi_to_ogg(self):
        """
        because it seems not possible to compare the two files,
        we compare only the types
        NB: in normal use, the OGG files created don't have the same size
        even with the ame input file and same command !!!
        """
        f = open(input_file_path('DonaldBlue.mid'), 'r')
        datain = f.read()
        f.close()
        convertedData = self.pt.convertTo(
            'audio/ogg',
            datain,
            )
        fout = open(input_file_path('ogg.ogg'), 'w')
        fout.write(convertedData.getData())
        fout.close()
        cmd = ['file', input_file_path('ogg.ogg')]
        p = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
        p.wait()
        c_output, c_errors = p.communicate()
        cmd = ['file', input_file_path('DonaldBlue.ogg')]
        p = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
        p.wait()
        o_output, o_errors = p.communicate()
        self.assertEqual(
            c_output.split(':')[1].strip(),
            o_output.split(':')[1].strip())
