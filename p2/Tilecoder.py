numTilings = 8
    
def tilecode(in1,in2,tileIndices):
    " write your tilecoder here (5 lines or so)"
    offset = .6/numTilings
    tiling=0
    for i in range(numTilings):
        x,y=in1//.6,in2//.6
        tileIndices[i]=y*11+x+tiling
        tiling+=121
        in1,in2=in1+offset,in2+offset
    
    
    
def printTileCoderIndices(in1,in2):
    tileIndices = [-1]*numTilings
    tilecode(in1,in2,tileIndices)
    print('Tile indices for input (',in1,',',in2,') are : ', tileIndices)

#printTileCoderIndices(0.1,0.1)
#printTileCoderIndices(4.0,2.0)
#printTileCoderIndices(5.99,5.99)
#printTileCoderIndices(4.0,2.1)


