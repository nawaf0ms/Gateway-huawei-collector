from netaddr import *
import socket
from threading import Thread
from time import sleep
import requests
from selenium import webdriver

startip = input("enter start ip >> ")
endip = input("enter end ip >> ")
ip_list = list(iter_iprange(startip, endip))
a3dd_ip = len(ip_list)
list_ip_port_open=[]
threads = []
adad = []
#--------------------------------------
page401_status =[]
page200_status =[]
page_erorr_requests = []
HG8245Q_HG8245 = []
HG658_V2_Home_Gateway_HG658_V2 =[]
page_unknown = []
adad2= []
threads2 =[]
#--------------------------------------
def scan_port(i):
    adad.append(i)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port_stat = s.connect_ex((i, 80))
    s.close()
    if port_stat == 0:
        list_ip_port_open.append(i)
    adad.remove(i)
#---------------------------------------
def analysis(ip):
    ip = "http://{}".format(ip)
    adad2.append(ip)
    try:
        req = requests.get(ip, verify=False, timeout=10)
        if req.status_code == 200:
            page200_status.append(ip)
            try:
                #driver = webdriver.Chrome('C:\webdrivers\chromedriver.exe')
                driver = webdriver.Firefox(executable_path=r'C:\webdrivers\geckodriver.exe')
                driver.set_page_load_timeout(10)
                driver.get(ip)
                print(driver.title)
                if driver.title == ("HG8245Q" or "HG8245"):
                    HG8245Q_HG8245.append(ip)
                    print("{} HG8245Q_HG8245".format(ip))

                elif driver.title == "HG658 V2 Home Gateway HG658 V2":
                    HG658_V2_Home_Gateway_HG658_V2.append(ip)
                    print("{} HG658 V2 Home Gateway HG658 V2".format(ip))
                else:
                    page_unknown.append(ip)
                    print("{} unknown".format(ip))
                driver.quit()


            except:
                print("{} erorr".format(ip))
                try:
                    driver.quit()
                except:
                    print("erorr driver quit")





        else:
            print("{} 401 status".format(ip))
            page401_status.append(ip)


    except:
        page_erorr_requests.append(ip)
        print("erorr {}".format(ip))
    adad2.remove(ip)



#----------------------------------------

for i in range(a3dd_ip):
    if len(adad) in list(range(500,600)):
        sleep(0.05)
        ip = str(ip_list[i])
        t = Thread(target=scan_port, args=(ip,))
        threads.append(t)
        t.start()
        print(ip)
    elif len(adad) in list(range(600, 800)):
        sleep(0.1)
        ip = str(ip_list[i])
        t = Thread(target=scan_port, args=(ip,))
        threads.append(t)
        t.start()
        print(ip)
    elif len(adad) in list(range(800,1000)):
        sleep(0.5)
        ip = str(ip_list[i])
        t = Thread(target=scan_port, args=(ip,))
        threads.append(t)
        t.start()
        print(ip)
    elif len(adad) > 1000:
        sleep(1)
        ip = str(ip_list[i])
        t = Thread(target=scan_port, args=(ip,))
        threads.append(t)
        t.start()
        print(ip)
    else:
        ip = str(ip_list[i])
        t = Thread(target=scan_port, args=(ip,))
        threads.append(t)
        t.start()
        print(ip)

[x.join() for x in threads]
print(list_ip_port_open)
#------------------------------------------------------
for ip in list_ip_port_open:
    if len(adad2) in list(range(5,7)):
        sleep(3)
        t = Thread(target=analysis, args=(ip,))
        threads2.append(t)
        t.start()
    elif len(adad2) in list(range(7,9)):
        sleep(5)
        t = Thread(target=analysis, args=(ip,))
        threads2.append(t)
        t.start()
    elif len(adad2) in list(range(9,13)):
        sleep(10)
        t = Thread(target=analysis, args=(ip,))
        threads2.append(t)
        t.start()
    else:
        t = Thread(target=analysis, args=(ip,))
        threads2.append(t)
        t.start()

[x.join() for x in threads2]
#------------------------------------------------------------

file_About_analysis = open("file About analysis.txt","w")
file_About_analysis.write("About analysis \n Number of IPs examined {0} \n Number of IPs open port 80 {1} \n Number IPs 200 status {2} \n Number IPs 401 status {3} \n Number HG8245Q or HG8245 {4} \n Number HG658_V2_Home_Gateway_HG658_V2 {5} \n Number page_unknown {6}".format(a3dd_ip,len(list_ip_port_open),len(page200_status),len(page401_status),len(HG8245Q_HG8245),len(HG658_V2_Home_Gateway_HG658_V2),len(page_unknown)))
file_About_analysis.close()
if len(HG8245Q_HG8245) >= 1:
    file_HG8245Q_HG8245 = open("HG8245Q_HG8245.txt", "w")
    for ips1 in HG8245Q_HG8245:
        file_HG8245Q_HG8245.write(ips1)
        file_HG8245Q_HG8245.write("\n")
    file_HG8245Q_HG8245.close()
if len(HG658_V2_Home_Gateway_HG658_V2) >= 1:
    file_HG658_V2_Home_Gateway_HG658_V2 = open("HG658_V2_Home_Gateway_HG658_V2.txt", "w")
    for ips2 in HG658_V2_Home_Gateway_HG658_V2:
        file_HG658_V2_Home_Gateway_HG658_V2.write(ips2)
        file_HG658_V2_Home_Gateway_HG658_V2.write("\n")
    file_HG658_V2_Home_Gateway_HG658_V2.close()
if len(page_unknown) >= 1:
    file_page_unknown = open("page_unknown.txt", "w")
    for ips3 in page_unknown:
        file_page_unknown.write(ips3)
        file_page_unknown.write("\n")
    file_page_unknown.close()

#-----------------------------------------------------------------
