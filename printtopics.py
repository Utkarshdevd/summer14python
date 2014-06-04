#!/usr/bin/python

# printtopics.py: Prints the words that are most prominent in a set of
# topics.
#
# Copyright (C) 2010  Matthew D. Hoffman
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys, os, re, random, math, urllib2, time, cPickle
import numpy

import onlineldavb
'''--------------------'''
from pylab import *

def plotData(dataValue, dataId):
    n = len(dataId)
    X = np.arange(n)
    Y1 = []
    for _ in dataValue:
        Y1.append(100*_)
    print Y1
    bar(X, Y1, facecolor='#9999ff', edgecolor='white')

    for x,y,ID in zip(X,Y1, dataId):
        text(x+0.4, y+0.05, '%.2f' % y, ha='center', va= 'bottom')
        text(x+0.6, y+ 0.1, '%20s' % ID, ha='center', va= 'bottom', rotation=90)

    ylim(0, 20)
    show()
'''--------------------'''
def main():
    """
    Displays topics fit by onlineldavb.py. The first column gives the
    (expected) most prominent words in the topics, the second column
    gives their (expected) relative prominence.
    """
    vocab = str.split(file(sys.argv[1]).read())
    testlambda = numpy.loadtxt(sys.argv[2])

    newVocab = file(str(sys.argv[-1])).readlines()
    for _ in newVocab:
        vocab.append(_)

    for k in range(0, len(testlambda)):
        # all in a row
        lambdak = list(testlambda[k, :])
        lambdak = lambdak / sum(lambdak)
        temp = zip(lambdak, range(0, len(lambdak)))
        temp = sorted(temp, key = lambda x: x[0], reverse=True)
        print 'topic %d:' % (k)
        # feel free to change the "53" here to whatever fits your screen nicely.
        num = 12
        dataId = []
        dataValue = []
        for _ in range(0, num):
            #print '%20s  ---  %.4f' % (vocab[temp[_][1]], temp[_][0])
            '''--------------------'''
            dataId.append(vocab[temp[_][1]])
            dataValue.append(float(temp[_][0]))
            '''--------------------'''
        '''--------------------'''
        plotData(dataValue, dataId)
        #raw_input("Press Enter to continue...")
        '''--------------------'''
        print

if __name__ == '__main__':
    main()
