from Ventanapython import *
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(6,GPIO.OUT)
Temperatura=100
Humedad=60
Presion=400
Altitud=2270
class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,*args,**kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self)
        
        self.label_5.setText("%0.1f" %Temperatura)
        self.label_6.setText("%0.1f" %Humedad)
        self.label_7.setText("%0.1f" %Presion)
        self.label_8.setText("%0.1f" %Altitud)
        self.label_9.setText("ºC")
        self.label_10.setText("%" )
        self.label_11.setText("MPA")
        self.label_12.setText("m")
        self.lcdNumber.setProperty("value",Temperatura)
        self.lcdNumber_2.setProperty("value",Humedad)
        self.lcdNumber_3.setProperty("value",Presion)
        self.lcdNumber_4.setProperty("value",Altitud)
        #for i in range(0,10):
            
            #sleep(1)
        #Actualizar()
        QtWidget.update()
        Temperatura+=1
        Humedad+=6
        Presion+=4
        Altitud+=2
        
            
if __name__=="__main__":
    app=QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
    
    