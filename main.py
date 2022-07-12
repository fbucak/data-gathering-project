import weather
import requests
import autoSelenium
import json
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QImage
import sys
import os
import psycopg2

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("autoscout24.ui", self)
        city = self.Action()
        print(city)
        self.city.setText(weather.location(city))
        self.date.setText(weather.date(city))      
        self.date1.setText(weather.date1(city))
        self.date2.setText(weather.date2(city))
        self.start_button.clicked.connect(self.start)
        self.tableWid.setColumnWidth(0,380)
        self.tableWid.clicked.connect(self.Action)
                    
        self.minTemp.setText(weather.min_temp(city))
        self.minTemp1.setText(weather.min_temp1(city))
        self.minTemp2.setText(weather.min_temp2(city))
        self.maxTemp.setText(weather.max_temp(city))
        self.maxTemp1.setText(weather.max_temp1(city))
        self.maxTemp2.setText(weather.max_temp2(city))
        
        self.condition.setText(weather.condition(city))
        self.condition1.setText(weather.condition1(city))
        self.condition2.setText(weather.condition2(city))


        
        
        image = QImage()
        image.loadFromData(requests.get(str(weather.icon_url(city))).content)
        self.icon.setPixmap(QPixmap(image))
        image.loadFromData(requests.get(str(weather.icon_url1(city))).content)
        self.icon1.setPixmap(QPixmap(image))
        image.loadFromData(requests.get(str(weather.icon_url2(city))).content)
        self.icon2.setPixmap(QPixmap(image))

# ***********************
        self.search_pushButton.clicked.connect(self.autoSelennium)


    def start(self):
             
            conn = psycopg2.connect(host= 'localhost',database = 'Autoscout24',user = 'postgres',password = '981')
            cur = conn.cursor()
            

        
            qry = "select brand_model,year,plate from cars"
            cur.execute(qry)
            self.cars = cur.fetchall()
        
            self.tableWid.setRowCount(len(self.cars))
            self.total_count_label.setText(str(len(self.cars)))
            row = 0
            for i in self.cars:
                self.tableWid.setItem(row, 0, QtWidgets.QTableWidgetItem(i[0]))
                self.tableWid.setItem(row, 1, QtWidgets.QTableWidgetItem(i[1]))
                self.tableWid.setItem(row, 2, QtWidgets.QTableWidgetItem(i[2]))
                row = row+1

            conn.commit()

    def Action(self):
        conn= psycopg2.connect(host= 'localhost',
        database = 'Autoscout24',
        user = 'postgres',password = '981')
        cur = conn.cursor()

        indx=(self.tableWid.selectionModel().currentIndex())
        self.value=indx.row()+1

        cur.execute("select brand_model,plate,km,year,price,province,image from cars where id = %s;",(self.value,))
        self.car = cur.fetchall()
        for self.c in self.car:
            self.modellabel.clear()
            self.modellabel.insert(self.c[0])
            self.kmlabel.clear()
            self.kmlabel.insert(self.c[2])
            self.pricelabel.clear()
            self.pricelabel.insert(self.c[4])
            self.yearlabel.clear()
            self.yearlabel.insert(self.c[3])
            self.provincelabel.clear()
            self.provincelabel.insert(self.c[5])
            self.platelabel.clear()
            self.platelabel.insert(self.c[1])
            
        return self.c
            

        conn.commit()

    def plakaSearch(self,plaka):
        self.plaka=plaka
        self.search_pushButton.setText(self.plaka)
    
    def autoSelennium(self):
        self.plaka=self.platelabel.text()
        autoSelenium.plakaSelenium(self.plaka)


        
            

    
        
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()