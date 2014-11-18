import numpy
from pylab import zeros, sin, cos, normal, random
from Tilecoder import numTilings, tilecode

     # initialize weights appropriately here
w = numpy.zeros(968)
     # initialize step size parameter appropriately here
stepsize=.1/numTilings
     # initialize your global list of tile indices here
tileIndices = [-1]*numTilings
    
def f(in1,in2):
    " write your linear function approximator here (5 lines or so)"
    tilecode(in1,in2,tileIndices)
    weights=w[tileIndices]
    return sum(weights)
   
def learn(in1,in2,target):
    " write your gradient descent learning algorithm here (3 lines or so)"
    function=f(in1,in2)
    for i in tileIndices:
        w[i]=w[i]+stepsize*(target-function)

def test1():
   for in1,in2,target in \
         [ (0.1, 0.1, 2.0), \
           (4.0, 2.0, -1.0), \
           (5.99, 5.99, 3.0), \
           (4.0, 2.1, -1.0) ]:
        before = f(in1,in2)
        learn(in1,in2,target)
        after = f(in1,in2)
        print('Example (', in1, ',', in2, ',', target, '):', end=' ') 
        print('    f before learning: ', before, end=' ') 
        print('    f after learning : ', after)
    
def targetFunction(in1,in2):
    return sin(in1-3.0)*cos(in2) + normal(0,0.1)

def train(numSteps):
    for i in range(numSteps):
        in1 = random() * 6.0
        in2 = random() * 6.0
        target = targetFunction(in1,in2)
        learn(in1,in2,target)
    
def writeF(filename):
    fout = open(filename, 'w')
    steps = 50
    for i in range(steps):
        for j in range(steps):
            target = f(i * 6.0/steps, j * 6.0/steps)
            fout.write(repr(target) + ' ')
        fout.write('\n')
    fout.close()
        
def MSE(sampleSize):
    totalSE = 0.0
    for i in range(sampleSize):
        in1 = random() * 6.0
        in2 = random() * 6.0
        error = targetFunction(in1,in2) - f(in1,in2)
        totalSE = totalSE + error * error
    print('The estimated MSE: ', (totalSE / sampleSize))
    
def test2():
    train(20)
    writeF('f20')
    MSE(10000)
    for i in range(10):
        train(1000)
        MSE(10000)
    writeF('f10000')

#test1()
test2()

