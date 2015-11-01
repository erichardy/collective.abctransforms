# -*- coding: utf-8 -*-

from zope.publisher.browser import BrowserView
from pdb import set_trace


class debug(BrowserView):
    """Excécute le débugger de python pour le contexte dans lequel cette vue
    est appelée.

    Cette vue ne peut être appelée que si l'utilisateur a un rôle manager
    et est appelée avec : @@debug

    Action configurée dans le fichier profiles/default/actions.xml
    """
    def __call__(self):
        set_trace()
