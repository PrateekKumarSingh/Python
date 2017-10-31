String = 'my name is prateek kumar singh\nI love Python'

savefile = open('Test.txt','w') # mode =  'w' (WRITE)
savefile.write(String)
savefile.close()

append = '\nI used to Powershell'

Appendfile = open('test.txt','a') # mode =  'a' (APPEND)
Appendfile.write(append)
Appendfile.close()


readme = open('test.txt','r').read() # mode =  'r' (READ)
print(readme)
