# -*- coding: utf-8 -*-

import logging
from plone import api
import os
import tempfile as tf
import subprocess as sp

logger = logging.getLogger('collective.abctransforms')


def add_abc_MIMEType():
    # manage_addMimeType
    '''
    mr = api.portal.get_tool(name='mimetypes_registry')
    mr.manage_addMimeType(
        'text_abc',
        mimetypes=['text/vnd.abc'],
        extensions=['abc'],
        binary=False,
        icon_path='txt.png',
        globs=['*.abc'])
    Il faut aussi trouver comment ajouter le 'magic' :
    from Products.MimetypesRegistry.mime_types.magic import magicNumbers
    from Products.MimetypesRegistry.mime_types.magic import magicTest
    m = [0, 'string', '=', '%abc', 'text/vnd.abc']
    magicNumbers.append(magicTest(m[0], m[1], m[2], m[3], m[4]))
    mat = magicTest(m[0], m[1], m[2], m[3], m[4])
    (Pdb) mat.msg
    'text/vnd.abc'
    (Pdb) mat.op
    '='
    (Pdb) mat.value
    '%abc'
    (Pdb) mat.type
    'string'
    '''
    pass

def from_to(src,
            command,
            toappend=None,
            logging=False,
            inputsuffix=None,
            outputsuffix=None):
    """
    This function convert input data given in the src param according
    to the command.

    :param src: data to convert
    :type src: any type
    :param command: external command to apply to src. Special strings
        "datain" and "dataout" in the list give the position of input
        and output files in the command string (usualy a command line).
        The first element is a binary to call, the others are options
        and/or parameters.
    :type command: list of strings, first element is a binary to call,
    :param toappend: bytes to append to src data
    :type toappend: bytes
    :param logging: output logs if True
    :type logging: boolean
    :returns: data converted by `command` from `src`
    """
    if not inputsuffix:
        inputsuffix = ''
    if not outputsuffix:
        outputsuffix = ''
    srcfile = tf.NamedTemporaryFile(mode='w+b',
                                    suffix=inputsuffix,
                                    delete=False).name
    fdsrc = open(srcfile, "wb")
    fdsrc.write(src)
    if toappend:
        fdsrc.write(toappend)
    fdsrc.close()
    destfile = tf.NamedTemporaryFile(mode='w+b',
                                     suffix=outputsuffix,
                                     delete=False).name
    command[command.index("datain")] = srcfile
    command[command.index("dataout")] = destfile
    p = sp.Popen(command, stdout=sp.PIPE, stderr=sp.PIPE)
    p.wait()

    fddest = open(destfile, "rb")
    destdata = fddest.read()
    fddest.close()
    output, errors = p.communicate()
    if logging:
        logger.info(errors)
        logger.info(output)
    os.unlink(srcfile)
    os.unlink(destfile)
    return destdata
