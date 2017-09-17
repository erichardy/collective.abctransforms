# -*- coding: utf-8 -*-

from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from collective.abctransforms import _
from collective.abctransforms.interfaces import IABCTransformsSettings


class IABCTransformsSettingsForm(RegistryEditForm):
    schema = IABCTransformsSettings
    label = _(u'ABC transforms Settings')
    description = _(u'ABC transforms Settings Description')

    """
    def updateFields(self):
        super(IIuemAgreementsSettingsForm, self).updateFields()

    def updateWidgets(self):
        super(IIuemAgreementsSettingsForm, self).updateWidgets()
    """


class IABCTransformsControlPanel(ControlPanelFormWrapper):
    form = IABCTransformsSettingsForm
