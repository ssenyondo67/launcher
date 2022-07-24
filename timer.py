
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
 
# timer1=timer(23,59,00)        
        

# print(timer1.previous_second())
# print(timer1.previous_second())
# print(timer1.previous_second())


class weeker:
    names={1:"MON",2:"TUE",3:"WED",4:"THU",5:"FRI",6:"SAT",0:"SUN"}
    def __init__(self,name) -> None:
        
        if name in weeker.names.values():
           self.__name = name
        else:
            raise Exception('Weekday.error')
    
    def __str__(self) -> str:
        return str(self.__name)
        
    def add_days(self,n):
       key=list(weeker.names.keys())[list(weeker.names.values()).index(self.__name)]
       key += (n%7)
       if key >6:
          key -=7
       self.__name=list(weeker.names.values())[list(weeker.names.keys()).index(key)]
       return self.__name
    
    def subtract_days(self,n):
        key=list(weeker.names.keys())[list(weeker.names.values()).index(self.__name)]
        if key ==0 and n%7 !=0 :
            key=7
        
        key -= (n%7)       
        if key<0:
            key +=7
        self.__name=list(weeker.names.values())[list(weeker.names.keys()).index(key)]
        return self.__name
    
week =weeker("TUE")
print(week.subtract_days(89))