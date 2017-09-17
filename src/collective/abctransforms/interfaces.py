# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.supermodel import model
from zope.schema import TextLine
from zope.schema import Bool
from collective.abctransforms import _


class ICollectiveAbctransformsLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


MidiToAiff = u'["timidity", "-A 400", "-EFchorus=2,50", '
MidiToAiff += u'"-EFreverb=2", "datain", "-o", "dataout", "-Oa"]'
MidiToOgg = u'["timidity", "-A 400", "-EFchorus=2,50", '
MidiToOgg += u'"-EFreverb=2", "datain", "-o", "dataout", "-Ov"]'
Lame = u'["lame","--cbr", "-b 32","-f","--quiet","datain", "dataout"]'
Ps2Epsi = u'["ps2epsi", "datain", "dataout"]'
EpsiToPng = u'["convert", "-filter", "Catrom", "-resize", "600", '
EpsiToPng += u'"datain", "dataout"]'


class IABCTransformsSettings(model.Schema):
    '''
    XXX
    Should develop a validation : each command must be a python list
    and must contain "datain" and "dataout"
    and check if first term of the list is a valid command
    '''
    model.fieldset('command_lines',
                   label=_(u'command lines'),
                   fields=['abc_to_midi',
                           'midi_to_aiff',
                           'aiff_to_mp3',
                           'midi_to_ogg',
                           'abc_to_ps',
                           'ps_to_pdf',
                           'ps_to_epsi',
                           'epsi_to_png',
                           'abc_to_svg'
                           ])
    abc_to_midi = TextLine(
        title=_(u'abc To midi command'),
        description=_(u'python list of strings, with "datain" and "dataout"'),
        default=u'["abc2midi", "datain", "-o", "dataout"]',
        required=True
        )

    midi_to_aiff = TextLine(
        title=_(u'midi to AIFF command'),
        description=_(u'used for abc to mp3'),
        default=MidiToAiff,
        required=True,
        )
    aiff_to_mp3 = TextLine(
        title=_(u'AIFF to mp3 command'),
        description=_(u'used for abc to mp3'),
        default=Lame,
        required=True,
        )
    midi_to_ogg = TextLine(
        title=_(u'MIDI to OGG command'),
        description=_(u'used for ABC to OGG'),
        default=MidiToOgg,
        required=True,
        )
    abc_to_ps = TextLine(
        title=_(u'ABC to PS command'),
        description=_(u'used for ABC to PDF/PNG'),
        default=u'["abcm2ps", "datain", "-O", "dataout"]',
        required=True,
        )
    ps_to_epsi = TextLine(
        title=_(u'PS to EPSI command'),
        description=_(u'used for abc to png'),
        default=Ps2Epsi,
        required=True,
        )
    epsi_to_png = TextLine(
        title=_(u'EPSI to PNG command'),
        description=_(u'used for abc to png'),
        default=EpsiToPng,
        required=True,
        )
    ps_to_pdf = TextLine(
        title=_(u'PS to PDF command'),
        description=_(u'used for ABC to PDF'),
        default=u'["ps2pdf", "datain", "dataout"]',
        required=True,
        )
    abc_to_svg = TextLine(
        title=_(u'ABC to SVG command'),
        description=_(u'used for ABC to SVG'),
        default=u'["abcm2ps", "datain", "-g", "-O", "dataout"]',
        required=True,
        )

    model.fieldset('debug',
                   label=_(u'debug options'),
                   fields=['debug_mode',
                           'show_command',
                           'keep_src',
                           'keep_dst',
                           ])
    debug_mode = Bool(
        title=_(u'debug mode ?'),
        description=_(u'uncheck for normal use'),
        default=True)
    show_command = Bool(
        title=_(u'show command line in logs ?'),
        description=_(u'uncheck for normal use'),
        default=True)
    keep_src = Bool(
        title=_(u'don\'t remove source temp file ?'),
        description=_(u'uncheck for normal use'),
        default=True)
    keep_dst = Bool(
        title=_(u'don\'t remove dest temp file ?'),
        description=_(u'uncheck for normal use'),
        default=True)
