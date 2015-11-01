# -*- coding: utf-8 -*-

import logging
import os
import tempfile as tf
import subprocess as sp

logger = logging.getLogger('collective.abctransforms')


def from_to(src, command, toappend=None, logging=False):
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
    srcfile = tf.NamedTemporaryFile(mode='w+b',
                                    delete=False).name
    fdsrc = open(srcfile, "wb")
    fdsrc.write(src)
    if toappend:
        fdsrc.write(toappend)
    fdsrc.close()
    destfile = tf.NamedTemporaryFile(mode='w+b',
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
