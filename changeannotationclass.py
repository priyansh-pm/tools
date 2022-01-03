import os

changefrom = 0
changeto = 1

readdir = os.listdir('mores/')
for z in range(0,len(readdir)):
    f = open("mores/"+readdir[z],'r')
    all_lines_in_file = f.readlines()
    file_length = len(all_lines_in_file)
    t = open('smores/'+readdir[z],'w')
    for i in range(0,file_length):
        linetext = all_lines_in_file[i]
        linelength = len(linetext)
        linearray = linetext.split(' ')
        if linearray[0] == str(changefrom):
            linearray[0] = str(changeto)
        elif linearray[0] == str(changeto):
            linearray[0] = str(changefrom)
        writingtext = ' '.join(linearray)
        print(writingtext)
        t.write(writingtext)
    t.close
    f.close()