import sys
import io
import time
from datetime import datetime
from PyQt5.QtGui import QPixmap, QTransform, QColor, QImage
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QWidget
from PyQt5.QtCore import QPoint
from res_rc import *
from res_rc1 import *
from res_rc2 import *
from res_rc3 import *
from res_rc4 import *
import sqlite3

NAME = 'picture.png'
ReLogWindow = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>633</width>
    <height>600</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>600</width>
    <height>600</height>
   </size>
  </property>
  <property name="font">
   <font>
    <family>Arial</family>
    <weight>50</weight>
    <bold>false</bold>
   </font>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QWidget" name="widget" native="true">
   <property name="geometry">
    <rect>
     <x>60</x>
     <y>40</y>
     <width>500</width>
     <height>500</height>
    </rect>
   </property>
   <property name="minimumSize">
    <size>
     <width>500</width>
     <height>500</height>
    </size>
   </property>
   <property name="maximumSize">
    <size>
     <width>500</width>
     <height>500</height>
    </size>
   </property>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>500</width>
      <height>500</height>
     </rect>
    </property>
    <property name="minimumSize">
     <size>
      <width>500</width>
      <height>500</height>
     </size>
    </property>
    <property name="maximumSize">
     <size>
      <width>500</width>
      <height>500</height>
     </size>
    </property>
    <property name="styleSheet">
     <string notr="true">border-image:url(:/pictures/F8fDYJzboAAbCup.png.png.png);
border-radius: 20px;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="regButton">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>400</y>
      <width>181</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
background-color: rgba(0,0,0,0);
border: 2px solid rgba(255, 33, 100, 230);
border-radius: 10px;
padding: 10px;
font-size: 10pt;
color: rgba(255, 255, 255, 200);
}

QPushButton:hover {
background-color: rgba(255,33,100,100);
}</string>
    </property>
    <property name="text">
     <string>Зарегистрироваться</string>
    </property>
   </widget>
   <widget class="QPushButton" name="logButton">
    <property name="geometry">
     <rect>
      <x>70</x>
      <y>350</y>
      <width>121</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
      <weight>75</weight>
      <italic>false</italic>
      <bold>true</bold>
     </font>
    </property>
    <property name="cursor">
     <cursorShape>PointingHandCursor</cursorShape>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
background-color: rgba(0,0,0,0);
border: 2px solid rgba(255, 33, 100, 230);
border-radius: 10px;
padding: 10px;
font-size: 10pt;
color: rgba(255, 255, 255, 200);
}

QPushButton:hover {
background-color: rgba(255,33,100,100);
}</string>
    </property>
    <property name="text">
     <string>Войти</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="enterPassword">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>265</y>
      <width>201</width>
      <height>45</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QLineEdit {
background-color: rgba(0,0,0,0);
border: 2px solid rgba(255, 33, 100, 230);
border-radius: 10px;
padding: 10px;
font-size: 10pt;
color: rgba(255, 255, 255, 200);
}

QLineEdit:hover {
background-color: rgba(255,33,100,100);
}</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="enterLogin">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>160</y>
      <width>201</width>
      <height>45</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QLineEdit {
background-color: rgba(0,0,0,0);
border: 2px solid rgba(255, 33, 100, 230);
border-radius: 10px;
padding: 10px;
font-size: 10pt;
color: rgba(255, 255, 255, 200);
}

QLineEdit:hover {
background-color: rgba(255,33,100,100);
}</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>110</y>
      <width>231</width>
      <height>371</height>
     </rect>
    </property>
    <property name="minimumSize">
     <size>
      <width>231</width>
      <height>371</height>
     </size>
    </property>
    <property name="maximumSize">
     <size>
      <width>231</width>
      <height>371</height>
     </size>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgba(0, 0, 0, 100);
border-radius: 10px;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>36</x>
      <y>220</y>
      <width>151</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color:rgb(255, 255, 255)</string>
    </property>
    <property name="text">
     <string>Пароль</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>36</x>
      <y>110</y>
      <width>151</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color:rgb(255, 255, 255)</string>
    </property>
    <property name="text">
     <string>Логин</string>
    </property>
   </widget>
   <widget class="QLabel" name="ReLogResult">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>440</y>
      <width>211</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>9</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color:rgb(255, 255, 255)</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="closeWindowButton">
    <property name="geometry">
     <rect>
      <x>440</x>
      <y>20</y>
      <width>41</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
background-color: rgba(255,33,100,150);
border: 2px solid rgba(255, 33, 100, 230);
border-radius: 10px;
padding: 10px;
font-size: 10pt;
color: rgba(255, 255, 255, 200);
}

QPushButton:hover {
background-color: rgba(255,33,100,100);
}</string>
    </property>
    <property name="text">
     <string>X</string>
    </property>
   </widget>
   <widget class="QCheckBox" name="reminderButton">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>310</y>
      <width>181</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QCheckBox {
background-color: rgba(0,0,0,0);
border: 2px solid rgba(255, 33, 100, 230);
border-radius: 10px;
padding: 10px;
font-size: 10pt;
color: rgba(255, 255, 255, 200);
}

QCheckBox:hover {
background-color: rgba(255,33,100,100);
}</string>
    </property>
    <property name="text">
     <string>Запомнить меня</string>
    </property>
   </widget>
   <zorder>label</zorder>
   <zorder>label_2</zorder>
   <zorder>regButton</zorder>
   <zorder>logButton</zorder>
   <zorder>enterPassword</zorder>
   <zorder>enterLogin</zorder>
   <zorder>label_3</zorder>
   <zorder>label_4</zorder>
   <zorder>ReLogResult</zorder>
   <zorder>closeWindowButton</zorder>
   <zorder>reminderButton</zorder>
  </widget>
 </widget>
 <resources>
  <include location="res.qrc"/>
 </resources>
 <connections/>
</ui>
"""

LoadWindow = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>502</width>
    <height>383</height>
   </rect>
  </property>
  <property name="font">
   <font>
    <family>Arial</family>
    <pointsize>12</pointsize>
    <weight>75</weight>
    <bold>true</bold>
   </font>
  </property>
  <property name="cursor">
   <cursorShape>PointingHandCursor</cursorShape>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QWidget" name="widget" native="true">
   <property name="geometry">
    <rect>
     <x>60</x>
     <y>60</y>
     <width>401</width>
     <height>281</height>
    </rect>
   </property>
   <widget class="QProgressBar" name="progressBar">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>50</y>
      <width>331</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="focusPolicy">
     <enum>Qt::NoFocus</enum>
    </property>
    <property name="contextMenuPolicy">
     <enum>Qt::DefaultContextMenu</enum>
    </property>
    <property name="styleSheet">
     <string notr="true">QProgressBar{
background-color: rgb(124, 113, 116);
border-radius: 12px;
color: white;
text-align: center;
}

QProgressBar::chunk{
border-radius: 12px;
	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:0, stop:0 rgba(179, 65, 149), stop:1 rgba(179, 65, 244, 255));
}</string>
    </property>
    <property name="value">
     <number>0</number>
    </property>
   </widget>
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>6</x>
      <y>2</y>
      <width>361</width>
      <height>251</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">border-image:url(:/pictures/IMG_20231008_160145_933.jpg);
border-radius: 20px;</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>16</x>
      <y>103</y>
      <width>341</width>
      <height>121</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgba(0, 0, 0, 100);
border-radius: 10px;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>80</x>
      <y>170</y>
      <width>201</width>
      <height>41</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
background-color: rgba(0,0,0,0);
border: 2px solid rgba(255, 33, 100, 230);
border-radius: 10px;
padding: 10px;
font-size: 10pt;
color: rgba(255, 255, 255, 200);
}

QPushButton:hover {
background-color: rgba(255,33,100,100);
}</string>
    </property>
    <property name="text">
     <string>Запустить</string>
    </property>
   </widget>
   <widget class="QCheckBox" name="checkBox">
    <property name="geometry">
     <rect>
      <x>50</x>
      <y>120</y>
      <width>261</width>
      <height>40</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
      <weight>50</weight>
      <bold>false</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QCheckBox {
background-color: rgba(0,0,0,0);
border: 2px solid rgba(255, 33, 100, 230);
border-radius: 10px;
padding: 10px;
font-size: 10pt;
color: white;
}

QCheckBox:hover {
background-color: rgba(255,33,100,100);
}</string>
    </property>
    <property name="text">
     <string>Запустить по завершению загрузки</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>150</x>
      <y>20</y>
      <width>71</width>
      <height>21</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: white;
background-color: rgba(0, 0, 0, 100);
border-radius: 10px;</string>
    </property>
    <property name="text">
     <string>Загрузка</string>
    </property>
   </widget>
   <zorder>label</zorder>
   <zorder>progressBar</zorder>
   <zorder>label_2</zorder>
   <zorder>pushButton</zorder>
   <zorder>checkBox</zorder>
   <zorder>label_3</zorder>
  </widget>
 </widget>
 <resources>
  <include location="res.qrc"/>
 </resources>
 <connections/>
</ui>
"""
MainWindowTemplate = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1170</width>
    <height>800</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>1008</width>
    <height>800</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>1200</width>
    <height>800</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QWidget" name="widget" native="true">
   <property name="geometry">
    <rect>
     <x>30</x>
     <y>10</y>
     <width>1031</width>
     <height>741</height>
    </rect>
   </property>
   <widget class="QLabel" name="background">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>1031</width>
      <height>741</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">border-image:url(:/pictures/images.jpg);
border-radius: 20px;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="settings">
    <property name="geometry">
     <rect>
      <x>941</x>
      <y>35</y>
      <width>70</width>
      <height>70</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton{
border-radius: 35px;
}

QPushButton:hover {
background-color: rgba(255,33,100,100);
}
</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="settingsLabel">
    <property name="geometry">
     <rect>
      <x>936</x>
      <y>30</y>
      <width>81</width>
      <height>81</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">border-image:url(:/pictures/Без названия (2).png);
border-radius: 37px;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="currencyConverter">
    <property name="geometry">
     <rect>
      <x>739</x>
      <y>27</y>
      <width>181</width>
      <height>90</height>
     </rect>
    </property>
    <property name="minimumSize">
     <size>
      <width>90</width>
      <height>90</height>
     </size>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton{
border-radius: 45px;
background-color: rgb(44, 109, 168);
color: white;
}

QPushButton:hover {
background-color: rgba(255,33,100, 100);
}
</string>
    </property>
    <property name="text">
     <string>Конвертатор валют</string>
    </property>
   </widget>
   <widget class="QLabel" name="currencyConverterLabel">
    <property name="geometry">
     <rect>
      <x>730</x>
      <y>20</y>
      <width>198</width>
      <height>104</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
border-radius:50px</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="expenseManager">
    <property name="geometry">
     <rect>
      <x>329</x>
      <y>27</y>
      <width>181</width>
      <height>90</height>
     </rect>
    </property>
    <property name="minimumSize">
     <size>
      <width>90</width>
      <height>90</height>
     </size>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton{
border-radius: 45px;
background-color: rgb(44, 109, 168);
color: white;
}

QPushButton:hover {
background-color: rgba(255,33,100,100);
}
</string>
    </property>
    <property name="text">
     <string>Менеджер расходов</string>
    </property>
   </widget>
   <widget class="QLabel" name="expenseManagerLabel">
    <property name="geometry">
     <rect>
      <x>320</x>
      <y>20</y>
      <width>198</width>
      <height>104</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
border-radius:50px</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="revenueManager">
    <property name="geometry">
     <rect>
      <x>124</x>
      <y>27</y>
      <width>181</width>
      <height>90</height>
     </rect>
    </property>
    <property name="minimumSize">
     <size>
      <width>90</width>
      <height>90</height>
     </size>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton{
border-radius: 45px;
background-color: rgb(44, 109, 168);
color: white;
}

QPushButton:hover {
background-color: rgba(255,33,100,100);
}
</string>
    </property>
    <property name="text">
     <string>Менеджер доходов</string>
    </property>
   </widget>
   <widget class="QLabel" name="revenueManagerLabel">
    <property name="geometry">
     <rect>
      <x>115</x>
      <y>20</y>
      <width>198</width>
      <height>104</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
border-radius:50px</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="goalPlanner">
    <property name="geometry">
     <rect>
      <x>534</x>
      <y>27</y>
      <width>181</width>
      <height>90</height>
     </rect>
    </property>
    <property name="minimumSize">
     <size>
      <width>90</width>
      <height>90</height>
     </size>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton{
border-radius: 45px;
background-color: rgb(44, 109, 168);
color: white;
}

QPushButton:hover {
background-color: rgba(255,33,100,100);
}
</string>
    </property>
    <property name="text">
     <string>Планировщик целей</string>
    </property>
   </widget>
   <widget class="QLabel" name="goalPlannerManager">
    <property name="geometry">
     <rect>
      <x>525</x>
      <y>20</y>
      <width>198</width>
      <height>104</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
border-radius:50px</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="mainMenu">
    <property name="geometry">
     <rect>
      <x>16</x>
      <y>27</y>
      <width>85</width>
      <height>85</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton{
border-radius: 42px;
}

QPushButton:hover {
background-color: rgba(255,33,100,100);
}
</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="mainMenuLabel">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>20</y>
      <width>100</width>
      <height>100</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">border-image:url(:/pictures/Иконка приложения.png);
border-radius: 45px;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QWidget" name="MainMenu" native="true">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>160</y>
      <width>971</width>
      <height>550</height>
     </rect>
    </property>
    <widget class="QLabel" name="MainMenuPlace">
     <property name="geometry">
      <rect>
       <x>0</x>
       <y>0</y>
       <width>971</width>
       <height>551</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">background-color: rgba(0, 0, 0, 150);
border-radius: 10px;</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
    <widget class="QLabel" name="avatarFrame">
     <property name="geometry">
      <rect>
       <x>40</x>
       <y>50</y>
       <width>151</width>
       <height>151</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">border-image: url(:/pictures/Рамка для аватарки.png)</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
    <widget class="QLabel" name="avatar">
     <property name="geometry">
      <rect>
       <x>55</x>
       <y>65</y>
       <width>122</width>
       <height>122</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">border-image:url(:/pictures/images.jpg)</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
    <widget class="QLabel" name="login">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>202</y>
       <width>190</width>
       <height>51</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial</family>
       <pointsize>12</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">border-radius: 15px;
color: white;
background-color:rgba(44, 109, 168, 210);
border: 5px solid rgba(255, 255, 255, 250);</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
    <widget class="QPushButton" name="editProfile">
     <property name="geometry">
      <rect>
       <x>45</x>
       <y>272</y>
       <width>144</width>
       <height>51</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial</family>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton{
border-radius: 15px;
color: white;
background-color:rgba(44, 109, 168, 210);
border: 5px solid rgba(255, 255, 255, 250);
}

QPushButton:hover {
background-color: rgbargba(44, 109, 168, 150);
}</string>
     </property>
     <property name="text">
      <string>Изменить профиль</string>
     </property>
    </widget>
    <widget class="QLabel" name="balance">
     <property name="geometry">
      <rect>
       <x>450</x>
       <y>65</y>
       <width>491</width>
       <height>122</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial</family>
       <pointsize>18</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">border-radius: 15px;
color: white;
background-color:rgba(44, 109, 168, 210);
border: 5px solid rgba(255, 255, 255, 250);</string>
     </property>
     <property name="text">
      <string/>
     </property>
    </widget>
    <widget class="QTableWidget" name="recentTransactions">
     <property name="geometry">
      <rect>
       <x>450</x>
       <y>260</y>
       <width>491</width>
       <height>271</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">border-radius: 15px;
color: white;
background-color:rgba(44, 109, 168, 210);
border: 5px solid rgba(255, 255, 255, 250);</string>
     </property>
    </widget>
    <widget class="QLabel" name="recentTransactionLabel">
     <property name="geometry">
      <rect>
       <x>450</x>
       <y>201</y>
       <width>491</width>
       <height>51</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial</family>
       <pointsize>12</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="focusPolicy">
      <enum>Qt::NoFocus</enum>
     </property>
     <property name="styleSheet">
      <string notr="true">border-radius: 15px;
color: white;
background-color:rgba(44, 109, 168, 210);
border: 5px solid rgba(255, 255, 255, 250);</string>
     </property>
     <property name="text">
      <string>Последние 10 транзакций</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QLabel" name="userInformation">
     <property name="geometry">
      <rect>
       <x>220</x>
       <y>65</y>
       <width>221</width>
       <height>465</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial</family>
       <pointsize>12</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">border-radius: 15px;
color: white;
background-color:rgba(44, 109, 168, 210);
border: 5px solid rgba(255, 255, 255, 250);</string>
     </property>
     <property name="text">
      <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;br/&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignTop</set>
     </property>
    </widget>
    <widget class="QLabel" name="MainMenuLabel">
     <property name="geometry">
      <rect>
       <x>320</x>
       <y>10</y>
       <width>331</width>
       <height>51</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial</family>
       <pointsize>24</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">color: white;</string>
     </property>
     <property name="text">
      <string>Главное меню</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
   </widget>
   <zorder>background</zorder>
   <zorder>mainMenuLabel</zorder>
   <zorder>currencyConverterLabel</zorder>
   <zorder>settingsLabel</zorder>
   <zorder>settings</zorder>
   <zorder>expenseManagerLabel</zorder>
   <zorder>revenueManagerLabel</zorder>
   <zorder>goalPlannerManager</zorder>
   <zorder>revenueManager</zorder>
   <zorder>expenseManager</zorder>
   <zorder>currencyConverter</zorder>
   <zorder>goalPlanner</zorder>
   <zorder>mainMenu</zorder>
   <zorder>MainMenu</zorder>
  </widget>
 </widget>
 <resources>
  <include location="res.qrc"/>
 </resources>
 <connections/>
</ui>
"""
settingsTemplate = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>747</width>
    <height>603</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QWidget" name="widget" native="true">
   <property name="geometry">
    <rect>
     <x>130</x>
     <y>90</y>
     <width>481</width>
     <height>391</height>
    </rect>
   </property>
   <widget class="QLabel" name="background">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>461</width>
      <height>371</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">border-image:url(:/pictures/Картинка для настроек.jpg);
border-radius: 20px;
</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="border">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>481</width>
      <height>391</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color:rgb(44, 109, 168);
border-radius: 20px;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="settingText">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>30</y>
      <width>111</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>16</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgba(0, 0, 0, 150);
border-radius: 10px;
color: white;</string>
    </property>
    <property name="text">
     <string>Настройки</string>
    </property>
   </widget>
   <widget class="QLabel" name="placeForText">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>90</y>
      <width>421</width>
      <height>261</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>16</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgba(0, 0, 0, 150);
border-radius: 10px;
color: white;</string>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="disableAutomaticLoginLabel">
    <property name="geometry">
     <rect>
      <x>56</x>
      <y>112</y>
      <width>231</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: white;</string>
    </property>
    <property name="text">
     <string>Отключить автоматический вход</string>
    </property>
   </widget>
   <widget class="QPushButton" name="disableAutomaticLoginButton">
    <property name="geometry">
     <rect>
      <x>330</x>
      <y>108</y>
      <width>111</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
background-color: rgba(0,0,0,0);
border: 2px solid rgba(255, 33, 100, 230);
border-radius: 10px;

color: rgba(255, 255, 255, 200);
}

QPushButton:hover {
background-color: rgba(255,33,100,100);
}</string>
    </property>
    <property name="text">
     <string>Отключить</string>
    </property>
   </widget>
   <widget class="QPushButton" name="exitButton">
    <property name="geometry">
     <rect>
      <x>370</x>
      <y>300</y>
      <width>71</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>12</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="toolTip">
     <string/>
    </property>
    <property name="toolTipDuration">
     <number>1</number>
    </property>
    <property name="statusTip">
     <string/>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
background-color: rgba(0,0,0,0);
border: 2px solid rgba(255, 33, 100, 230);
border-radius: 10px;

color: rgba(255, 255, 255, 200);
}

QPushButton:hover {
background-color: rgba(255,33,100,150);
}</string>
    </property>
    <property name="text">
     <string>Выход</string>
    </property>
   </widget>
   <widget class="QLabel" name="disableAutomaticLoginLabel_2">
    <property name="geometry">
     <rect>
      <x>56</x>
      <y>300</y>
      <width>231</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Arial</family>
      <pointsize>10</pointsize>
      <weight>75</weight>
      <bold>true</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">color: white;</string>
    </property>
    <property name="text">
     <string>Выйти из программы</string>
    </property>
   </widget>
   <widget class="QPushButton" name="closeSettingsButton">
    <property name="geometry">
     <rect>
      <x>420</x>
      <y>20</y>
      <width>41</width>
      <height>41</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <pointsize>10</pointsize>
     </font>
    </property>
    <property name="toolTip">
     <string/>
    </property>
    <property name="toolTipDuration">
     <number>1</number>
    </property>
    <property name="styleSheet">
     <string notr="true">QPushButton {
background-color: rgba(255,33,100,150);
border: 2px solid rgba(255, 33, 100, 230);
border-radius: 10px;
padding: 10px;
font-size: 10pt;
color: rgba(255, 255, 255, 200);
}

QPushButton:hover {
background-color: rgba(255,33,100,100);
}</string>
    </property>
    <property name="text">
     <string>X</string>
    </property>
   </widget>
   <zorder>border</zorder>
   <zorder>background</zorder>
   <zorder>settingText</zorder>
   <zorder>placeForText</zorder>
   <zorder>disableAutomaticLoginLabel</zorder>
   <zorder>disableAutomaticLoginButton</zorder>
   <zorder>exitButton</zorder>
   <zorder>disableAutomaticLoginLabel_2</zorder>
   <zorder>closeSettingsButton</zorder>
  </widget>
 </widget>
 <resources>
  <include location="res.qrc"/>
 </resources>
 <connections/>
</ui>
"""
errorDisableAutomaticLoginTemplate = """<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>520</width>
    <height>417</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <widget class="QLabel" name="border">
   <property name="geometry">
    <rect>
     <x>110</x>
     <y>120</y>
     <width>321</width>
     <height>180</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color:rgb(44, 109, 168);
border-radius: 20px;</string>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QLabel" name="placeForText">
   <property name="geometry">
    <rect>
     <x>120</x>
     <y>130</y>
     <width>301</width>
     <height>161</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>16</pointsize>
     <weight>75</weight>
     <bold>true</bold>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: rgba(0, 0, 0, 150);
border-radius: 35px;
color: white;</string>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <widget class="QPushButton" name="exitFromError">
   <property name="geometry">
    <rect>
     <x>230</x>
     <y>230</y>
     <width>71</width>
     <height>41</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>12</pointsize>
     <weight>75</weight>
     <bold>true</bold>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">QPushButton {
background-color: rgba(0,0,0,0);
border: 2px solid rgba(255, 33, 100, 230);
border-radius: 10px;

color: rgba(255, 255, 255, 200);
}

QPushButton:hover {
background-color: rgba(255,33,100,150);
}</string>
   </property>
   <property name="text">
    <string>Ок</string>
   </property>
  </widget>
  <widget class="QLabel" name="errorText">
   <property name="geometry">
    <rect>
     <x>150</x>
     <y>150</y>
     <width>261</width>
     <height>51</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Arial</family>
     <pointsize>10</pointsize>
     <weight>75</weight>
     <bold>true</bold>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">color: white;</string>
   </property>
   <property name="text">
    <string>Автоматический вход уже выключен</string>
   </property>
  </widget>
  <widget class="QLabel" name="background">
   <property name="geometry">
    <rect>
     <x>120</x>
     <y>130</y>
     <width>301</width>
     <height>161</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">border-image:url(:/pictures/ErrorBackground.jpg);
border-radius: 9px;</string>
   </property>
   <property name="text">
    <string/>
   </property>
  </widget>
  <zorder>border</zorder>
  <zorder>background</zorder>
  <zorder>placeForText</zorder>
  <zorder>exitFromError</zorder>
  <zorder>errorText</zorder>
 </widget>
 <resources>
  <include location="res.qrc"/>
 </resources>
 <connections/>
</ui>
"""
class RegistrationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(ReLogWindow)
        uic.loadUi(f, self)
        self.BackgroundUpdate(NAME)
        self.WindowTransparency()
        con = sqlite3.connect('RecordedLoginAndPassword')
        cur = con.cursor()
        data = cur.execute("""SELECT * FROM loginpassword WHERE id = '1'""").fetchall()
        if data:
            self.enterLogin.setText(data[-1][1])
            self.enterPassword.setText(data[-1][2])
            self.reminderButton.setChecked(True)
        con.close()
        self.logButton.clicked.connect(self.log)
        self.regButton.clicked.connect(self.reg)
        self.closeWindowButton.clicked.connect(self.closeWindow)

    def BackgroundUpdate(self, fileName):
        self.label.setStyleSheet("""border-image: url(:/picture/F8fDYJzboAAbCup.png);
        border-radius: 35px""")

    def WindowTransparency(self):
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def log(self):
        if self.enterPassword.text() == '' and self.enterLogin.text() == '':
            self.ReLogResult.setText('Введите логин и пароль')
        elif self.enterPassword.text() != '' and self.enterLogin.text() == '':
            self.ReLogResult.setText('Введите логин')
        elif self.enterPassword.text() == '' and self.enterLogin.text() != '':
            self.ReLogResult.setText('Введите пароль')
        else:
            self.login = self.enterLogin.text()
            con = sqlite3.connect('LoginsAndPasswords')
            cur = con.cursor()
            LoginAndPassword = cur.execute(f"""SELECT * FROM logpass WHERE
             login = '{self.enterLogin.text()}'""").fetchall()
            if LoginAndPassword != [] and LoginAndPassword[0][1] == self.enterPassword.text():
                con1 = sqlite3.connect('RecordedLoginAndPassword')
                cur1 = con1.cursor()
                if self.reminderButton.isChecked():
                    login = self.enterLogin.text()
                    passw = self.enterPassword.text()
                    cur1.execute(f"INSERT INTO loginpassword (id,login,password) VALUES('1', '{login}', '{passw}')")
                    con1.commit()
                    con1.close
                    self.GoEnd()
                else:
                    cur1.execute("""DELETE FROM loginpassword WHERE id = '1'""")
                    a = cur1.execute("""SELECT * FROM loginpassword""").fetchall()
                    con1.commit()
                    con1.close()
                    self.GoEnd()
            else:
                self.ReLogResult.setText('Неверный логин или пароль')
            con.close()

    def reg(self):
        if self.enterPassword.text() == '' and self.enterLogin.text() == '':
            self.ReLogResult.setText('Введите логин и пароль')
        elif self.enterPassword.text() != '' and self.enterLogin.text() == '':
            self.ReLogResult.setText('Введите логин')
        elif self.enterPassword.text() == '' and self.enterLogin.text() != '':
            self.ReLogResult.setText('Введите пароль')
        else:
            con = sqlite3.connect('LoginsAndPasswords')
            cur = con.cursor()
            logins = cur.execute(f"""SELECT login FROM logpass WHERE login = '{self.enterLogin.text()}'""").fetchall()
            passwords = (cur.execute(f"""SELECT password FROM logpass
             WHERE password = '{self.enterPassword.text()}'""").fetchall())
            if logins and not passwords:
                self.ReLogResult.setText('Данный логин занят')
                self.enterLogin.setText('')
            elif not logins and passwords:
                self.ReLogResult.setText('Данный пароль занят')
                self.enterPassword.setText('')
            elif logins and passwords:
                self.ReLogResult.setText('Данные логин и пароль заняты')
                self.enterLogin.setText('')
                self.enterPassword.setText('')
            elif len(self.enterLogin.text()) > 14:
                self.ReLogResult.setText('Логин слишком длинный')
                self.enterLogin.setText('')
            else:
                self.login = self.enterLogin.text()
                passw = self.enterPassword.text()
                date = datetime.datetime.now().date()
                zero = 0
                con1 = sqlite3.connect('UsersInformat')
                cur1 = con1.cursor()
                cur1.execute(f"INSERT INTO inf (username, balance, numberofauthorizations, registrationdate,"
                             f" daysintheapp, numberoftransactions) VALUES('{self.login}', '0', '0', '{date}', '0', '0')")
                con1.commit()
                cur.execute(f"INSERT INTO logpass (login,password) VALUES('{self.login}', '{passw}')")
                con.commit()
                self.ReLogResult.setText('Вы успешно зарегистрировались!')
            con.close()

    def GoEnd(self):
        self.hide()
        self.app2 = LoadingWindow(self.login)
        self.app2.show()

    def closeWindow(self):
        sys.exit(app.exec_())

class LoadingWindow(QMainWindow):
    def __init__(self, login):
        self.login = login
        super().__init__()
        f = io.StringIO(LoadWindow)
        uic.loadUi(f, self)
        self.endLoad = False
        self.n = 100
        self.initUi()

    def initUi(self):
        f = io.StringIO(LoadWindow)
        uic.loadUi(f, self)
        self.BackgroundUpdate(NAME)
        self.WindowTransparency()
        self.timer = QtCore.QTimer()
        with open('LoadCheckbox.txt', mode='r', encoding='UTF-8') as file:
            data = file.read()
        if data == 'True':
            self.checkBox.setChecked(True)
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.run)
        QtCore.QTimer.singleShot(100, self.timer.start)
        self.pushButton.clicked.connect(self.GoEnd)

    def run(self):
        for i in range(self.n):
            time.sleep(0.01)
            self.progressBar.setValue(i + 1)
        self.timer.stop()
        if self.checkBox.isChecked():
            self.GoEnd()

    def BackgroundUpdate(self, fileName):
        self.label.setStyleSheet("""border-image: url(:/pictures/IMG_20231008_160145_933.jpg);
                border-radius: 35px""")

    def WindowTransparency(self):
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def GoEnd(self):
        if self.checkBox.isChecked():
            with open('LoadCheckbox.txt', mode='w', encoding='UTF-8') as file:
                file.write('True')
        con1 = sqlite3.connect('UsersInformat')
        cur1 = con1.cursor()
        count = cur1.execute(f"SELECT numberofauthorizations FROM inf WHERE username = '{self.login}'").fetchall()[0][0]
        count = int(count) + 1
        cur1.execute(f"UPDATE inf SET numberofauthorizations = {count} WHERE username = '{self.login}'")
        con1.commit()
        con1.close()
        self.hide()
        self.app2 = MainWindow(self.login)
        self.app2.show()