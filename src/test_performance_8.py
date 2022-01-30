from os import error
from re import M
import pytest
import time
import test_system as ts

def test_ExitAfterNewGameFirstMove2_Fail_benchmark(monkeypatch):
    runtimings = {}
    totaltime = 0
    loop = [50,100,300,1000]
    averagetimes = {}
    maxtimes = {}
    totaltimes = []
    count = 0
    for x in loop:
        for i in range(x):
            start_time = time.time()
            timetaken = ts.test_ExitAfterNewGameFirstMove2_Fail(monkeypatch)
            runtimings[i]= timetaken
            totaltime += timetaken
        averagetime = totaltime/100
        maxtime = max(runtimings.values())
        averagetimes[count] = averagetime
        totaltimes.append(totaltime)
        maxtimes[count] = maxtime
        count += 1
       
    print("\nPerformance Test Results for Exit After New Game First Move Random Building 2 Test (Wrong Inputs) Functionality:")
    print("------------------------------------------------------------------")
    for y in range(count):
        print("Results for " + str(loop[y]) + " times ran:\n")
        print("Total time elapsed: " + str(totaltimes[y]) + " seconds")
        print("Average time taken: " + str(averagetimes[y]) + " seconds")
        print("Longest run time: " + str(maxtimes[y]) + " seconds")
        print("------------------------------------------------------------------")