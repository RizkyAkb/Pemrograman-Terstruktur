from datetime import *

def diff_date(x):
    time = datetime.strptime(x, '%Y-%m-%d').date()
    
    time_now = datetime.date(datetime.now())
    
    gap =  time_now - time

    return gap
    
print ('Selisih tanggal 2021-12-1 dengan hari ini adalah',diff_date('2021-12-1').days)
