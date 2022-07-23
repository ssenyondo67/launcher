
def format_string(hours,minutes,seconds):
    hour = str(hours)
    minute = str(minutes)
    second = str(seconds)
    if hours<10:
        hour = "0"+str(hours)
    if minutes<10:
        minute= "0"+str(minutes)
    if seconds<10:
        second= "0"+str(seconds)
    
    return "%s:%s:%s"%(hour,minute, second)

class timer:

    def __init__(self,hours=0,minutes=0,seconds=0):
        self.__hours=hours
        self.__minutes=minutes
        self.__seconds=seconds

    def __str__(self) -> str:
        return format_string(self.__hours,self.__minutes,self.__seconds)

    def next_second(self):
        self.__seconds =self.__seconds +1
        self.__minutes=self.__minutes
        self.__hours=self.__hours
        if self.__seconds == 60:
            self.__seconds = 0
            self.__minutes +=1
            if self.__minutes == 60:
                self.__minutes=0
                self.__hours +=1
                if self.__hours==24:
                   self.__hours=0
        return format_string(self.__hours,self.__minutes,self.__seconds)
 
    def previous_second(self):
        self.__seconds =self.__seconds -1
        self.__minutes=self.__minutes
        self.__hours=self.__hours
        if self.__seconds <0:
            self.__seconds = 59
            self.__minutes -=1
            if self.__minutes < 0:
                self.__minutes=59
                self.__hours -=1
                if self.__hours < 0:
                    return 'time has reached to zero'
        return format_string(self.__hours,self.__minutes,self.__seconds)
 
timer1=timer(23,59,00)        
        

print(timer1.previous_second())
print(timer1.previous_second())
print(timer1.previous_second())