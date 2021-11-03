from parinya import LINE
import schedule
import time
line = LINE('Y3qLnECWXQTc3RN6CU6QatWNwX7DrGYllRbHPVy7jX9')


def thai():
    line.sendtext('ภาษาไทย: ---')

def math_01():
    line.sendtext('จำนวนและพีชคณิต: https://meet.google.com/zop-oxmh-jjv?authuser=0 ')

def eng_teacher():
    line.sendtext('อังกฤษท่องเที่ยว teacher: https://meet.google.com/rjo-yhuz-zhf?authuser=0 ')

def sci():
    line.sendtext('วิทยาศาสตร์: https://meet.google.com/pwx-mgxh-xgv?authuser=0 ')

def internet():
    line.sendtext('อินเตอร์เน็ต: https://meet.google.com/tgy-bcbr-ahi?authuser=0 ')

def HSK():
    line.sendtext('ติวHSK: https://meet.google.com/hdh-vnni-rno?authuser=0 ')

def SOC():
    line.sendtext('สังคมศึกษา: https://meet.google.com/guk-cnqn-abm?authuser=0')

def free():
    line.sendtext('คาบว่างๆๆๆ')
    line.sendsticker(2, 1)

def PE():
    line.sendtext('พละ: https://meet.google.com/iwz-axie-qyx?authuser=0 ')

def Sub():
    line.sendtext('ชมรม: ---')

def Art():
    line.sendtext('ศิลปะ: https://meet.google.com/uas-yaqr-kkc?authuser=0')

def math_02():
    line.sendtext('เรขาคณิตและสถิติ: ---')

def design():
    line.sendtext('ออกแบบ: https://meet.google.com/xbd-vtcc-dec?authuser=0')

def CHN():
    line.sendtext('ภาษาจีน: https://meet.google.com/hdh-vnni-rno?authuser=0 ')

def eng():
    line.sendtext('อังกฤษ: https://meet.google.com/ieq-dgkq-fpb?authuser=0')

def h_work():
    line.sendtext('การงาน: https://meet.google.com/yft-vksg-thn?authuser=0')

def PE_02():
    line.sendtext('สุขศึกษา: https://meet.google.com/eep-xtew-ruk?authuser=0')

def history():
    line.sendtext('ประวัติ: https://meet.google.com/yrq-tjbh-itd?authuser=0')

def info():
    line.sendtext('แนะแนว: https://meet.google.com/fpt-qmmu-zfy?authuser=0')


#monday
schedule.every().monday.at("08:00").do(thai)
schedule.every().monday.at("09:00").do(math_01)
schedule.every().monday.at("10:00").do(eng_teacher)
schedule.every().monday.at("11:00").do(sci)
schedule.every().monday.at("13:00").do(internet)
schedule.every().monday.at("14:00").do(HSK)

#tuesday
schedule.every().tuesday.at("08:00").do(math_01)
schedule.every().tuesday.at("09:00").do(SOC)
schedule.every().tuesday.at("10:00").do(sci)
schedule.every().tuesday.at("11:00").do(free)
schedule.every().tuesday.at("13:00").do(PE)
schedule.every().tuesday.at("14:00").do(Sub)

#wednesday
schedule.every().wednesday.at("08:00").do(Art)
schedule.every().wednesday.at("09:00").do(math_02)
schedule.every().wednesday.at("10:00").do(design)
schedule.every().wednesday.at("11:00").do(CHN)
schedule.every().wednesday.at("13:00").do(eng_teacher)

#thursday
schedule.every().tuesday.at("08:00").do(eng)
schedule.every().tuesday.at("09:00").do(math_01)
schedule.every().tuesday.at("10:00").do(thai)
schedule.every().tuesday.at("11:00").do(h_work)
schedule.every().tuesday.at("13:00").do(SOC)

#friday
schedule.every().tuesday.at("08:00").do(math_02)
schedule.every().tuesday.at("09:00").do(sci)
schedule.every().tuesday.at("10:00").do(PE_02)
schedule.every().tuesday.at("11:00").do(history)
schedule.every().tuesday.at("13:00").do(info)






while True:
    schedule.run_pending()
    time.sleep(1)
