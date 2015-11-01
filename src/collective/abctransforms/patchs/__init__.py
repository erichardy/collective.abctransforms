# -*- coding: utf-8 -*-
from Acquisition import aq_base
from zope.contenttype import guess_content_type


def patchedclassify(self, data, mimetype=None, filename=None):
    """Classify works as follows:
    1) you tell me the rfc-2046 name and I give you an IMimetype
       object
    2) the filename includes an extension from which we can guess
       the mimetype
    3) we can optionally introspect the data
    4) default to self.defaultMimetype if no data was provided
       else to application/octet-stream of no filename was provided,
       else to text/plain

    Return an IMimetype object or None
    """
    mt = None
    if mimetype:
        mt = self.lookup(mimetype)
        if mt:
            mt = mt[0]
    elif filename:
        mt = self.lookupExtension(filename)
        if mt is None:
            mt = self.globFilename(filename)
    if data and not mt:
        for c in self._classifiers():
            if c.classify(data):
                mt = c
                break
        if not mt:
            from collective.abctransforms import magic_with_abc
            mstr = magic_with_abc.guessMime(data)
            if mstr:
                _mt = self.lookup(mstr)
                if len(_mt) > 0:
                    mt = _mt[0]
    if not mt:
        if not data:
            mtlist = self.lookup(self.defaultMimetype)
        elif filename:
            mtlist = self.lookup('application/octet-stream')
        else:
            failed = 'text/x-unknown-content-type'
            filename = filename or ''
            data = data or ''
            ct, enc = guess_content_type(filename, data, None)
            if ct == failed:
                ct = 'text/plain'
            mtlist = self.lookup(ct)
        if len(mtlist) > 0:
            mt = mtlist[0]
        else:
            return None

    # Remove acquisition wrappers
    return aq_base(mt)
