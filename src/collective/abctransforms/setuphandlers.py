# -*- coding: utf-8 -*-
import logging
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer

from Products.CMFCore.utils import getToolByName
from plone import api
from StringIO import StringIO
from Products.MimetypesRegistry.MimeTypeItem import MimeTypeItem
# from plone.outputfilters.setuphandlers import register_transform_policy
from Products.PortalTransforms.chain import chain
from collective.abctransforms.transforms.abc_to_midi import abc_to_midi
from collective.abctransforms.transforms.midi_to_aiff import midi_to_aiff
from collective.abctransforms.transforms.aiff_to_mp3 import aiff_to_mp3

logger = logging.getLogger('collective.abctransforms:GS')

module = 'collective.abctransforms.transforms.'
abctransforms = []
abctransforms.append('abc_to_midi')
abctransforms.append('midi_to_aiff')
abctransforms.append('aiff_to_mp3')
abctransforms.append('abc_to_mp3')


class text_abc(MimeTypeItem):
    __name__ = "text_abc"
    mimetypes = ('text/vnd.abc',)
    extensions = ('abc',)
    globs = ('*.abc',)
    binary = 0


@implementer(INonInstallable)
class HiddenProfiles(object):

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller"""
        return [
            'collective.abctransforms:uninstall',
        ]


def post_install(context):
    """Post install script
    First, test if text/vnd.abc mimetype exists,
    If not, add it to MimetypesRegistry
    """
    if context.readDataFile('collectiveabctransforms_default.txt') is None:
        return
    # Do something during the installation of this package
    portal = api.portal.get()
    mtr = getToolByName(portal, 'mimetypes_registry')
    mimetypes = mtr.lookup('text/vnd.abc')
    if len(mimetypes) == 0:
        # install 'text/vnd.abc'
        ta = text_abc()
        mtr.register(ta)
    out = StringIO()
    portal = api.portal.get()
    # register_transform_policy(portal, 'text/vnd.abc', 'abc_to_midi')
    install_transforms(portal, out)
    # install_chain(portal, "abc_to_mp3")


def install_chain(portal, chainId):
    portal = api.portal.get()
    pt = getToolByName(portal, 'portal_transforms')
    abc_to_mp3 = chain('abc_to_mp3')
    abc_to_mp3.registerTransform(abc_to_midi())
    abc_to_mp3.registerTransform(midi_to_aiff())
    abc_to_mp3.registerTransform(aiff_to_mp3())
    try:
        pt.registerTransform(abc_to_mp3())
    except:
        pass


def install_transforms(portal, out):
    for abctransform in abctransforms:
        install_transform(portal, out, abctransform)


# code from Products/CMFBibliographyAT/setuphandlers.py
def install_transform(portal, out, abctransform):
    print 'install ' + abctransform
    try:
        print >>out, "Add transforms"
        pt = getToolByName(portal, 'portal_transforms')
        try:
            pt.manage_delObjects([abctransform])
        except:
            logger.info(abctransform + ' not yet installed')
            # XXX: get rid of bare except

        pt.manage_addTransform(abctransform,
                               module + abctransform)
        # see Products/CMFBibliographyAT/setuphandlers.py
        # addPolicy(transform_tool, out)
    except (NameError, AttributeError):
        print >>out, "No MimetypesRegistry, text/vnd.abc not supported."


def uninstall(context):
    """Uninstall script"""
    if context.readDataFile('collectiveabctransforms_uninstall.txt') is None:
        return
    # Do something during the uninstallation of this package
    portal = api.portal.get()
    mtr = getToolByName(portal, 'mimetypes_registry')
    mimetypes = mtr.lookup('text/vnd.abc')
    if len(mimetypes) != 0:
        # uninstall 'text/vnd.abc'
        ta = text_abc()
        mtr.unregister(ta)
    pt = getToolByName(portal, 'portal_transforms')
    
    for abctransform in abctransforms:
        pt.unregisterTransform(abctransform)
    # pt.unregisterTransform("abc_to_mp3")
