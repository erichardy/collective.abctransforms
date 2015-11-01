# -*- coding: utf-8 -*-

# from collective.abctransforms.testing import \
#     COLLECTIVE_ABCTRANSFORMS_FUNCTIONAL_TESTING  # noqa
from collective.abctransforms.tests.utils import (input_file_path,
                                                  output_file_path)
from collective.abctransforms.utils import from_to
import unittest


class TestAbcToMidi(unittest.TestCase):

    # layer = COLLECTIVE_ABCTRANSFORMS_FUNCTIONAL_TESTING

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
