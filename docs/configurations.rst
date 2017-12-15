
.. include:: links.rst


==============
Configurations
==============

External commands configurations
================================

Most of the transforms use external commands. They are listed in :doc:`dependencies`.

The usage of these commands are found in the control panel. Every parameter
must follow the rules below :

* It must be a python list of strings

* The first element of the list is the command to run (usally a binary)

* The list MUST contain an element ``"datain"`` **AND** an element ``"dataout"``.
  They are used for the position of the source and destination files in the
  function ``from_to`` (see :ref:`from_to`).

For example::

   ["abc2midi", "datain", "-o", "dataout"]
   or
   ["timidity", "-A 400", "-EFchorus=2,50", "-EFreverb=2", "datain", "-o", "dataout", "-Oa"]'


The control panel contains default values for these commands but it is possible to
adapt them to fit other needs...

.. autoclass:: collective.abctransforms.interfaces.IABCTransformsSettings
   :members:
   :undoc-members:

Debug configuration
===================

In order to verify that commands are run accordingly, debug options can be set :

* ``debug_mode`` : complete command is logged to the console

* ``keep_src`` : after the command run, the source file is not deleted.

* ``keep_dst`` : after the command run, the destination file is not deleted.

.. warning:: be aware that the use of ``keep_src`` and ``keep_dst`` can fulfil
   the temp folder !


max_output_size
===============

``max_output_size`` can be used to limit the maximun size of output or errors
stored in annotations. NOT USED for now...

