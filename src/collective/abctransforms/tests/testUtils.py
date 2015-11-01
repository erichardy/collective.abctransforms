# -*- coding: utf-8 -*-

# tests with the function : from_to

from collective.abctransforms.tests.utils import (input_file_path,
                                                  output_file_path)
from collective.abctransforms.utils import from_to
import unittest


class TestAbcToMidi(unittest.TestCase):

    def setUp(self):
        """Custom shared utility setup for tests."""
        """
        self.portal = self.layer['portal']
        self.pt = getToolByName(self.portal, "portal_transforms")
        self.mtr = getToolByName(self.portal, "mimetypes_registry")
        """

    def test_fromABC_toMIDI(self):
        fd = open(input_file_path('DonaldBlue.abc'), "r")
        abc = fd.read()
        mi = open(output_file_path('DonaldBlue1.mid'), "rb")
        midi = mi.read()
        mi.close()
        command = ["abc2midi", "datain", '-o', "dataout"]
        got = from_to(abc,
                      command,
                      toappend='\n\n',
                      logging=False)
        self.assertEqual(got, midi)

    def test_fromMIDI_toAIFF(self):
        mi = open(output_file_path('DonaldBlue1.mid'), "rb")
        midi = mi.read()
        mi.close()
        Aiff = open(output_file_path('DonaldBlue1.aiff'), "rb")
        aiff = Aiff.read()
        Aiff.close()
        timidity = ["timidity",
                    '-A 400',
                    '-EFchorus=2,50',
                    '-EFreverb=2',
                    "datain",
                    '-o', "dataout",
                    '-Oa']
        got = from_to(midi,
                      timidity,
                      logging=False)
        self.assertEqual(got, aiff)

    def test_fromAIFF_toMP3(self):
        Aiff = open(output_file_path('DonaldBlue1.aiff'), "rb")
        aiff = Aiff.read()
        Aiff.close()
        fdMP3 = open(output_file_path('DonaldBlue1.mp3'), "rb")
        mp3 = fdMP3.read()
        fdMP3.close()
        lame = ["lame",
                '--cbr',
                '-b 32',
                '-f',
                '--quiet',
                "datain",
                "dataout"]
        got = from_to(aiff,
                      lame,
                      logging=False)
        self.assertEqual(got, mp3)
