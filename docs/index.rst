
.. _List of Common MIME Types: http://hul.harvard.edu/ois/systems/wax/wax-public-help/mimetypes.htm
.. _Fileformat.info: http://www.fileformat.info/info/mimetype/text/vnd.abc/index.htm
.. _MIME type for ABC: http://www.ucolick.org/~sla/abcmusic/abcmime.html
.. _text/vnd.abc: https://www.iana.org/assignments/media-types/text/vnd.abc

========================
collective.abctransforms
========================

This plone module provides transform utilities for ABC music notation.

First, the mimetype 'text/vnd.abc' is created according to some insformations
gathered from internet :

`List of Common MIME Types`_

`Fileformat.info`_

`MIME type for ABC`_

`text/vnd.abc`_

Other used mimetypes already exist : application/postscript, image/x-eps, audio/x-wav,
audio/wav, audio/vnd.wave, audio/mpeg, audio/x-mp3, audio/x-mpeg, audio/mp3
image/png, audio/midi, audio/x-midi

examples :
Products.PortalTransforms-2.1.10-py2.7.egg/Products/PortalTransforms/transforms/pdf_to_text.py
Products.PortalTransforms-2.1.10-py2.7.egg/Products/PortalTransforms/transforms/__init__.py (register)

class ITransform : Products.PortalTransforms-2.1.10-py2.7.egg/Products/PortalTransforms/interfaces.py

For install transform, see :
https://github.com/collective/Products.CMFBibliographyAT/blob/master/Products/CMFBibliographyAT/setuphandlers.py
