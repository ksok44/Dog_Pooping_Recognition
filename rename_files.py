import os
#mydir = 'C:/Users/kobys/Desktop/DApps_Model/Images/dog_pooping'
#mydir = 'C:/Users/kobys/Desktop/DApps_Model/Images/dog_not_pooping'
mydir = 'G:/My Drive/Analytic Apps/DApps_Project/Images_Staging'
for dirs, subdirs, files in os.walk(mydir):
    counter = 0
    for f in files:
    	os.rename(os.path.join(mydir,f), os.path.join(mydir,'dnp'+str(counter)+'.jpg'))
    	counter += 1