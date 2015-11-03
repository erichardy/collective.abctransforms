
.. _List of Common MIME Types: http://hul.harvard.edu/ois/systems/wax/wax-public-help/mimetypes.htm
.. _Fileformat.info: http://www.fileformat.info/info/mimetype/text/vnd.abc/index.htm
.. _MIME type for ABC: http://www.ucolick.org/~sla/abcmusic/abcmime.html
.. _text/vnd.abc: https://www.iana.org/assignments/media-types/text/vnd.abc
.. _abc music notation: http://abcnotation.com/

========================
collective.abctransforms
========================

This plone module provides transform utilities for ABC music notation.

First, the mimetype 'text/vnd.abc' is created according to some informations
gathered from internet :

`List of Common MIME Types`_

`Fileformat.info`_

`MIME type for ABC`_

`text/vnd.abc`_

Other used mimetypes already exist : application/postscript, image/x-eps, audio/x-wav,
audio/wav, audio/vnd.wave, audio/mpeg, audio/x-mp3, audio/x-mpeg, audio/mp3
image/png, audio/midi, audio/x-midi

The transformations from a tune coded in abc music notation are installed in
portal_transform tool.

=====
Usage
=====

This module doesn't provide any content type. It can be usefull for developpers
concerned by `abc music notation`_.

In addition to mimetype **text/vnd.abc**, some utilities are installed which
allow transformation :

* from ``abc`` to ``midi`` (for sound)

* from ``abc`` to ``mp3`` (for sound)

* from ``abc`` to ``PDF`` (for scores)

* from ``abc`` to ``png`` (for scores)

The best way to know how to use the transformations is to look at the tests.

Example::

   from Products.CMFCore.utils import getToolByName
   from plone import api
   
   abc = """
   %abc
   X:1
   %%MIDI chordvol 30
   %%MIDI bassvol 30
   P: A
   Q:190
   T: Donald Blue
   M: 4/4
   L: 1/8
   R: reel
   K: Dmaj
   P: A
   |:"D"dBAF A2 FA|dBAF "A"EFDA|"D"dBAF A2 FA|1"Bm"B2 BA B2 AB:|2"Bm"B2 BA B2 d2|
   |:"D"ABde faaa|"G"g2 fd "Em"edBd|"D"ABde fafd |1"Bm"B2 BA B2 dB:|2"Bm"B2 BA B2 AB|
   """
   portal = api.portal.get()
   pt = getToolByName(portal, "portal_transforms")
   midiStream = pt.convertTo('audio/x-midi', abc)
   midi = midiStream.getData()



   

