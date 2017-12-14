# -*- coding: utf-8 -*-

from datetime import datetime
import logging
import os
import tempfile as tf
import subprocess as sp
from plone import api
from zope.annotation.interfaces import IAnnotations
from collective.abctransforms.interfaces import IABCTransformsSettings

logger = logging.getLogger('collective.abctransforms')


def manageOutputs(new_val=None, key=None, annotation=None):
    """
    on peut éventuellement gérer plus finement l'output des commandes
    mais pour l'instant, on se content de mettre dans l'annotation
    la dernière valeur de l'output sans chercher à conserver un quelconque
    historique...
    la valeur ``max_output_size`` ne sert donc pas ici.
    """
    # val = annotation.get(key)
    if new_val is not None:
        annotation[key] = new_val
    """
    if new_val is not None:
        logger.info(key)
        logger.info(new_val)
        if val is None:
            annotation[key] = val
        else:
            maxsize = api.portal.get_registry_record(
                'max_output_size',
                interface=IABCTransformsSettings)
            if len(val) > maxsize:
                annotation[key] = val[len(val) - maxsize:]
            annotation[key] += u'\n--\n' + new_val
    """


def saveOutputAndErrors(context, command, output, errors):
    annot = IAnnotations(context)
    now = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    try:
        cmd = command[0]
    except Exception:
        cmd = u'COMMAND?'
    K_OUTPUT = cmd + u'_OUTPUT'
    manageOutputs(
        new_val=now + '\n' + output,
        key=K_OUTPUT,
        annotation=annot)
    K_ERRORS = cmd + u'_ERRORS'
    manageOutputs(
        new_val=now + '\n' + errors,
        key=K_ERRORS,
        annotation=annot)


def from_to(src,
            command,
            toappend=None,
            inputsuffix=None,
            outputsuffix=None,
            context=None,
            annotate=False):
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

    if annotate:
        saveOutputAndErrors(context, command, output, errors)
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
