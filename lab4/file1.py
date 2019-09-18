#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
\00\00\00\00\00\00\00\00\00\00\00e\9An\F7'6f\AA\FF\94ũ\E7Z\EAx\F1\F2 \B8׌\AC6\BAAT\C5\DD\A1\FC\F1\D2El>k\DAO!\F0\8F\892$\EBb
b\C1\9D|\E8M\9Bj\8D\C9:f\A8\93\A0\F6\9B\B3\C5ȑnD\E2\85yR
xA^\CDW\C5U!Y\B2s\81\DF\FEn\9A\9DDqq\CC\CFl\8En\A8\C1\D4\A2a\AF^\8A\9A\94\81\B5\F1\B3
"""
from hashlib import sha256
if  sha256(blob).hexdigest()=='41fae5b55b5a7c38c316c1bee0ad598526e623927031c215be7c5bb90b210cc9' : print "I come in peace."
else : print "Prepare to be destroyed!"
