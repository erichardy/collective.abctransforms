.. include:: links.rst


=====
Usage
=====

Main usage
==========

The entry point is the portal_transform tool::

   from plone import api
   pt = api.portal.get_tool('portal_transforms')

Then, the portal_transform method ``convertTo`` is called with, at least, 2 parameters :

* the target mime type : i.e. ``'image/svg+xml'``

* the data to convert.

Other arguments can be given, they are retrieved by ``**kwargs`` in the ``convert`` method
of the transform::

   class abc_to_midi(popentransform):
       implements(ITransform)
   
       __name__ = "abc_to_midi"
       inputs = ('text/vnd.abc',)
       output = 'audio/midi'
   
       __version__ = '2015-10-31.01'
   
       binaryName = "abc2midi"
       binaryArgs = ""
       useStdin = False
   
       def convert(self, orig, data, **kwargs):
           context = kwargs.get('context')
           annotate = kwargs.get('annotate')
           s_cmd = api.portal.get_registry_record(
               'abc_to_midi',
               interface=IABCTransformsSettings)
           cmd = eval(s_cmd)
           midi = from_to(
               orig,
               cmd,
               outputsuffix='.mid',
               context=context,
               annotate=annotate,
               )
           data.setData(midi)
           return data

The method returns the converted data::

        svgData = pt.convertTo(
            'image/svg+xml',
            context.abc,
            context=context,
            annotate=True
            )
        svgFilename = normalizedTitle + u'.svg'
        svgContenType = 'image/svg+xml'
        context.svgscore = NamedBlobImage()
        context.svgscore.data = svgData.getData()
        context.svgscore.filename = svgFilename
        context.svgscore.contentType = svgContenType

Annotations
===========

The transforms of this module give the ability to annotate an object with
the output and errors issued from the external commands.

In the example above :

* the parameter ``context`` is for the object to annotate

* the parameter ``annontate`` indicate if the object is annotated or not.


See the functions ``saveOutputAndErrors`` and ``manageOutputs`` in :ref:`from_to`.




