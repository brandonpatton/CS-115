'''
Created on 11/27/17
@author:   bpatton
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

Brandon Patton

CS115 - Hw 11 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    
    def copy(self):
        '''Returns a new object with the same month, day, year
            as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew
    
    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
            whether or not they are the in the same place in memory.'''
        return self.year == d2.year and self.month == d2.month and \
            self.day == d2.day
            
    def tomorrow(self):
        '''Changes the calling object so that it represents one calendar day after
        the date it originally represented.'''
        if self.isLeapYear() == True and self.month == 2:
            if self.day == 29 and self.month == 2:
                self.month += 1
                self.day = 0
            self.day += 1
        elif self.day == DAYS_IN_MONTH[self.month] and self.month < 12:              
            self.day = 1
            self.month += 1
        elif self.day == DAYS_IN_MONTH[self.month] and self.month == 12:
            self.day = 1
            self.month = 1
            self.year += 1
        else:
            self.day += 1
            
    def yesterday(self):
        '''Changes the calling object so that it represents one calendar day before
        the date it originally represented.'''
        if self.month == 3 and self.day == 1 and self.isLeapYear() == True:
            self.month -= 1
            self.day = DAYS_IN_MONTH[self.month] + 1
        elif self.day == 1 and self.month > 1:
            self.month -= 1
            self.day = DAYS_IN_MONTH[self.month]
        elif self.day == 1 and self.month == 1:
            self.month = 12
            self.day = DAYS_IN_MONTH[self.month]
            self.year -= 1
        else:
            self.day -= 1
            
    def addNDays(self, N):
        '''Changes the calling object so that it represents N calendar days after 
        the date it originally represented.'''  
        print(self) 
        for d in range(N):
            Date.tomorrow(self)
            print(self)
    
    def subNDays(self, N):
        '''Changes the calling object so that it represents N calendar days before
        the date it originally represented.'''
        print(self)
        for d in range(N):
            Date.yesterday(self)
            print(self)
    
    def isBefore(self, d2):
        '''This method returns True if the calling object is a calendar date 
        before the input named d2 (which will always be an object of type Date). 
        If self and d2 represent the same day, this method returns False. 
        Similarly, if self is after d2, this returns False'''
        if d2.year == self.year:
            if d2.month == self.month:
                if d2.day > self.day:
                    return True
                else:
                    return False
            elif d2.month > self.month:
                return True
            else:
                return False
        elif d2.year > self.year:
            return True
        else:
            return False
        
    def isAfter(self, d2):
        '''This method returns True if the calling object is a calendar date
        after the input named d2 (which will always be an object of type Date). 
        If self and d2 represent the same day, this method returns False. 
        Similarly, if self is before d2, this returns False.'''
        if self.equals(d2):
            return False
        else:
            return not self.isBefore(d2)
    
    def diff(self, d2):
        '''This method returns an integer representing the number of days 
        between self and d2.'''
        day1 = self.copy()
        day2 = d2.copy()
        count = 0
        while day1.isBefore(day2):
            day1.tomorrow()
            count -= 1
        while day1.isAfter(day2):
            day1.yesterday()
            count += 1
        return count
    
    def dow(self):
        '''This method returns a string that indicates the day of the week 
        (dow) of the object (of type Date) that calls it. That is, this method 
        returns one of the following strings: �Monday�, �Tuesday�, �Wednesday�, 
        �Thursday�, �Friday�, �Saturday�, or �Sunday� '''
        
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', \
                        'Friday', 'Saturday', 'Sunday']
        d = Date(11, 27, 2017)
        return days_of_week[self.diff(d) % 7]

       
        
        
        