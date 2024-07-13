#Import relevant python software packages
import tkinter as tk 

#Window & title creation
window = tk.Tk()
window.title("Severe Weather Risk Calculator")

#Canvas area creation
canvasArea = tk.Canvas(window, width = 1500, height = 1000)
canvasArea.pack() 

#Titles & Important Note(s)
applicationTitle = tk.Label(window, text = "Thunderstorm Risk Level Calculator")
applicationTitle.config(font = ("calibri", 17, "bold"))
canvasArea.create_window(700, 20, window = applicationTitle)

lowTropLapseRateTitle = tk.Label(window, text = "Low Troposphere Lapse Rate Calculation")
lowTropLapseRateTitle.config(font = ("calibri", 13, "bold"))
canvasArea.create_window(170, 60, window = lowTropLapseRateTitle)

midTropLapseRateTitle = tk.Label(window, text = "Mid Troposphere Lapse Rate Calculation")
midTropLapseRateTitle.config(font = ("calibri", 13, "bold"))
canvasArea.create_window(690, 60, window = midTropLapseRateTitle)

kIndexTTITitle = tk.Label(window, text = "K-Index & Total Totals Index Calculation")
kIndexTTITitle.config(font = ("calibri", 13, "bold"))
canvasArea.create_window(1190, 60, window = kIndexTTITitle)

lowTropResultsTitle = tk.Label(window, text = "Low Troposphere Results")
lowTropResultsTitle.config(font = ("calibri", 13, "bold"))
canvasArea.create_window(170, 330, window = lowTropResultsTitle)

midTropResultsTitle = tk.Label(window, text = "Mid Troposphere Results")
midTropResultsTitle.config(font = ("calibri", 13, "bold"))
canvasArea.create_window(690, 330, window = midTropResultsTitle)

kIndexResultsTitle = tk.Label(window, text = "K-Index & TTI Results")
kIndexResultsTitle.config(font = ("calibri", 13, "bold")) 
canvasArea.create_window(1190, 330, window = kIndexResultsTitle)

riskLevelTitle = tk.Label(window, text = "Thunderstorm Risk")
riskLevelTitle.config(font = ("calibri", 13, "bold"))
canvasArea.create_window(530, 685, window = riskLevelTitle)

severeRiskLevelTitle = tk.Label(window, text = "Severe Thunderstorm Risk")
severeRiskLevelTitle.config(font = ("calibri", 13, "bold"))
canvasArea.create_window(875, 685, window = severeRiskLevelTitle)

importantNote = tk.Label(window, text = "(NOTE: Please clear your current results or certain or all content if you wish to compute new results)")
importantNote.config(font = ("calibri", 12, "bold"))
canvasArea.create_window(710, 880, window = importantNote)






#Low Troposphere Lapse Rate Info 

lowTropStartPressure = tk.Entry(window, justify = "right")
canvasArea.create_window(280, 100, window = lowTropStartPressure)

lowTropEndPressure = tk.Entry(window, justify = "right")
canvasArea.create_window(280, 140, window = lowTropEndPressure)

lowTropStartTemp = tk.Entry(window, justify = "right")
canvasArea.create_window(280, 180, window = lowTropStartTemp)

lowTropEndTemp = tk.Entry(window, justify = "right")
canvasArea.create_window(280, 220, window = lowTropEndTemp)

lowTropAltitudeGain = tk.Entry(window, justify = "right")
canvasArea.create_window(280, 360, window = lowTropAltitudeGain)

lowTropLapseRateCFT = tk.Entry(window, justify = "right")
canvasArea.create_window(280, 400, window = lowTropLapseRateCFT)

lowTropLapseRateC1000FT = tk.Entry(window, justify = "right")
canvasArea.create_window(280, 440, window = lowTropLapseRateC1000FT)

lowTropLapseRateCKM = tk.Entry(window, justify = "right")
canvasArea.create_window(280, 480, window = lowTropLapseRateCKM)

#Labels
lowTropStartPressureLabel = tk.Label(window, text = "Low Trop Starting Pressure (mb): ")
lowTropStartPressureLabel.config(font = ("calibri", 10))
canvasArea.create_window(100, 100, window = lowTropStartPressureLabel)

lowTropEndPressureLabel = tk.Label(window, text = "Low Trop Ending Pressure (mb): ")
lowTropEndPressureLabel.config(font = ("calibri", 10))
canvasArea.create_window(100, 140, window = lowTropEndPressureLabel)

lowTropStartTempLabel = tk.Label(window, text = "Low Trop Starting Temperature (C): ")
lowTropStartTempLabel.config(font = ("calibri", 10))
canvasArea.create_window(100, 180, window = lowTropStartTempLabel)

lowTropEndTempLabel = tk.Label(window, text = "Low Trop Ending Temperature (C): ")
lowTropEndTempLabel.config(font = ("calibri", 10))
canvasArea.create_window(100, 220, window = lowTropEndTempLabel)

lowTropAltitudeGainLabel = tk.Label(window, text = "Low Trop Altitude Gain (Ft): ")
lowTropAltitudeGainLabel.config(font = ("calibri", 10))
canvasArea.create_window(80, 360, window = lowTropAltitudeGainLabel)

lowTropLapseRateCFTLabel = tk.Label(window, text = "Lapse Rate (C/ft): ")
lowTropLapseRateCFTLabel.config(font = ("calibri", 10))
canvasArea.create_window(90, 400, window = lowTropLapseRateCFTLabel)

lowTropLapseRateC1000FTLabel = tk.Label(window, text = "Lapse Rate (C/1000ft): ")
lowTropLapseRateC1000FTLabel.config(font = ("calibri", 10))
canvasArea.create_window(90, 440, window = lowTropLapseRateC1000FTLabel)

lowTropLapseRateCKMLabel = tk.Label(window, text = "Lapse Rate (C/km): ")
lowTropLapseRateCKMLabel.config(font = ("calibri", 10, "bold"))
canvasArea.create_window(90, 480, window = lowTropLapseRateCKMLabel)






#Mid Troposphere Lapse Rate Info

midTropStartPressure = tk.Entry(window, justify = "right")
canvasArea.create_window(800, 100, window = midTropStartPressure)

midTropEndPressure = tk.Entry(window, justify = "right")
canvasArea.create_window(800, 140, window = midTropEndPressure)

midTropStartTemp = tk.Entry(window, justify = "right")
canvasArea.create_window(800, 180, window = midTropStartTemp)

midTropEndTemp = tk.Entry(window, justify = "right")
canvasArea.create_window(800, 220, window = midTropEndTemp)

midTropAltitudeGain = tk.Entry(window, justify = "right")
canvasArea.create_window(800, 360, window = midTropAltitudeGain)

midTropLapseRateCFT = tk.Entry(window, justify = "right")
canvasArea.create_window(800, 400, window = midTropLapseRateCFT)

midTropLapseRateC1000FT = tk.Entry(window, justify = "right")
canvasArea.create_window(800, 440, window = midTropLapseRateC1000FT)

midTropLapseRateCKM = tk.Entry(window, justify = "right")
canvasArea.create_window(800, 480, window = midTropLapseRateCKM)

#Labels

midTropStartPressureLabel = tk.Label(window, text = "Mid Trop Starting Pressure (mb): ")
midTropStartPressureLabel.config(font = ("calibri", 10))
canvasArea.create_window(600, 100, window = midTropStartPressureLabel)

midTropEndPressureLabel = tk.Label(window, text = "Mid Trop Ending Pressure (mb): ")
midTropEndPressureLabel.config(font = ("calibri", 10))
canvasArea.create_window(600, 140, window = midTropEndPressureLabel)

midTropStartTempLabel = tk.Label(window, text = "Mid Trop Starting Temperature (C): ")
midTropStartTempLabel.config(font = ("calibri", 10))
canvasArea.create_window(600, 180, window = midTropStartTempLabel)

midTropEndTempLabel = tk.Label(window, text = "Mid Trop Ending Temperature (C): ")
midTropEndTempLabel.config(font = ("calibri", 10))
canvasArea.create_window(600, 220, window = midTropEndTempLabel)

midTropAltitudeGainLabel = tk.Label(window, text = "Mid Trop Altitude Gain (Ft): ")
midTropAltitudeGainLabel.config(font = ("calibri", 10))
canvasArea.create_window(600, 360, window = midTropAltitudeGainLabel)

midTropLapseRateCFTLabel = tk.Label(window, text = "Lapse Rate (C/ft): ")
midTropLapseRateCFTLabel.config(font = ("calibri", 10))
canvasArea.create_window(600, 400, window = midTropLapseRateCFTLabel)

midTropLapseRateC1000FTLabel = tk.Label(window, text = "Lapse Rate (C/1000ft): ")
midTropLapseRateC1000FTLabel.config(font = ("calibri", 10))
canvasArea.create_window(600, 440, window = midTropLapseRateC1000FTLabel)

midTropLapseRateCKMLabel = tk.Label(window, text = "Lapse Rate (C/km): ")
midTropLapseRateCKMLabel.config(font = ("calibri", 10, "bold"))
canvasArea.create_window(600, 480, window = midTropLapseRateCKMLabel)






#K-Index & TTI Info

kIndex = tk.Entry(window, justify = "right")
canvasArea.create_window(1250, 360, window = kIndex)

temp850 = tk.Entry(window, justify = "right")
canvasArea.create_window(1250, 100, window = temp850)

temp500 = tk.Entry(window, justify = "right")
canvasArea.create_window(1250, 130, window = temp500)

dP850 = tk.Entry(window, justify = "right")
canvasArea.create_window(1250, 160, window = dP850) 

temp700 = tk.Entry(window, justify = "right")
canvasArea.create_window(1250, 190, window = temp700)

dP700 = tk.Entry(window, justify = "right")
canvasArea.create_window(1250, 220, window = dP700)

#Labels 

temp850Label = tk.Label(window, text = "850 Temp. (C): ")
temp850Label.config(font = ("calibri", 10))
canvasArea.create_window(1100, 100, window = temp850Label)

temp500Label = tk.Label(window, text = "500 Temp. (C): ")
temp500Label.config(font = ("calibri", 10))
canvasArea.create_window(1100, 130, window = temp500Label)

dP850Label = tk.Label(window, text = "850 Td (C): ")
dP850Label.config(font = ("calibri", 10))
canvasArea.create_window(1100, 160, window = dP850Label)

temp700Label = tk.Label(window, text = "700 Temp. (C): ")
temp700Label.config(font = ("calibri", 10))
canvasArea.create_window(1100, 190, window = temp700Label)

dP700Label = tk.Label(window, text = "700 Td (C): ")
dP700Label.config(font = ("calibri", 10))
canvasArea.create_window(1100, 220, window = dP700Label)

kIndexLabel = tk.Label(window, text = "K-Index: ")
kIndexLabel.config(font = ("calibri", 10, "bold"))
canvasArea.create_window(1100, 360, window = kIndexLabel)






#Total Totals Index

TTI = tk.Entry(window, justify = "right")
canvasArea.create_window(1250, 400, window = TTI)

#Label

TTILabel = tk.Label(window, text = "Total Totals Index: ")
TTILabel.config(font = ("calibri", 10, "bold"))
canvasArea.create_window(1100, 400, window = TTILabel)






#Risk Level

riskLevel = tk.Entry(window, justify = "center")
canvasArea.create_window(560, 735, window = riskLevel)

#Labels

riskLevelLabel = tk.Label(window, text = "Risk Level: ")
riskLevelPercentageLabel = tk.Label(window, text = "%")

riskLevelLabel.config(font = ("calibri", 10, "bold"))
riskLevelPercentageLabel.config(font = ("calibri", 11, "bold"))

canvasArea.create_window(460, 735, window = riskLevelLabel)
canvasArea.create_window(630, 735, window = riskLevelPercentageLabel)






#Severe Risk Level 

severeRiskLevel = tk.Entry(window, justify = "center")
canvasArea.create_window(920, 735, window = severeRiskLevel)

#Labels 

severeRiskLevelLabel = tk.Label(window, text = "Severe Risk Level: ")
sevRiskLevelPercentageLabel = tk.Label(window, text = "%")

severeRiskLevelLabel.config(font = ("calibri", 10, "bold"))
sevRiskLevelPercentageLabel.config(font = ("calibri", 11, "bold"))

canvasArea.create_window(800, 735, window = severeRiskLevelLabel)
canvasArea.create_window(990, 735, window = sevRiskLevelPercentageLabel)






#Back End Lapse Rate, K-Index, TTI Computational Functions & Interactive Buttons
def ComputeLowTropResults():
    a = lowTropStartPressure.get()
    b = lowTropEndPressure.get()

    lowTropAltitudeGain.insert(0, round(((1 - ((float(b) / 1013.25) ** 0.190284) * 145366.45) - (1 - ((float(a) / 1013.25) ** 0.190284) * 145366.45)), 3))

    x = lowTropStartTemp.get()
    y = lowTropEndTemp.get()
    z = lowTropAltitudeGain.get()

    lowTropLapseRateCFT.insert(0, round(-1 * ((float(y) - float(x)) / float(z)), 5))

    lowTropLapseRateC1000FT.insert(0, round(-1 * ((float(y) - float(x)) / float(z)) * 1000, 5))

    lowTropLapseRateCKM.insert(0, round(-1 * ((float(y) - float(x)) / float(z)) * 3280.84, 5))

computeLowTropButton = tk.Button(text = "Compute Low Troposphere Results", command = ComputeLowTropResults, bg = "red", fg = "white", font = ("calibri", 10, "bold"), width = 28, cursor = "X_cursor")
canvasArea.create_window(170, 275, window = computeLowTropButton)

def ComputeMidTropResults():
    a = midTropStartPressure.get()
    b = midTropEndPressure.get()

    midTropAltitudeGain.insert(0, round(((1 - ((float(b) / 1013.25) ** 0.190284) * 145366.45) - (1 - ((float(a) / 1013.25) ** 0.190284) * 145366.45)), 3))

    x = midTropStartTemp.get()
    y = midTropEndTemp.get()
    z = midTropAltitudeGain.get()

    midTropLapseRateCFT.insert(0, -1 * round(((float(y) - float(x)) / float(z)), 5))

    midTropLapseRateC1000FT.insert(0, -1 * round(((float(y) - float(x)) / float(z)) * 1000, 5))

    midTropLapseRateCKM.insert(0, -1 * round(((float(y) - float(x)) / float(z)) * 3280.84, 5))

computeMidTropButton = tk.Button(text = "Compute Mid Troposphere Results", command = ComputeMidTropResults, bg = "blue", fg = "white", font = ("calibri", 10, "bold"), width = 28, cursor = "X_cursor")
canvasArea.create_window(690, 275, window = computeMidTropButton)

def ComputeKIndexTTI():
    a = temp850.get()
    b = temp500.get()
    c = dP850.get()
    d = temp700.get()
    e = dP700.get()

    kIndex.insert(0, (float(a) - float(b)) + float(c) - (float(d) - float(e)))

    TTI.insert(0, (float(a) + float(c)) - (2 * float(b)))

computeKIndexTTIButton = tk.Button(text = "Compute K-Index & TTI Results", command = ComputeKIndexTTI, bg = "green", fg = "white", font = ("calibri", 10, "bold"), width = 25, cursor = "X_cursor")
canvasArea.create_window(1190, 275, window = computeKIndexTTIButton)

def DeleteLowTropContent():
    lowTropAltitudeGain.delete(first = 0, last = 20)
    lowTropLapseRateCFT.delete(first = 0, last = 20)
    lowTropLapseRateC1000FT.delete(first = 0, last = 20)
    lowTropLapseRateCKM.delete(first = 0, last = 20)

    lowTropStartPressure.delete(first = 0, last = 20)
    lowTropEndPressure.delete(first = 0, last = 20)
    lowTropStartTemp.delete(first = 0, last = 20)
    lowTropEndTemp.delete(first = 0, last = 20)

clearLowTropButton = tk.Button(text = "Clear Low Troposphere Content", command = DeleteLowTropContent, bg = "yellow", fg = "black", font = ("calibri", 10, "bold"), width = 25, cursor = "X_cursor")
canvasArea.create_window(170, 570, window = clearLowTropButton)

def DeleteLowTropResults():
    lowTropAltitudeGain.delete(first = 0, last = 20)
    lowTropLapseRateCFT.delete(first = 0, last = 20)
    lowTropLapseRateC1000FT.delete(first = 0, last = 20)
    lowTropLapseRateCKM.delete(first = 0, last = 20)

clearLowTropResultsButton = tk.Button(text = "Clear Low Troposphere Results", command = DeleteLowTropResults, bg = "yellow", fg = "black", font = ("calibri", 10, "bold"), width = 25, cursor = "X_cursor")
canvasArea.create_window(170, 530, window = clearLowTropResultsButton)

def DeleteMidTropContent():
    midTropAltitudeGain.delete(first = 0, last = 20)
    midTropLapseRateCFT.delete(first = 0, last = 20)
    midTropLapseRateC1000FT.delete(first = 0, last = 20)
    midTropLapseRateCKM.delete(first = 0, last = 20)

    midTropStartPressure.delete(first = 0, last = 20)
    midTropEndPressure.delete(first = 0, last = 20)
    midTropStartTemp.delete(first = 0, last = 20)
    midTropEndTemp.delete(first = 0, last = 20)

clearMidTropButton = tk.Button(text = "Clear Mid Troposphere Content", command = DeleteMidTropContent, bg = "yellow", fg = "black", font = ("calibri", 10, "bold"), width = 25, cursor = "X_cursor")
canvasArea.create_window(690, 570, window = clearMidTropButton)

def DeleteMidTropResults():
    midTropAltitudeGain.delete(first = 0, last = 20)
    midTropLapseRateCFT.delete(first = 0, last = 20)
    midTropLapseRateC1000FT.delete(first = 0, last = 20)
    midTropLapseRateCKM.delete(first = 0, last = 20)

clearMidTropResultsButton = tk.Button(text = "Clear Mid Troposphere Results", command = DeleteMidTropResults, bg = "yellow", fg = "black", font = ("calibri", 10, "bold"), width = 25, cursor = "X_cursor")
canvasArea.create_window(690, 530, window = clearMidTropResultsButton)

def DeleteKIndexTTIContent():
    temp850.delete(first = 0, last = 20)
    temp500.delete(first = 0, last = 20)
    dP850.delete(first = 0, last = 20)
    temp700.delete(first = 0, last = 20)
    dP700.delete(first = 0, last = 20)

    kIndex.delete(first = 0, last = 20)
    TTI.delete(first = 0, last = 20)

clearKIndexTTIButton = tk.Button(text = "Clear K-Index & TTI Content", command = DeleteKIndexTTIContent, bg = "yellow", fg = "black", font = ("calibri", 10, "bold"), width = 25, cursor = "X_cursor")
canvasArea.create_window(1190, 570, window = clearKIndexTTIButton)

def DeleteKIndexTTIResults():
    kIndex.delete(first = 0, last = 20)
    TTI.delete(first = 0, last = 20)

clearKIndexTTIResultsButton = tk.Button(text = "Clear K-Index & TTI Results", command = DeleteKIndexTTIResults, bg = "yellow", fg = "black", font = ("calibri", 10, "bold"), width = 25, cursor = "X_cursor")
canvasArea.create_window(1190, 530, window = clearKIndexTTIResultsButton)

def DeleteAll():
    lowTropAltitudeGain.delete(first = 0, last = 20)
    lowTropLapseRateCFT.delete(first = 0, last = 20)
    lowTropLapseRateC1000FT.delete(first = 0, last = 20)
    lowTropLapseRateCKM.delete(first = 0, last = 20)

    lowTropStartPressure.delete(first = 0, last = 20)
    lowTropEndPressure.delete(first = 0, last = 20)
    lowTropStartTemp.delete(first = 0, last = 20)
    lowTropEndTemp.delete(first = 0, last = 20)

    midTropAltitudeGain.delete(first = 0, last = 20)
    midTropLapseRateCFT.delete(first = 0, last = 20)
    midTropLapseRateC1000FT.delete(first = 0, last = 20)
    midTropLapseRateCKM.delete(first = 0, last = 20)

    midTropStartPressure.delete(first = 0, last = 20)
    midTropEndPressure.delete(first = 0, last = 20)
    midTropStartTemp.delete(first = 0, last = 20)
    midTropEndTemp.delete(first = 0, last = 20)

    temp850.delete(first = 0, last = 20)
    temp500.delete(first = 0, last = 20)
    dP850.delete(first = 0, last = 20)
    temp700.delete(first = 0, last = 20)
    dP700.delete(first = 0, last = 20)

    kIndex.delete(first = 0, last = 20)
    TTI.delete(first = 0, last = 20)

    riskLevel.delete(first = 0, last = 20)
    severeRiskLevel.delete(first = 0, last = 20)

clearAllButton = tk.Button(text = "Clear All Content", command = DeleteAll, bg = "yellow", fg = "black", font = ("calibri", 10, "bold"), width = 15, cursor = "X_cursor")
canvasArea.create_window(690, 835, window = clearAllButton)

def ComputeRiskLevel():
    x = lowTropLapseRateCKM.get()
    y = midTropLapseRateCKM.get()
    z = kIndex.get()

    if float(x) <= 6.5 and float(y) <= 6.5 and float(z) <= 20:
        riskLevel.insert(0, 0)
    elif 6.5 <= float(x) <= 8.0 and float(y) <= 6.5 and 25 <= float(z) <= 30:
        riskLevel.insert(0, 50)
    elif float(x) <= 6.5 and float(y) <= 6.5 and 30 <= float(z) <= 40:
        riskLevel.insert(0, 80)
    elif float(x) <= 6.5 and float(y) <= 6.5 and float(z) >= 40:
        riskLevel.insert(0, 90)
    elif 6.5 <= float(x) <= 8.0 and float(y) <= 6.5 and 30 <= float(z) <= 40:
        riskLevel.insert(0, 90)
    elif 6.5 <= float(x) <= 8.0 and 6.5 <= float(y) <= 8.0 and 30 <= float(z) <= 40:
        riskLevel.insert(0, 90)
    elif 6.5 <= float(x) <= 8.0 and float(y) <= 6.5 and float(z) >= 40:
        riskLevel.insert(0, 100)
    elif 8.0 <= float(x) <= 9.5 and float(y) <= 6.5 and float(z) >= 40:
        riskLevel.insert(0, 100)
    elif 8.0 <= float(x) <= 9.5 and 6.5 <= float(y) <= 8.0 and 30 <= float(z) <= 40:
        riskLevel.insert(0, 100)
    elif float(x) <= 6.5 and 6.5 <= float(y) <= 8.0 and float(z) >= 40:
        riskLevel.insert(0, 100)
    elif float(x) >= 9.5 and float(y) >= 9.5 and 30 <= float(z) <= 40:
        riskLevel.insert(0, 100)
    elif float(x) >= 9.5 and float(y) >= 9.5 and float(z) >= 40:
        riskLevel.insert(0, 100)

computeRiskLevelButton = tk.Button(text = "Compute Risk Level", command = ComputeRiskLevel, bg = "purple", fg = "white", font = ("calibri", 10, "bold"), width = 18, cursor = "X_cursor")
canvasArea.create_window(530, 785, window = computeRiskLevelButton)

def ComputeSevereRiskLevel():
    x = lowTropLapseRateCKM.get()
    y = midTropLapseRateCKM.get()
    z = TTI.get()

    if float(x) <= 6.5 and float(y) <= 6.5 and float(z) <= 45:
        severeRiskLevel.insert(0, 0)
    elif float(x) <= 6.5 and float(y) <= 6.5 and 45 <= float(z) <= 50:
        severeRiskLevel.insert(0, 5)
    elif float(x) <= 6.5 and float(y) <= 6.5 and 50 <= float(z) <= 55:
        severeRiskLevel.insert(0, 10)
    elif 6.5 <= float(x) <= 8.0 and float(y) <= 6.5 and 45 <= float(z) <= 50:
        severeRiskLevel.insert(0, 20)
    elif 6.5 <= float(x) <= 8.0 and float(y) <= 6.5 and 50 <= float(z) <= 55:
        severeRiskLevel.insert(0, 20)
    elif float(x) <= 6.5 and 6.5 <= float(y) <= 8.0 and 45 <= float(z) <= 50:
        severeRiskLevel.insert(0, 20)
    elif 6.5 <= float(x) <= 8.0 and 6.5 <= float(y) <= 8.0 and 45 <= float(z) <= 50:
        severeRiskLevel.insert(0, 25)
    elif 6.5 <= float(x) <= 8.0 and float(y) <= 6.5 and 45 <= float(z) <= 50:
        severeRiskLevel.insert(0, 25)
    elif float(x) <= 6.5 and 6.5 <= float(y) <= 8.0 and 50 <= float(z) <= 55:
        severeRiskLevel.insert(0, 30)
    elif 6.5 <= float(x) <= 8.0 and 6.5 <= float(y) <= 8.0 and 50 <= float(z) <= 55:
        severeRiskLevel.insert(0, 55)
    elif 8.0 <= float(x) <= 9.5 and float(y) <= 6.5 and 50 <= float(z) <= 55:
        severeRiskLevel.insert(0, 70)
    elif 8.0 <= float(x) <= 9.5 and 8.0 <= float(y) <= 9.5 and 45 <= float(z) <= 50:
        severeRiskLevel.insert(0, 85)
    elif float(x) >= 9.5 and float(y) >= 9.5 and 50 <= float(z) <= 55:
        severeRiskLevel.insert(0, 90)
    elif float(x) >= 9.5 and float(y) >= 9.5 and 55 <= float(z) <= 60:
        severeRiskLevel.insert(0, 95)
    elif float(x) >= 9.5 and float(y) >= 9.5 and float(z) >= 60:
        severeRiskLevel.insert(0, 100)

computeSevereRiskLevelButton = tk.Button(text = "Compute Severe Risk Level", command = ComputeSevereRiskLevel, bg = "purple", fg = "white", font = ("calibri", 10, "bold"), width = 23, cursor = "X_cursor")
canvasArea.create_window(875, 785, window = computeSevereRiskLevelButton)

#Display
window.mainloop()