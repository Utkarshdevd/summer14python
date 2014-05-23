from nltk.corpus import wordnet
x = 'social'
y = 'network'
xsyn = wordnet.synsets(x)
# xsyn
#[Synset('sociable.n.01'), Synset('social.a.01'), Synset('social.a.02'),   
#Synset('social.a.03'), Synset('social.s.04'), Synset('social.s.05'),   
#Synset('social.s.06')]

ysyn = wordnet.synsets(y)
#ysyn
#[Synset('network.n.01'), Synset('network.n.02'), Synset('net.n.06'), 
#Synset('network.n.04'), Synset('network.n.05'), Synset('network.v.01')]

xlen = len(xsyn)
ylen = len(ysyn)

import numpy
simindex = numpy.zeros( (xlen,ylen) )

def relative_matrix(asyn,bsyn,simindex): # find similarity between asyn & bsyn

    I = -1
    J = -1

    for asyn_element in asyn:
        I += 1

        cb = wordnet.synset(asyn_element.name)
        J = -1
        for bsyn_element in bsyn:
            J += 1
            ib = wordnet.synset(bsyn_element.name)
            if not cb.pos == ib.pos: # compare nn , vv not nv or an
                continue
            score = cb.wup_similarity(ib)
            r = cb.path_similarity(ib)
            if simindex [I,J] < score:
                simindex [I,J] = score

 relative_matrix(xsyn,ysyn,simindex)
 print simindex
'''
array([[ 0.46153846,  0.125     ,  0.13333333,  0.125     ,  0.125     ,
     0.        ],
   [ 0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
     0.        ],
   [ 0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
     0.        ],
   [ 0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
     0.        ],
   [ 0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
     0.        ],
   [ 0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
     0.        ],
   [ 0.        ,  0.        ,  0.        ,  0.        ,  0.        ,
     0.        ]])
'''
#xsyn[0].definition
#'a party of people assembled to promote sociability and communal activity'
#ysyn[0].definition
#'an interconnected system of things or people'
