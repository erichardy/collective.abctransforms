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
    :param new_val: the value of the annotation
    :type new_val: string
    :param key: the annotation key
    :type key: string
    :param annotation: the annotation of a context
    :type annotation: IAnnotations
    :returns: nothing, only set annotation if new_val is not none
    """
    if new_val is not None:
        annotation[key] = new_val
    """
    # if we want to manage a max size in annotations...
    val = annotation.get(key)
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
    """
    Save in annotations **``command``_OUTPUT** and **``command``_ERRORS**
    in a given context.

    ``output`` and ``errors`` come from
    the result of a ``subprocess.Popen`` method.

    :param context: any plone object
    :type context: object
    :param command: the command name used in ``Popen`` method
    :type command: string
    :param output: the output returned by ``Popen`` method
    :type output: string
    :param errors: the error returned by ``Popen`` method
    :type errors: string
    :returns: nothing, set annotations for the context
    """
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
    This is a *almost* generic function to make the transform.
    This function convert input data given in the src param according
    to the command.

    .. note:: a special use case for *SVG* : abcm2ps allways adds 001.svg
        to output filename !!!

    For debugging purpose, if ``debug_mode`` is set in control panel,
    the *command*, *output* and *errors* will be logged. If ``keep_src`` and
    ``keep_dst`` are set in control panel, temporary input and output
    files are not deleted after command process. It is usefull to verify
    there content.

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
    :param inputsuffix: suffix to add to the temporary input file
    :type inputsuffix: string
    :param outputsuffix: suffix to add to the temporary output file
    :type outputsuffix: string
    :param context: used for annotations : the object to be annotated
    :type context: object
    :param annotate: if True, the object will be annotate
    :returns: data converted by ``command`` from ``src``
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
