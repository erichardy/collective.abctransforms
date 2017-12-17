# -*- coding: utf-8 -*-

# import re
import glob
# from sys import modules
from os.path import join, abspath, dirname, basename
from os import system
import subprocess as sp


PREFIX = abspath(dirname(__file__))


def input_file_path(f):
    return join(PREFIX, 'inputs', f)


def output_file_path(f):
    return join(PREFIX, 'outputs', f)


def matching_inputs(pattern):
    return [basename(path) for path in
            glob.glob(join(PREFIX, "input", pattern))]


registryRecords = {
    'abc_to_midi': u'["abc2midi", "datain", "-o", "dataout"]',
    'midi_to_aiff': u'["timidity", "-A 400", "-EFchorus=2,50", "-EFreverb=2", "datain", "-o", "dataout", "-Oa"]',
    'aiff_to_mp3': u'["lame","--cbr", "-b 32","-f","--quiet","datain", "dataout"]',
    'midi_to_ogg': u'["timidity", "-A 400", "-EFchorus=2,50", "-EFreverb=2", "datain", "-o", "dataout", "-Ov"]',
    'abc_to_ps': u'["abcm2ps", "datain", "-O", "dataout"]',
    'ps_to_epsi': u'["ps2epsi", "datain", "dataout"]',
    'epsi_to_png': u'["convert", "-filter", "Catrom", "-resize", "600", "datain", "dataout"]',
    'ps_to_pdf': u'["ps2pdf", "datain", "dataout"]',
    'abc_to_svg': u'["abcm2ps", "datain", "-g", "-O", "dataout"]',
    'debug_mode': True,
    'show_command': True,
    'keep_src': True,
    'keep_dst': True,
    'max_output_size': 1000,
    }


def createFile(data, name):
    try:
        fout = open(input_file_path(name), 'w')
        fout.write(data)
        fout.close()
        return name
    except Exception:
        raise IOError


def fileType(name):
    try:
        cmd = ['file', input_file_path(name)]
        p = sp.Popen(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
        p.wait()
        o_output, o_errors = p.communicate()
        return ' '.join(o_output.split(':')[1:]).strip()
    except Exception:
        return False


def createSoundFiles():
    # abc_to_midi
    datain = input_file_path('DonaldBlue.abc')
    dataout = input_file_path('DonaldBlue.mid')
    lcmd = eval(registryRecords['abc_to_midi'])
    lcmd[lcmd.index('datain')] = datain
    lcmd[lcmd.index('dataout')] = dataout
    cmd = ' '.join(lcmd)
    system(cmd)
    # midi_to_aiff
    datain = input_file_path('DonaldBlue.mid')
    dataout = input_file_path('DonaldBlue.aiff')
    lcmd = eval(registryRecords['midi_to_aiff'])
    lcmd[lcmd.index('datain')] = datain
    lcmd[lcmd.index('dataout')] = dataout
    cmd = ' '.join(lcmd)
    system(cmd)
    # aiff_to_mp3
    datain = input_file_path('DonaldBlue.aiff')
    dataout = input_file_path('DonaldBlue.mp3')
    lcmd = eval(registryRecords['aiff_to_mp3'])
    lcmd[lcmd.index('datain')] = datain
    lcmd[lcmd.index('dataout')] = dataout
    cmd = ' '.join(lcmd)
    system(cmd)
    # midi_to_ogg
    datain = input_file_path('DonaldBlue.mid')
    dataout = input_file_path('DonaldBlue.ogg')
    lcmd = eval(registryRecords['midi_to_ogg'])
    lcmd[lcmd.index('datain')] = datain
    lcmd[lcmd.index('dataout')] = dataout
    cmd = ' '.join(lcmd)
    system(cmd)


def deleteSoundFiles():
    f1 = input_file_path('DonaldBlue.mid') + ' '
    f2 = input_file_path('DonaldBlue.aiff') + ' '
    f3 = input_file_path('DonaldBlue.ogg') + ' '
    f4 = input_file_path('DonaldBlue.mp3') + ' '
    f5 = input_file_path('aiff.aiff') + ' '
    f6 = input_file_path('ogg.ogg')
    cmd = 'rm ' + f1 + f2 + f3 + f4 + f5 + f6
    system(cmd)


def createScoreFiles():
    # abc_to_midi
    datain = input_file_path('DonaldBlue.abc')
    dataout = input_file_path('DonaldBlue.ps')
    lcmd = eval(registryRecords['abc_to_ps'])
    lcmd[lcmd.index('datain')] = datain
    lcmd[lcmd.index('dataout')] = dataout
    cmd = ' '.join(lcmd)
    system(cmd)
    # ps_to_epsi
    datain = input_file_path('DonaldBlue.ps')
    dataout = input_file_path('DonaldBlue.epsi')
    lcmd = eval(registryRecords['ps_to_epsi'])
    lcmd[lcmd.index('datain')] = datain
    lcmd[lcmd.index('dataout')] = dataout
    cmd = ' '.join(lcmd)
    system(cmd)
    # epsi_to_png
    datain = input_file_path('DonaldBlue.epsi')
    dataout = input_file_path('DonaldBlue.png')
    lcmd = eval(registryRecords['epsi_to_png'])
    lcmd[lcmd.index('datain')] = datain
    lcmd[lcmd.index('dataout')] = dataout
    cmd = ' '.join(lcmd)
    system(cmd)
    # ps_to_pdf
    datain = input_file_path('DonaldBlue.ps')
    dataout = input_file_path('DonaldBlue.pdf')
    lcmd = eval(registryRecords['ps_to_pdf'])
    lcmd[lcmd.index('datain')] = datain
    lcmd[lcmd.index('dataout')] = dataout
    cmd = ' '.join(lcmd)
    system(cmd)


def deleteScoreFiles():
    f1 = input_file_path('DonaldBlue.ps') + ' '
    f2 = input_file_path('ps.ps') + ' '
    f3 = input_file_path('DonaldBlue.png') + ' '
    f4 = input_file_path('DonaldBlue.ps') + ' '
    f5 = input_file_path('DonaldBlue.epsi') + ' '
    f6 = input_file_path('DonaldBlue.pdf') + ' '
    f7 = input_file_path('pdf.pdf') + ' '
    f8 = input_file_path('pdf.pdf') + ' '
    cmd = 'rm -f ' + f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8
    system(cmd)


