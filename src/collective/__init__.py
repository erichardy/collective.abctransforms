# -*- coding: utf-8 -*-
# from Products.PortalTransforms.libtransforms.utils import MissingBinary

__import__('pkg_resources').declare_namespace(__name__)

"""
modules = [
    'transforms/abc_to_midi',
]

g = globals()
transforms = []
for m in modules:
    try:
        ns = __import__(m, g, g, None)
        transforms.append(ns.register())
    except ImportError, e:
        print "Problem importing module %s : %s" % (m, e)
    except MissingBinary, e:
        print e
    except:
        import traceback
        traceback.print_exc()


def initialize(engine):
    pass

"""