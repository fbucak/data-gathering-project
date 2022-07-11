import weather
import requests
import json
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap, QImage
import sys
import os

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("autoscout24.ui", self)
        
        city = 'Amsterdam'
        self.city.setText(weather.location(city))
        self.date.setText(weather.date(city))      
        self.date1.setText(weather.date1(city))
        self.date2.setText(weather.date2(city))
                    
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
        
            

    
        
        
        
        
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()