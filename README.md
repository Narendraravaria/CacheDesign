# CacheDesign
This Repository contains Python script require to run the project

To run this project you need SimpleScalar Simulator and Benchmarks.
SimpleScalr setup:-
1. Download SimpleScalar 3.0 from www.simplescalar.com 
2. Extract it by using command- tar xvzf simplesim-3v0e.tgz
3. To install SmpleScalar follow steps below
    -cd simplesim-3.0
    -make
4. Verify that it is working properly by typing command 
   ./sim-cache tests-alpha/bin/test-math
   if you will get output as below that means your simulator is installed and working properly
   -1e-17 == -1e-17 Worked!

Benchmark Setup:-
1. Download benchmarks from http://www.eecs.umich.edu/~taustin/eecs573_public/instruct-progs.tar.gz
2. Extract benchmark in the simplesim-3.0 directory (i.e. both benchmark ad simplesim-3.0 folder should be in the same parent folder say SimpleScalr)
3. Test the Bechmarks (Read the README file present in Benchmark folder )
4. 
Now to Run all python script present in this repository 
1. Dowload .py file and copy paste in the simplesim-3.0 folder (except outputfile.py) 
2. creat output empty folder in simplesim-3,0 folder which cotains all the data extracted from output get by running above python script (except outputfile.py)
3. run .py file except outputfile.py one by one
4. Once you get all output then run outputfile.py to calculate CPI and Cost of design

