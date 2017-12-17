

==========
Transforms
==========

Intro
=====

All the transform classes implement ``Products.PortalTransforms.interfaces.ITransform``
interface. So, they have a ``convert`` method wich takes the source data to convert.

See :doc:`usage` for more information...

.. _from_to:

Methods used by transforms
==========================

.. automodule:: collective.abctransforms.utils
   :members: manageOutputs, saveOutputAndErrors, from_to
   :undoc-members:

abc_to_midi
===========

.. autoclass:: collective.abctransforms.transforms.abc_to_midi.abc_to_midi
   :members: convert
   :undoc-members:

abc_to_mp3
==========

.. autoclass:: collective.abctransforms.transforms.abc_to_mp3.abc_to_mp3
   :members: convert
   :undoc-members:

abc_to_ogg
==========

.. autoclass:: collective.abctransforms.transforms.abc_to_ogg.abc_to_ogg
   :members: convert
   :undoc-members:

abc_to_pdf
==========

.. autoclass:: collective.abctransforms.transforms.abc_to_pdf.abc_to_pdf
   :members: convert
   :undoc-members:

abc_to_png
==========

Doesn't work !

.. autoclass:: collective.abctransforms.transforms.abc_to_png.abc_to_png
   :members: convert
   :undoc-members:

abc_to_ps
=========

.. autoclass:: collective.abctransforms.transforms.abc_to_ps.abc_to_ps
   :members: convert
   :undoc-members:

abc_to_svg
==========

.. autoclass:: collective.abctransforms.transforms.abc_to_svg.abc_to_svg
   :members: convert
   :undoc-members:

aiff_to_mp3
===========

.. autoclass:: collective.abctransforms.transforms.aiff_to_mp3.aiff_to_mp3
   :members: convert
   :undoc-members:

epsi_to_png
===========

Doesn't work !

.. autoclass:: collective.abctransforms.transforms.epsi_to_png.epsi_to_png
   :members: convert
   :undoc-members:

midi_to_aiff
============

.. autoclass:: collective.abctransforms.transforms.midi_to_aiff.midi_to_aiff
   :members: convert
   :undoc-members:

midi_to_ogg
===========

.. autoclass:: collective.abctransforms.transforms.midi_to_ogg.midi_to_ogg
   :members: convert
   :undoc-members:

ps_to_epsi
==========

.. autoclass:: collective.abctransforms.transforms.ps_to_epsi.ps_to_epsi
   :members: convert
   :undoc-members:

ps_to_pdf
=========

.. autoclass:: collective.abctransforms.transforms.ps_to_pdf.ps_to_pdf
   :members: convert
   :undoc-members:
