numTilings = 4
    
def tilecode(in1,in2,tileIndices):
    " write your tilecoder here (5 lines or so)"
    offset1 = .2125/numTilings
    offset2 = .0175/numTilings
    in1=in1+1.2
    in2=in2+.07
    tiling=0
    for i in range(numTilings):
        x,y=in1//.2125,in2//.0175
        tileIndices[i]=y*9+x+tiling
        tiling+=81
        in1,in2=in1+offset1,in2+offset2
    
    
    
def printTileCoderIndices(in1,in2):
    tileIndices = [-1]*numTilings
    tilecode(in1,in2,tileIndices)
    print('Tile indices for input (',in1,',',in2,') are : ', tileIndices)

#printTileCoderIndices(.49,0)
#printTileCoderIndices(4.0,2.0)
#printTileCoderIndices(5.99,5.99)
#printTileCoderIndices(4.0,2.1)


