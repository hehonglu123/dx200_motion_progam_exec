from MotomanEthernet import MotomanConnector
import time, copy
import numpy as np


###YASKAWA REAL TIME READING: 20HZ
mh=MotomanConnector(IP='192.168.55.1', PORT=80, S_pulse = 1341.6437777308, L_pulse = 1341.4, U_pulse = 1341.4, R_pulse = 1000, B_pulse = 1000, T_pulse = 622)
mh.connectMH() #Connect to Controller

mh.setGroup(2)
print(mh.readGroup())
# last_reading=np.zeros(6)
# while True:
# 	try:
# 		time_now=time.time()
# 		new_reading=mh.getJointAnglesMH()
# 		if np.linalg.norm(last_reading-new_reading)>0:
# 			print('freq: ',1/(time.time()-time_now))
# 			print(np.linalg.norm(last_reading-new_reading))
# 		last_reading=copy.deepcopy(new_reading)
# 	except:
# 		mh.disconnectMH()
# 		break
