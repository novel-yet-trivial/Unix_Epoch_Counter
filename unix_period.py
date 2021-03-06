import datetime
import sys
import time

#Press CTRL C to interrupt the unix_countup function:
###If highlight command line, then the function pauses but does not resync time
def unix_countup(party=1500000000, moment=0.01, offset=0):
    '''Unix Time Stamp Counter.
    
    unix_countup(party, moment, offset)
    party:= counter end time
    moment:= distinct measures of time
    offset:= displacement from generated time
    
    Example:
    unix_countup(party=1500000000, moment=0.01, offset=0)
    '''
    now = round((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() + offset, 2)
    while now < party:
        print("{:,}".format(now)),'\r',
        sys.stdout.flush()
        time.sleep(moment)
        now = round((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() + offset, 2)






###If text is marked in the command-line, then the function pauses and does not resync time. I will upgrade this file in the future, so the time will resync after text is marked.
###Note: The counter ascends. I might add a parameter to the unix_countup() that allows for ascending or descending the counter.
