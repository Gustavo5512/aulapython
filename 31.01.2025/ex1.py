vetoridade= [ ]
soma=0 
for i in range(0,10):
    vetoridade.append( int(input('Digite a idade')))
    soma+=vetoridade[i]

media=soma/vetoridade.__len__( )

for i in range(0,  vetoridade.__len__( )):
    print('idade',vetoridade[i])
print('media', media)