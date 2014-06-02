****************************************************************************
	PROJECT : CROWDSOURCED POWERED PLATFORM
	AUTHOR  : UTKARSH DWIVEDI
	PURPOSE : NLTK BASED TEXT EXTRACTOR IN PYTHON 2.7.5
	DATE    : 05-17-2014
****************************************************************************

This extractor will take out all the violation passages in typical environmental impact assessment 
and environmental clearances texts.
NLTK library is used along with REGEX, in Python.

REQUIREMENTS
=> SCIPY
=> RE
=> NUMPY
=> NLTK

FOLDER STRUCTURE
 - lambda/		# stores lamda.dat files from LDA
 - gamma/		# stores gamma.dat files from LDA
 - data/		# this is the data folder, all your text data goes here with a proper name convention
 - res /		# here the corresponding violations are stripped and kept

FILE STRUCTURE
onlineldavb.py 		:	functions for processing documents, and performing LDA topic modelling
reTRY.py 	   		:	extracts violations from raw clearance docs
removeDict.py 		:	purges data off stopwords(english), punctuations, numbers(possible loss of data)
onlinewikipedia.py  :	controller file for running LDA on data
PARAMETER_FILE.txt 	:	Contains all modifiable parameters
nameGen.py 			:	generates filenames of data, results using input from parameter file
getDocList.py 		:	appends all purged docs into a list, for use in onlinewikipedia.py(HACK)
printtopics.py 		:	prints results of lda, takes dictionary and lamda or gamma file as input
dictnostops.txt 	: 	vocab source used, is updated by new words from data