
.. include:: links.rst

============
Installation
============

This module must be installed like all other Plone Modules.
See : `Installing add-on packages using buildout`_


The MimeType ``text/vnd.abc`` is not registred by default. So, when the
module is activated, it is added to the ``mimetypes_registry``::

   from Products.MimetypesRegistry.MimeTypeItem import MimeTypeItem
   
   class text_abc(MimeTypeItem):
       """
       Declare properties of ``text/vnd.abc`` Mime Type
       """
       __name__ = "text_abc"
       mimetypes = ('text/vnd.abc',)
       extensions = ('abc',)
       globs = ('*.abc',)
       binary = 0
   ...
   
    mtr = getToolByName(portal, 'mimetypes_registry')
    mimetypes = mtr.lookup('text/vnd.abc')
    if len(mimetypes) == 0:
        # install 'text/vnd.abc'
        ta = text_abc()
        mtr.register(ta)

Then, every transform is installed. See :

.. automodule:: collective.abctransforms.setuphandlers
   :members: install_transforms, install_transform, post_install
   :undoc-members:

.. note:: in order a transform from ABC can be used, the ABC data must start
   with the line : ``%abc``

