# -*- coding: utf-8 -*-
from Products.CMFPlone.interfaces import INonInstallable
from zope.interface import implementer

from Products.CMFCore.utils import getToolByName
from plone import api
from StringIO import StringIO
from Products.MimetypesRegistry.interfaces import IMimetype
from Products.MimetypesRegistry.MimeTypeItem import MimeTypeItem
from plone import api
from plone.outputfilters.setuphandlers import register_transform_policy


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
    install_transform(portal, out)


# code from Products/CMFBibliographyAT/setuphandlers.py
def install_transform(portal, out):
    try:
        print >>out, "Add transforms"
        transform_tool = getToolByName(portal, 'portal_transforms')
        try:
            transform_tool.manage_delObjects(['abc_to_midi'])
        except:
            # XXX: get rid of bare except
            pass
        transform_tool.manage_addTransform('abc_to_midi',
                                           'collective.abctransforms.transforms.abc_to_midi')
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
    pt.unregisterTransform('abc_to_midi')
