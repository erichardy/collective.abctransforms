# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import collective.abctransforms


class CollectiveAbctransformsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=collective.abctransforms)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.abctransforms:default')


COLLECTIVE_ABCTRANSFORMS_FIXTURE = CollectiveAbctransformsLayer()


COLLECTIVE_ABCTRANSFORMS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_ABCTRANSFORMS_FIXTURE,),
    name='CollectiveAbctransformsLayer:IntegrationTesting'
)


COLLECTIVE_ABCTRANSFORMS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(COLLECTIVE_ABCTRANSFORMS_FIXTURE,),
    name='CollectiveAbctransformsLayer:FunctionalTesting'
)


COLLECTIVE_ABCTRANSFORMS_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        COLLECTIVE_ABCTRANSFORMS_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='CollectiveAbctransformsLayer:AcceptanceTesting'
)
