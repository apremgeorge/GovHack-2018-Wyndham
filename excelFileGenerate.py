import sys, traceback
import time
from datetime import datetime


if __name__ == '__main__':
    try:
        with open("/Users/ashish/Documents/Wyndham_Road_Crashes_Cleaned.csv") as f:
            listAllLines = f.read().splitlines()

        timeAppender = datetime.now().strftime("%Y-%m-%d-%H%M%S")

        filterString = ",ANY MANOEUVRE "
        listFilteredLines = list(filter(lambda k: filterString in k, listAllLines))

        with open("/Users/ashish/Documents/Wyndham_Road_Crashes_Cleaned_"+timeAppender+".csv", "w") as f:
            f.write(listAllLines[0]+"\n")
            for line in listFilteredLines:
                f.write(line+"\n")

    except Exception:
        print("Error")