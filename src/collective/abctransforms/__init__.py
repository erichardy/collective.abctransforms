# -*- coding: utf-8 -*-
"""Init and utils."""

import logging
from zope.i18nmessageid import MessageFactory
from Products.MimetypesRegistry.mime_types.magic import magicNumbers
from Products.MimetypesRegistry.mime_types.magic import magicTest

logger = logging.getLogger('collective.abctransforms:init')

_ = MessageFactory('collective.abctransforms')

values = [v.value for v in magicNumbers]
if '%abc' not in values:
    logger.info(u'add %abc in magicNumbers')
    m = [0, 'string', '=', '%abc', 'text/vnd.abc']
    magicNumbers.append(magicTest(m[0], m[1], m[2], m[3], m[4]))
