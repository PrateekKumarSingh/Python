from cx_Freeze import setup, Executable 

setup(
    name = 'GetHREF', # name of the executable
    version = '0.3', # versions
    description = 'Parse URLs', 
    executables = [Executable('.\\samplefiles\\getHREF.py')] # file to compiled and wrapped as executable
)
