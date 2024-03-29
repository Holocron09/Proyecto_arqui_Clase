from Ventanapython import *
from PyQt5.QtCore import QTimer
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import RPi.GPIO as GPIO
from time import sleep
import board
import busio
import adafruit_bme280
import psycopg2
from psycopg2 import Error
try:
    i2c = busio.I2C(board.SCL, board.SDA)
    bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
except:
    print("no sensor attatched")



GPIO.setmode(GPIO.BCM)
GPIO.setup(6,GPIO.OUT)
Temperatura=0
Humedad=0
Presion=0
Altitud=0
lock=0
val=0
hour=[]
temp=[]
hum=[]
pres=[]
Alt=[]
pen=pg.mkPen(255,0,0)
pen1=pg.mkPen(0,255,0)
pen2=pg.mkPen(0,0,255)

        
class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    global Temperatura, Humedad, Presion, Altitud 
    def __init__(self,*args,**kwargs):
        QtWidgets.QMainWindow.__init__(self,*args,**kwargs)
        self.setupUi(self)
        self.valores()
        self.graphicsView.setBackground('w')
        self.graphicsView_2.setBackground('w')
        self.graphicsView_3.setBackground('w')
        self.graphicsView_4.setBackground('w')
        self.graphicsView_5.setBackground('w')
        #self.actualizar()
    def valores(self):
        global Temperatura, Humedad, Presion, Altitud
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
        
    def actualizar(self):
        global Temperatura, Humedad, Presion, Altitud,val,hour,temp, hum, pres ,Alt

        sensor()
        self.graphicsView.plot(hour,temp)
        self.graphicsView_2.plot(hour,hum, pen=pen)
        self.graphicsView_3.plot(hour,Alt,pen=pen1)
        self.graphicsView_4.plot(hour,pres,pen=pen2)
        self.graphicsView_5.plot(hour,temp)
        self.graphicsView_5.plot(hour,hum, pen=pen)
        self.graphicsView_5.plot(hour,Alt,pen=pen1)
        self.graphicsView_5.plot(hour,pres,pen=pen2)
        valores=self.spinBox.value()
        #print(valores)
        if (val)>=valores:
            val=0
            hour=[]
            temp=[]
            hum=[]
            pres=[]
            Alt=[]
            self.graphicsView.clear()
            self.graphicsView_2.clear()
            self.graphicsView_3.clear()
            self.graphicsView_4.clear()
            self.graphicsView_5.clear()
        self.valores()
    
def sensor():
    global Temperatura, Humedad, Presion, Altitud,temp, hum, pres ,Alt,hour,val
    try:
        Temperatura=bme280.temperature
        Humedad=bme280.humidity
        Presion=bme280.pressure
        Altitud=bme280.altitude
        temp.append(Temperatura)
        hum.append(Humedad)
        pres.append(Presion)
        Alt.append(Altitud)
        hour.append(val)
        val+=1
        Database()
    except:
        print ("Sensor Data not Available")
def Database():
    global Temperatura, Humedad, Presion, Altitud
    try:
        connection=psycopg2.connect(user="pi", password="raspberry",host="127.0.0.1",port="5432",database="pi")
        cursor=connection.cursor()
        try:
            createTableQuery='''Create TABLE IF NOT EXISTS EstatMeteo
                (ID SERIAL  PRIMARY KEY,
                TEMPERATURA    REAL    NOT NULL,
                HUMEDAD        REAL    NOT NULL,
                PRESION        REAL    NOT NULL,
                ALTITUD        REAL    NOT NULL);'''
            cursor.execute(createTableQuery)
            connection.commit()
            print('Table created successfully in PostgresSQL')
        except:
            print('Table already created')
        try:
            
            addTableQuerry="INSERT INTO EstatMeteo (temperatura,humedad,presion,altitud) VALUES (%0.2f,%0.2f,%0.2f,%0.2f);" %(Temperatura, Humedad, Presion, Altitud)
            print(addTableQuerry)
            cursor.execute(addTableQuerry)
            connection.commit()
            print("Data added successfully")
        except:
            print("Data could not be added")
    except(Exception,psycopg2.DatabaseError)as error:
        print('Error while creating PostgresSQL table', error)
    finally:
    #closing database connection
        if (connection):
            cursor.close()
            connection.close()
            print("PostgresSQL connection is closed")
                    

                
if __name__=="__main__":
    app=QtWidgets.QApplication([])
    window = MainWindow()
    timer=QTimer()
    timer.timeout.connect(window.actualizar)
    timer.start(500)
    
    window.show()
    app.exec()
    
    
    
    