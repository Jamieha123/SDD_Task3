#from message import Format#Format of message
class Log:
    tempArray = []#store temporary logs in file
    def __init__(self, DateNTime, orginal_path):
        self.DateNTime = DateNTime
        self.original_path = orginal_path

    def File(self, message):# forwarding the parameter "message" to make a custom judgement of logging
        logName = '/Logs/logsDetection'# location of logFile
        fileLog =  open(self.original_path+logName, 'r').read().split('\n')
        for evryLog in fileLog:
            self.tempArray.append(evryLog)# List all lines of txt
        noOfLogs = len(self.tempArray)# add them to a temporary array
        logString = "%s) %s: %s" % (noOfLogs, message,self.DateNTime)
        fileLog = open(self.original_path+logName, 'a')
        fileLog.write(str(logString)+'\n')
        fileLog.close()