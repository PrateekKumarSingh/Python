## Python
My [day-wise] Python Learning journey

## Resources
Python 3 Learning
* [Video] [Basics concepts](https://www.youtube.com/playlist?list=PLQVvvaa0QuDe8XSftW-RAxdo6OmaeL85M)
* [Video] [Machine Learning](https://www.youtube.com/playlist?list=PLQVvvaa0QuDfKTOs3Keq_kaG2P55YRn5v)
* [Link] [Selenium:Browser Automation](http://selenium-python.readthedocs.io/)

Python language reference 
* https://docs.python.org/3/reference/
* https://www.scaler.com/topics/python/

Python cheat sheets 
* https://github.com/PrateekKumarSingh/CheatSheets
* https://becominghuman.ai/cheat-sheets-for-ai-neural-networks-machine-learning-deep-learning-big-data-678c51b4b463

Python quick reference cards 
* http://www.cs.put.poznan.pl/csobaniec/software/python/py-qrc.html

## Daily Log
### Day 1
* Print function
* Comments
* Math module and mathematical operations
* Loop - For, While
* if, else, elif

### Day 2
* Functions
* Global and Local Variables
* Install Modules

### Day 3
* Importing modules
* Read, write, append files
* Class
* Getting User Input
* Statistics Module
    1. - Mean, Median, Standard deviation, Variance
* Tuples and Lists
* Launching WebBrowser
* Multi-Dimensional List
* Reading CSV files
* Try and Except

### Day 4
* Multiline print
* Dictionaries
    1. Create, delete and nested with lists
* Using Builtin functions
    1. Format(), int(), float(), round(), floor(), ceil()

### Day 5
* OS module
    1. Current working directory, new, remove directory and renaming files
* Sys Module
    1. Passing cmdline arguments
    2. Stderr, stdout 
    3. System-specific parameters and functions

### Day 6
* Basic URLLIB module usecases
    1. Requesting html response from a web url
    2. Encoding the url parameters    
* Sending web requests using URLLIB module with custom headers
* Dowloading JSON data from a URL

### Day 7
* Regular expressions
    1. Identifiers \d \D \w \W etc
    2. Modifiers + $ ^ etc
    3. Functions .findall() , .search() _

### Day 8
* List comprehensions and usecases
    1. Example of regular and list comprehension approach
    2. UseCase-1 : performing operations on each item in the list
    3. UseCase-2 : filtering elements of a list, eg - Null, empty strings, negative numbers etc
    4. UseCase-3 : list flattening - convert a 2D list to 1D list
* String manipulations
    1. Slicing a string
    2. .split() and .join()
    3. reversed()
    4. .strip() , .lstrip() , .rstrip()
    5. .rjust() .ljust(), .center()
    6. UseCase - Printing data in tabular format using .center()

### Day 9 
* MINI PROJECTS
    1. Dice Roll Simulator
    2. Guess the Number
    3. Hangman - Word guessing game

### Day 10
* Parsing websites
    1. Extracting data from withing the HTML tags of websites using reglar expression and web request

* TKinter module to make windows forms
    1. Basic form with labels and buttons
    2. Button onclick event handling
    3. Change label text dynamically

* MINI PROJECT

    4. Calclator GUI (Using Tkinter module)

### Day 11
* Tkinter module to create MENU in windows forms
* Add drop down menu items under each menu
* Add functionalities to drop down menu items
    1. File > Save [Opens a File Dialog box to save the file]
    2. File > Exit
    3. Tools > Show Image
    4. Tools > Show Text
* Threading Module
    1. Creating a thread
    2. Thread lock() , acquire() , release()  
    3. Queue
    
### Day 12
* CX Freeze module
    1. Define setup files
    2. Build executables (.exe) from Python scripts
* MatPlotLib module
    1. Loading coordinates from a csv file
    2. Plotting graph
    3. Scatter graph
    4. Bar graph
    5. Defining title, label, grid and legends
    6. Styling graphs

### Day 13
* Socket programming
    1. socket module
    2. socket.AF_INET (Address Family = IPv4)
    3. socket.SOCK_STREAM (Protocol = TCP) | socket.SOCK_DGRAM (Protocol = UDP) 
* Multi-threaded port scanner using socket programming
* Listen\Bind ports
* Client\Server system using socket programming

### Day 14
* Mini Project

    5. Chat System using Socket Programming
        * Telnet.exe clients can connect to a chat room on port 5555 of the server and start chat with other users
        * Multi-threaded client/server chat system
        * Broadcast [1-to-all] adnd private [1-to-1] messages
        * Chat room admin can Kick user(s) out of chat room
        * Poke users in a chat room
        * Ability to leave the chat room

### Day 15 
* Pandas module
    1. Convert dictionaries to Dataframes
    2. Slicing dataframes
    3. Making new columsn in dataframes
* SKLearn and Quandl module
    1. Get financial and economic datasets using Quandl
    2. Performing mathematical operations on dataframe columns
    3. Dataframe functions - .head() .tail() .shift() .fillna() dropna()
### Day 16    
* Train, test, predict data using Linear regression or Simple vector machine model
    1. Features vs labels
    2. Training and predicting using a model
        1. Prepare training data and split in 2 parts, ~80% to train ~20% to test [ model_selection.train_test_split() ]
        2. Define a classifier/model, like LinearRegression, SVM (Simple vector Machine) and then Train the classifier using .fit()
        3. Test accuracy of the classifier with respect to test data from step 1 [~20% of data]
        4. Predict -  Label = classifier.predict('Features')
            ![](https://github.com/PrateekKumarSingh/Python/blob/master/Python%20Machine%20Learning/SampleFiles/StockPrediction.png)
* Best fit line and how regression works
    1. What is slope(m) and intercept(b)
    2. Linear Regression = mX + b

### Day 17
* What are Squared error?
* Squared error vs Absolute errors
* R-Squared / Coeffcient of determination
* Classification with K-Nearest neighbor (KNN)

### Day 18
* Euclidean distance

    ![](https://github.com/PrateekKumarSingh/Python/blob/master/Python%20Machine%20Learning/SampleFiles/Euclidean_Distance.jpg)
* Making your own k-NN (k-Nearest Neighbor) algorithm in python
* Comparing the accuracy and confidence of your algorithm with SKLearn module's neighbors.KNeighborsClassifier()
* Accuracy vs confidence in k-NN algorithm

### Day 19
* SKLearn Support Vector Machine (SVM) classifier
* Making your own Support Vector Machine (SVM) algorithm in python [Courtesy: ![Harrison](https://pythonprogramming.net) ] 

### Day 20    
* Browser Automation using Selenium web driver with Python
* Python Web Scraping
    1. Using URLLib module and Regular expressions
    2. Using Beautiful Soup module   

### Day 21
* Soft Marging Support vector machines, kernels and CVXOPT
* SKLearn KMeans() classifier and clustering data sets

### Day 22
* Applying SKLearn KMeans classifier on Titanic data set to see if it can classify survivors and deads accurately
* Making your own custom K_Means() classifier algorithm in python
* Applying custom K_Means() algorithm on Titanic data set

## Folder/Files listing
```
.Root
|   README.md
|   
+---.vscode
|       launch.json
|       tasks.json
|       
+---Python Basics
|   |   01_Print_Function.py
|   |   02_Comment.py
|   |   03_Math.py
|   |   04_Variables.py
|   |   05_While_Loop.py
|   |   06_For_Loop.py
|   |   07_If_Else.py
|   |   08_Function.py
|   |   09_Global_Local_Variable.py
|   |   10_Install_Modules.py
|   |   11_Import_modules.py
|   |   12_Write_Append_Read_File.py
|   |   13_Class.py
|   |   14_User_Input.py
|   |   15_Statistics_Module.py
|   |   16_Tuples_List.py
|   |   17_Using_WebBrowser.py
|   |   18_MultiDimensional_List.py
|   |   19_Reading_CSV.py
|   |   20_Try_Except.py
|   |   21_Multiline_print.py
|   |   22_Dictionaries.py
|   |   23_Builtin_Functions.py
|   |   24_OS_Module.py
|   |   25_SYS_Module.py
|   |   26_URLLIB_Module_Basic.py
|   |   27_URLLIB_Module_Custom_Headers.py
|   |   28_URLLIB_Module_with_JSON.py
|   |   29_Regular_Expressions.py
|   |   30_List_Comprehensions.py
|   |   31_String_Manipulations.py
|   |   32_Parsing_Websites.py
|   |   33_TKINTER_Module.py
|   |   34_TKINTER_Add_Menu.py
|   |   35_Threading_Module.py
|   |   36_Threading_Advanced.py
|   |   37_CX_Freeze_and_Making_Exes.py
|   |   38_MatPlotLib_Module.py
|   |   39_Sockets_Programming.py
|   |   40_Multithreaded_Port_Scanner.py
|   |   41_Listen_And_Bind_Ports.py
|   |   42_Client_Server_Systems_With_Sockets.py
|   |   debug.log
|   |   
|   +---MiniProjects
|   |       1_Dice_Roll_Simulator.py
|   |       2_Guess_The_Number.py
|   |       3_Hangman.py
|   |       4_Calculator_GUI.py
|   |       5_Chat_System_On_Socket_Programming.py
|   |       readme.md
|   |       
|   +---Resources
|   |       Python_3_Tips.jpg
|   |       
|   \---SampleFiles
|           coordinates1.csv
|           coordinates2.csv
|           example.csv
|           GetHREF.py
|           picture.jpg
|           RequestWithHeader.txt
|           
+---Python Machine Learning
|   |   01_Pandas_Module.py
|   |   02_Sklearn_and_Quandl_module.py
|   |   03_Regression_Train_Test_Predict.py
|   |   04_Best_Fit_Line_and_Regression.py
|   |   05_Classification_with_SKLEARN_K_Nearest_Neighbor_Algorithm.py
|   |   06_KNN_Algorithm_using_Python.py
|   |   07_Test_Accuracy_of_kNN_Classifier_on_Cancer_Data.py
|   |   08_Classification_with_SKLEARN_Support_Vector_Machine_Algorithm.py
|   |   09_Creating_a_SVM_from_scratch.py
|   |   10_Soft_Margin_SVM_and_Kernels_with_CVXOPT.py
|   |   11_Clustering_DataSets_with_KMeans_Algorithm.py
|   |   12_KMeans_on_Titanic_DataSet.py
|   |   13_Creating_KMeans_from_scratch.py
|   |   14_Custom_KMeans_Algorithm_on_Titanic_dataset.py
|   |   
|   +---MiniProjects
|   |       01_Twitter.py
|   |       
|   +---Resources
|   |       Basic_Algebra.pdf
|   |       Python_For_DataScience.jpg_large
|   |       R_and_Python_DataScience.jpg
|   |       
|   \---SampleFiles
|           breast-cancer-wisconsin.txt
|           Euclidean_Distance.jpg
|           Intro to Regression.pdf
|           linearregression.pickle
|           StockPrediction.png
|           titanic.xls
|           
+---Python Selenium
|       01_Selenium_With_Python.py
|       
+---Python Web Scraping
|       01_Using_URLLIB_and_REGEX.py
|       02_Using_Beautiful_Soup.py

```
