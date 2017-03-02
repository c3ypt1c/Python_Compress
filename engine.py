##Python compress
from fractions import gcd;

fp = "testFile.py";
f = open ( fp, "rb" );
fd = f.read();
f.close();
del f;
fd = fd.decode();
fd = fd.split("\r\n");
fdi = [];

for x in fd:
    indent = 0;
    for y in x:
        if y == " ":
            indent+=1;
        else:
            break;
    fdi.append(indent);

temp = fdi[:];

while True:
    try:
        temp.remove(0);
    except:
        break;
    
fdgcf = gcd(max(fdi), min(temp)); ##Obviously not going to work because stuff

newfdi = [ x / fdgcf * 2 for x in fdi ]

    

del temp;



