from multiprocessing import Process,Manager
from result import getResult
from checkLifes import getLife
def start(id,startCode,semester,start):
    if(getLife(id)==0):
        return {'lifeerror':'not enough lifes left'}
    manager = Manager()
    results  =manager.list()
    errors = manager.list()
    end = start+10
    rollNos = []
    for x in range(int(start), int(end) + 1):
        rollNo = str(startCode)
        if (x >= 1 and x < 10):
            rollNo = rollNo + '00' + str(x)
        elif (x >= 10 and x < 100):
            rollNo = rollNo + '0' + str(x)
        else:
            rollNo = rollNo + str(x)
        rollNos.append(rollNo)
    process  = []
    for x in rollNos:
        process.append(Process(target=getResult,args=(x,semester,results,errors)))
    for x in process:
        import time
        time.sleep(1)
        x.start()
    for y in process:
        y.join()
    return [list(results),list(errors)]


