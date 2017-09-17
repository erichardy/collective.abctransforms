# -*- coding: utf-8 -*-

import logging
import os
import tempfile as tf
import subprocess as sp
from plone import api
from collective.abctransforms.interfaces import IABCTransformsSettings

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
    :returns: data converted by `command` from `src`
    """
    debug_mode = api.portal.get_registry_record(
        'debug_mode',
        interface=IABCTransformsSettings)
    if not inputsuffix:
        inputsuffix = ''
    if not outputsuffix:
        outputsuffix = ''
    to = ''
    if outputsuffix == 'svg':
        # special SVG : abcm2ps allways adds 001.svg to output filename !!!
        to = 'svg'
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
    if to == 'svg':
        # special SVG : abcm2ps allways adds 001.svg to output filename !!!
        destfile = destfile + '001.svg'
    if debug_mode:
        logger.info('srcfile : ' + srcfile)
        logger.info('destfile : ' + destfile)
        show_command = api.portal.get_registry_record(
            'show_command',
            interface=IABCTransformsSettings)
        if show_command:
            logger.info('command : ' + str(command))
        keep_src = api.portal.get_registry_record(
            'keep_src',
            interface=IABCTransformsSettings)
        keep_dst = api.portal.get_registry_record(
            'keep_dst',
            interface=IABCTransformsSettings)
    p = sp.Popen(command, stdout=sp.PIPE, stderr=sp.PIPE)
    p.wait()

    fddest = open(destfile, "rb")
    destdata = fddest.read()
    fddest.close()
    output, errors = p.communicate()
    if debug_mode:
        logger.info(errors)
        logger.info(output)
        if not keep_src:
            os.unlink(srcfile)
        if not keep_dst:
            os.unlink(destfile)
    else:
        os.unlink(srcfile)
        os.unlink(destfile)
    return destdata
