##Python compress

fp = "testFile.py";
f = open ( fp, "rb" );
fd = f.read();
f.close();
del f;
fd = fd.decode();
fd = fd.split("\r\n");
i = 0;
usualIndent = False;

while i != len(fd)-1:
    indent = 0;
    for x in fd[i]:
        if x == " ":
            indent += 1;
        else:
            break;
    
    fd[i] = str ( indent ) + fd[i][indent:];
    i += 1;
    
for x in fd:
    print ( x );
