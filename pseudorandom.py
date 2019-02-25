import datetime
import time

def pseudorand():
        date= str(datetime.datetime.now())
        aleat= int(date[-2])
#the idea is to create a second layer of pseudorandomness,
#by making the computer perform X numbers of operations before
#getting the final number
        for x in range(aleat):
                time.sleep(0.0001)
        date= str(datetime.datetime.now())
        aleat= int(date[-1])
#the sleep seems to be necessary for the date to be randomized enough
#for some reason, when the sleep steps removed, the results tend
#to be disproportionately 0 (380 out of 400, approx)        
        time.sleep(0.0002)
        return (aleat)
        

#the idea here is to get the difference between the first number and last
# and then, given that length, create random numbers for each digit
#then checking if the resulting number is less than the difference
#between the two given numbers
def pseudorandint(start, end):      
        if type(start) != int or type (end) != int:
                return ("ERROR, MUST USE INTEGERS!")
        elif start == end:
                return(start)
        elif start < end:
                variance = end - start
                begin=start
        elif start > end:
                variance = start - end
                begin=end
        variance = abs (variance)
        variance_length = len (str(variance))
        result = variance + 2
        first_digit = variance%10+3
        provResult=''
        while result > variance:              
                while first_digit > variance%10:
                        first_digit = pseudorand()
                        prov_result=str(first_digit)
                        for z in range(first_digit):
                                time.sleep(0.001)
                for item in range(variance_length-1):
                        item=pseudorand()
                        prov_result+=str(item)
                        for z in range(item):
                                time.sleep(0.001)                       
                       # print('item', item)
                result=int(prov_result)
        return(result+begin)


