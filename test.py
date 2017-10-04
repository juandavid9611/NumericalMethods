picture = "       .......                      |     ..       .                     |......          .                   |.....            .                  |     ..           .                 |       .           ........         |     ..                   ......... |    .                           ... |   .                           .    |   .                           .    |    .                         .     |     ...                   ...      |        ..................."         |  

picturebyLines = picture.split('|')

for line in picturebyLines:
    print (line)

posx = []
posy = []

for i in range(0, len(picturebyLines[0])-1):
  pos = 0
  for j in picturebyLines:
    if( j[ i ] == '.' ):
      posx.append(i)
      posy.append(pos)
      break
    pos+=1

print(posx)
print(posy)
