import os, subprocess, time ,datetime

file = open("doge.log","a")
str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " start....\r\n"
file.write(str)
file.flush()
while True:
      print("Starting CG...")
      now = datetime.datetime.now()
      
      #p = subprocess.Popen("D:\\install\\btc\\cgminer-3.1.0-windows\\cgminer.exe -c home-2-card.conf")
      #p = subprocess.Popen("E:\\U\\cgminer-3.7.2-windows\\WaDOGE.bat")
      #time.sleep(3600)
      #print("Terminating CG...")
      #p.terminate()
      #os.system("taskkill /T /F /IM  cgminer.exe ")
      res = os.popen("tasklist /fi \"imagename eq cgminer.exe\"")
      str = res.read()
      if str.find("cgminer") < 0:
		p = subprocess.Popen("E:\\U\\cgminer-3.7.2-windows\\WaDOGE.bat")
		now = datetime.datetime.now()
		str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " closed,restart....\r\n"
      		file.write(str)
		file.flush()
      time.sleep(5)
      if (datetime.datetime.now() - now).seconds > 7200:
		print("Terminating CG...")
		os.system("taskkill /T /F /IM  cgminer.exe ")
		str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " restart....\r\n"
		file.write(str)
		file.flush()