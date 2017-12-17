
.. include:: links.rst

====
Bugs
====

EPSI transform
==============

It is not possible to use the transforms epsi_to_png, so, consequently abc_to_png.

The transform ``Products/PortalTransforms/transforms/image_to_png.py``
uses ``Products/PortalTransforms/libtransforms/piltransform.py`` and is configured
for the transforms : ``image/*`` to ``image/png``.

But it seems that it doesn't work for EPS to PNG!


Known bug
=========

If the instance is stopped and re-started, the module MUST be re-installed.


I don't know why ???

Tests
=====

Tests MUST be re-written !

Dependencies
============

At module install, the dependencies should be checked.
