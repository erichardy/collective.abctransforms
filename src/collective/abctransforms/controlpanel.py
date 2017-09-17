# -*- coding: utf-8 -*-

from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plonetheme.iuem20 import _
from plonetheme.iuem20.interfaces import IPlonethemeIuem20Settings


class IABCTransformsSettingsForm(RegistryEditForm):
    schema = IPlonethemeIuem20Settings
    label = _(u'plonetheme.iuem20 Settings')
    description = _(u'plonetheme.iuem20 Settings Description')

    """
    def updateFields(self):
        super(IIuemAgreementsSettingsForm, self).updateFields()

    def updateWidgets(self):
        super(IIuemAgreementsSettingsForm, self).updateWidgets()
    """


class IABCTransformsControlPanel(ControlPanelFormWrapper):
    form = IABCTransformsSettingsForm
