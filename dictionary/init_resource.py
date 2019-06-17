import os
import sys
import json
import android
import os
import sys
import glob
folder="/sdcard/extras/org.qpython.qpy/files/lib/python2.7/site-packages/*.egg"
for file in glob.glob(folder):
    sys.path.append(file)
import nltk 
import ssl
from nltk.corpus import wordnet
try: 
    _create_unverified_https_context = ssl._create_unverified_context 
except AttributeError: 
    pass
else: 
    ssl._create_default_https_context = _create_unverified_https_context 
nltk.data.path.append("/sdcard/nltkdata")
#Initialize Android
droid = android.Android()
os.environ['PATH'] = os.environ['PATH']+':/data/data/com.termux/files/usr/bin/'
os.environ['SHELL'] = '/data/data/com.termux/files/usr/bin/sh'
os.environ['MKSH'] = '/data/data/com.termux/files/usr/bin/sh'
os.environ['LD_LIBRARY_PATH'] = os.environ['LD_LIBRARY_PATH']+":"+'/data/data/com.termux/files/usr/lib'
import subprocess
def run(args):
	p= subprocess.Popen(args,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	p_out, p_err = p.communicate()
	return p_out, p_err 
def take_pic(path,layout):
	
	file='/sdcard/'+path+'.png'
	pic=droid.cameraInteractiveCapturePicture(file)
	layout.views.result.text="Processing ..."
	args=['tesseract', '--tessdata-dir', '/data/data/com.termux/files/usr/share', file ,'stdout', '-l', 'eng' ,'--psm', '3']
	return run(args)
def define(term,layout):
	layout.views.result.text="Processing ..."
	try:
		syns = wordnet.synsets(term)
		res = syns[0].definition()
		return res
	except:
		return "no result"
def getDefinition(word,layout):
    layout.views.result.text="Processing ..."
    try:
    	res=""
    	#get word synsets
        syns = wordnet.synsets(word)
        c = 1
        #loop over sunsets and get definition
        for s in syns:
            res += str(c)+')'+s.definition()+"\n"
            res += "\n"
            c += 1
        #res = syns[0].definition()
        layout.views.result.text=res
        #return res
    except Exception as e:
        return e
