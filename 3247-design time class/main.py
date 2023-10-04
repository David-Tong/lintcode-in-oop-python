class MyTime:
    def __init__(self,hour,minute,second):
        # write your code here
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def set_hour(self, hour):
        self.__hour = hour

    def get_hour(self):
        return self.__hour
    
    def set_minute(self, minute):
        self.__minute = minute
    
    def get_minute(self):
        return self.__minute
    
    def set_second(self, second):
        self.__second = second

    def get_second(self):
        return self.__second
