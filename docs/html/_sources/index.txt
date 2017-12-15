
.. include:: links.rst

=========================================
Documentation de collective.abctransforms
=========================================

Documentation of ``collective.abctransforms`` by `Eric Hardy`_.

Installation
============
add *collective.abctransforms* to the ``eggs`` section in the *buildout.cfg* file

and the source in section ``[sources]``::

   collective.abctransforms = git git@github.com:erichardy/collective.abctransforms.git

and re-run ``bin/buildout``.

Intro
=====

``collective.abctransforms`` is a set of transforms and transform chains for `Plone`_.
So, it is targeted to **Plone Developpers**, not for end users.

The main starting point is the transform from a text in `ABC music notation`_ to
MIDI, SVG, etc...

This set of transforms has many *Linux/Unix* dependencies : see :doc:`dependencies`.

Most of the transforms can be configured in the control panel : see :doc:`configuration`.

Compatibility : Plone 5 (not tested for Plone 4).

This module is used in the module `collective.abctune`_

.. warning:: documentation in progress !

Toute la documentation
======================

.. toctree::
    :maxdepth: 2

    Dependencies <dependencies>
    Configuration <configuration>
    Usage <usage>
    Transforms <transforms>
    LICENSE <LICENSE>
