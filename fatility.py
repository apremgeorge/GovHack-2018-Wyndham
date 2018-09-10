import rpy2.robjects as robjects

def fatilityMethod(timing, accidentTime, geometry, alcoholTime, speedZone, nodeType, latitude, longitude):
    returnValue = "Error"
    try:
        rFormulae = (""" 
        Wyn_Crash <- read.csv("/Users/ashish/Documents/Wyndham_Road_Crashes_Cleaned.csv")

        mod.fit.Fatal<-glm(formula = FATALITY ~ (ALCOHOLTIME + ACCIDENT_TIME + LIGHT_CONDITION 
        + ROAD_GEOMETRY + SPEED_ZONE + NODE_TYPE ), family = binomial(link = logit), data = Wyn_Crash)
        
        predict.Fatal <- data.frame(ALCOHOLTIME = \""""+alcoholTime+"""\",
        ACCIDENT_TIME = \""""+accidentTime+"""\",
        LIGHT_CONDITION = \""""+timing+"""\",
        ROAD_GEOMETRY = \""""+geometry+"""\",
        SPEED_ZONE = \""""+speedZone+"""\",
        NODE_TYPE = \""""+nodeType+"""\")
        
        predict(object = mod.fit.Fatal, newdata = predict.Fatal, type = "response")*100

        """)
        print ("FATALITY Formulae: "+rFormulae)

        rexecution = robjects.r(rFormulae)
        countedValue = rexecution.rx2(1)[0]
        print("Calculated Value: "+str(countedValue))
        roundedValue = round(countedValue, 2)
        returnValue = str(roundedValue) + " %"

    except Exception:
        returnValue = "Error"

    return returnValue