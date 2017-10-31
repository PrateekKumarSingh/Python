x = [2,3,4,6,73,6,87,7] # one dimensional list
print(x[4]) # single [] bracket to refer the index

x = [2,3,[1,2,3,4],6,73,6,87,7] # two dimensional list
print(x[2][1]) # using  double [] to refer the index of list

x = [[2,3,[8,7,6,5,4,3,2,1]],[1,2,3,4],6,73,6,87,7] # three dimensional list
print(x[0][2][2]) # using triple [] to refer the index of the three dimensional list

# you can also define a 3-D list in following manner, which is comparatively easy to visualize and understand
x = [
        [   2,
            3,
            [8,7,6,5,4,3,2,1]
        ],
        [   1,
            2,
            [5,6,7,8,9,12,34,5,3,2],
            4
        ],
            6,
            73,
            6,
            87,
            7
    ] 


print(x[1][2][-1])