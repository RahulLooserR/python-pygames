from time import strftime, localtime

dtime = strftime ("%y-%m-%d_%H:%M:%S", localtime())
print (dtime)
fileid = ['FILEID']
fileid += "_" + dtime

print (fileid)
