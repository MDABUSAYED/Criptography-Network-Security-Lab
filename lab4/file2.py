#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           en÷'6fªÿÅ©çZêxñò ¸×¬6ºATÅÝ¡üñÒEl>kÚO!ð2$ëb
bÁ|èMêÉ:f¨ ö³ÅÈnDâ
yÒ
xA^ÍWÅU!Y²sßþnDqqÌÏln¨ÁÔ¢a¯^µñ³
"""
from hashlib import sha256
if  sha256(blob).hexdigest()=='41fae5b55b5a7c38c316c1bee0ad598526e623927031c215be7c5bb90b210cc9' : print "I come in peace."
else : print "Prepare to be destroyed!"
