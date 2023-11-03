import sys
import io
import time
from datetime import datetime
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from FilesForImportingImages.res_rc2 import *
from FilesForImportingImages.res_rc1 import *
from FilesForImportingImages.res_rc4 import *
from FilesForImportingImages.res_rc3 import *
from FilesForImportingImages.res_rc import *
from OtherFiles import *
from openpyxl import load_workbook
from openpyxl.writer.excel import save_workbook
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
    <width>1093</width>
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
  <property name="font">
   <font>
    <family>Arial</family>
    <pointsize>10</pointsize>
    <weight>75</weight>
    <bold>true</bold>
   </font>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <property name="styleSheet">
   <string notr="true"/>
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
   <property name="minimumSize">
    <size>
     <width>1031</width>
     <height>741</height>
    </size>
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
     <string>Конвертатор
валют</string>
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
     <string>Менеджер
расходов</string>
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
     <string>Менеджер
доходов</string>
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
     <string>Планировщик
целей</string>
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
    <property name="autoFillBackground">
     <bool>false</bool>
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
      <width>961</width>
      <height>550</height>
     </rect>
    </property>
    <widget class="QLabel" name="MainMenuPlace">
     <property name="geometry">
      <rect>
       <x>0</x>
       <y>0</y>
       <width>961</width>
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
      <string>Изменить
профиль</string>
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
      <string notr="true">color: black;
background-color:rgba(44, 109, 168, 210);
</string>
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
   <widget class="QWidget" name="revenueManagerMenu" native="true">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>160</y>
      <width>961</width>
      <height>550</height>
     </rect>
    </property>
    <widget class="QLabel" name="revenueManagerPlace">
     <property name="geometry">
      <rect>
       <x>0</x>
       <y>0</y>
       <width>961</width>
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
    <widget class="QLabel" name="revenueMenuLabel">
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
      <string>Менеджер доходов</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QLabel" name="revenueHistoryLabel">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>70</y>
       <width>421</width>
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
     <property name="styleSheet">
      <string notr="true">border-radius: 15px;
color: white;
background-color:rgba(34, 139, 34, 210);
border: 5px solid rgba(255, 255, 255, 250);</string>
     </property>
     <property name="text">
      <string>История доходов</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QTableWidget" name="revenueTransactions">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>150</y>
       <width>421</width>
       <height>381</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">color: black;
background-color:rgba(34, 139, 34, 210);
</string>
     </property>
    </widget>
    <widget class="QLabel" name="sortRevenueLabel">
     <property name="geometry">
      <rect>
       <x>36</x>
       <y>115</y>
       <width>111</width>
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
      <string>Сортировать по</string>
     </property>
    </widget>
    <widget class="QComboBox" name="sortRevenueParameter">
     <property name="geometry">
      <rect>
       <x>150</x>
       <y>120</y>
       <width>121</width>
       <height>22</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">border: 5px solid rgba(255, 255, 255, 250);</string>
     </property>
     <item>
      <property name="text">
       <string>Дата</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>Категория</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>От максимального</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>От минимального</string>
      </property>
     </item>
    </widget>
    <widget class="QPushButton" name="updateRevenueButton">
     <property name="geometry">
      <rect>
       <x>300</x>
       <y>117</y>
       <width>111</width>
       <height>26</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton{
color: white;
background-color:rgba(34, 139, 34, 210);
border: 3px solid rgba(255, 255, 255, 250);
}

QPushButton:hover {
background-color:rgba(34, 139, 34, 100);
}</string>
     </property>
     <property name="text">
      <string>Обновить</string>
     </property>
    </widget>
    <widget class="QLabel" name="addRevenueLabel">
     <property name="geometry">
      <rect>
       <x>510</x>
       <y>70</y>
       <width>391</width>
       <height>41</height>
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
      <string>Добавление доходов</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QLabel" name="revenueSummaLabel">
     <property name="geometry">
      <rect>
       <x>600</x>
       <y>110</y>
       <width>211</width>
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
      <string notr="true">border-radius: 15px;
color: white;
background-color:rgba(34, 139, 34, 210);
border: 5px solid rgba(255, 255, 255, 250);</string>
     </property>
     <property name="text">
      <string>Сумма</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QLineEdit" name="revenueSummaEnter">
     <property name="geometry">
      <rect>
       <x>542</x>
       <y>159</y>
       <width>331</width>
       <height>41</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">color: rgba(255, 255, 255, 150);
background-color:rgba(34, 139, 34, 210);
border: 2px solid rgba(255, 255, 255, 250);</string>
     </property>
     <property name="text">
      <string/>
     </property>
     <property name="placeholderText">
      <string>Например (3125)</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="revenueCategoryEnter">
     <property name="geometry">
      <rect>
       <x>542</x>
       <y>259</y>
       <width>331</width>
       <height>41</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">color: rgba(255, 255, 255, 150);
background-color:rgba(34, 139, 34, 210);
border: 2px solid rgba(255, 255, 255, 250);</string>
     </property>
     <property name="text">
      <string/>
     </property>
     <property name="placeholderText">
      <string>Например (Зарплата, перевод)</string>
     </property>
    </widget>
    <widget class="QLabel" name="revenueCategoryLabel">
     <property name="geometry">
      <rect>
       <x>600</x>
       <y>210</y>
       <width>211</width>
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
      <string notr="true">border-radius: 15px;
color: white;
background-color:rgba(34, 139, 34, 210);
border: 5px solid rgba(255, 255, 255, 250);</string>
     </property>
     <property name="text">
      <string>Категория</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QLineEdit" name="revenueSourceEnter">
     <property name="geometry">
      <rect>
       <x>542</x>
       <y>359</y>
       <width>331</width>
       <height>41</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">color: rgba(255, 255, 255, 150);
background-color:rgba(34, 139, 34, 210);
border: 2px solid rgba(255, 255, 255, 250);</string>
     </property>
     <property name="text">
      <string/>
     </property>
     <property name="placeholderText">
      <string>Например (Работа, бизнес)</string>
     </property>
    </widget>
    <widget class="QLabel" name="revenueSourceLabel">
     <property name="geometry">
      <rect>
       <x>600</x>
       <y>310</y>
       <width>211</width>
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
      <string notr="true">border-radius: 15px;
color: white;
background-color:rgba(34, 139, 34, 210);
border: 5px solid rgba(255, 255, 255, 250);</string>
     </property>
     <property name="text">
      <string>Источник дохода</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QPushButton" name="addRevenue">
     <property name="geometry">
      <rect>
       <x>610</x>
       <y>410</y>
       <width>191</width>
       <height>41</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial</family>
       <pointsize>14</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton{
color: white;
background-color:rgba(34, 139, 34, 210);
border: 3px solid rgba(255, 255, 255, 250);
}

QPushButton:hover {
background-color:rgba(34, 139, 34, 100);
}</string>
     </property>
     <property name="text">
      <string>Добавить</string>
     </property>
    </widget>
    <widget class="QPushButton" name="createRevenueFileGraphicDiagramButton">
     <property name="geometry">
      <rect>
       <x>480</x>
       <y>470</y>
       <width>451</width>
       <height>51</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial</family>
       <pointsize>14</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton{
color: white;
background-color:rgba(34, 139, 34, 210);
border: 3px solid rgba(255, 255, 255, 250);
}

QPushButton:hover {
background-color:rgba(34, 139, 34, 100);
}</string>
     </property>
     <property name="text">
      <string>Создать файл/график/диаграмму</string>
     </property>
    </widget>
    <widget class="QLabel" name="addRevenueErrorLabel">
     <property name="geometry">
      <rect>
       <x>670</x>
       <y>20</y>
       <width>271</width>
       <height>41</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial Black</family>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">color: white;</string>
     </property>
     <property name="text">
      <string>TextLabel</string>
     </property>
    </widget>
   </widget>
   <widget class="QWidget" name="expenseManagerMenu" native="true">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>160</y>
      <width>961</width>
      <height>550</height>
     </rect>
    </property>
    <widget class="QLabel" name="expenseManagerPlace">
     <property name="geometry">
      <rect>
       <x>0</x>
       <y>0</y>
       <width>961</width>
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
    <widget class="QLabel" name="expenseMenuLabel">
     <property name="geometry">
      <rect>
       <x>320</x>
       <y>10</y>
       <width>331</width>
       <height>50</height>
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
      <string>Менеджер расходов</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QLabel" name="expenseHistoryLabel">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>70</y>
       <width>421</width>
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
     <property name="styleSheet">
      <string notr="true">border-radius: 15px;
color: white;
background-color:rgba(178, 34, 34, 210);
border: 5px solid rgba(255, 255, 255, 250);</string>
     </property>
     <property name="text">
      <string>История расходов</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QTableWidget" name="expenseTransactions">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>150</y>
       <width>421</width>
       <height>381</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">color: black;
background-color:rgba(178, 34, 34, 210);
</string>
     </property>
    </widget>
    <widget class="QLabel" name="sortExpenseLabel">
     <property name="geometry">
      <rect>
       <x>36</x>
       <y>115</y>
       <width>111</width>
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
      <string>Сортировать по</string>
     </property>
    </widget>
    <widget class="QComboBox" name="sortExpenseParameter">
     <property name="geometry">
      <rect>
       <x>150</x>
       <y>120</y>
       <width>141</width>
       <height>22</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">border: 5px solid rgba(255, 255, 255, 250);</string>
     </property>
     <property name="frame">
      <bool>true</bool>
     </property>
     <item>
      <property name="text">
       <string>Дата</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>Категория</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>От максимальной суммы</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>От минимальной суммы</string>
      </property>
     </item>
     <item>
      <property name="text">
       <string>Источник </string>
      </property>
     </item>
    </widget>
    <widget class="QPushButton" name="updateExpenseButton">
     <property name="geometry">
      <rect>
       <x>300</x>
       <y>118</y>
       <width>111</width>
       <height>26</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton{
color: white;
background-color:rgba(178, 34, 34, 210);
border: 3px solid rgba(255, 255, 255, 250);
}

QPushButton:hover {
background-color:rgba(178, 34, 34, 100);
}</string>
     </property>
     <property name="text">
      <string>Обновить</string>
     </property>
    </widget>
    <widget class="QLabel" name="addExpenseLabel">
     <property name="geometry">
      <rect>
       <x>510</x>
       <y>70</y>
       <width>391</width>
       <height>41</height>
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
      <string>Добавление расходов</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QLabel" name="expenseSummaLabel">
     <property name="geometry">
      <rect>
       <x>600</x>
       <y>110</y>
       <width>211</width>
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
      <string notr="true">border-radius: 15px;
color: white;
background-color:rgba(178, 34, 34, 210);
border: 5px solid rgba(255, 255, 255, 250);</string>
     </property>
     <property name="text">
      <string>Сумма</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QLineEdit" name="expenseSummaEnter">
     <property name="geometry">
      <rect>
       <x>542</x>
       <y>159</y>
       <width>331</width>
       <height>41</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">color: rgba(255, 255, 255, 150);
background-color:rgba(178, 34, 34, 210);
border: 2px solid rgba(255, 255, 255, 250);</string>
     </property>
     <property name="text">
      <string/>
     </property>
     <property name="placeholderText">
      <string>Например (3125)</string>
     </property>
    </widget>
    <widget class="QLineEdit" name="expenseCategoryEnter">
     <property name="geometry">
      <rect>
       <x>542</x>
       <y>259</y>
       <width>331</width>
       <height>41</height>
      </rect>
     </property>
     <property name="accessibleName">
      <string/>
     </property>
     <property name="autoFillBackground">
      <bool>false</bool>
     </property>
     <property name="styleSheet">
      <string notr="true">color: rgba(255, 255, 255, 150);
background-color:rgba(178, 34, 34, 210);
border: 2px solid rgba(255, 255, 255, 250);</string>
     </property>
     <property name="inputMask">
      <string/>
     </property>
     <property name="text">
      <string notr="true"/>
     </property>
     <property name="placeholderText">
      <string>Например (Покупка, перевод)</string>
     </property>
    </widget>
    <widget class="QLabel" name="expenseCategoryLabel">
     <property name="geometry">
      <rect>
       <x>600</x>
       <y>210</y>
       <width>211</width>
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
      <string notr="true">border-radius: 15px;
color: white;
background-color:rgba(178, 34, 34, 210);
border: 5px solid rgba(255, 255, 255, 250);</string>
     </property>
     <property name="text">
      <string>Категория</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QLineEdit" name="expenseSourceEnter">
     <property name="geometry">
      <rect>
       <x>542</x>
       <y>359</y>
       <width>331</width>
       <height>41</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">color: rgba(255, 255, 255, 150);
background-color:rgba(178, 34, 34, 210);
border: 2px solid rgba(255, 255, 255, 250);</string>
     </property>
     <property name="text">
      <string/>
     </property>
     <property name="placeholderText">
      <string>Например (Интернет-магазин, магазин одежды)</string>
     </property>
    </widget>
    <widget class="QLabel" name="expenseSourceLabel">
     <property name="geometry">
      <rect>
       <x>600</x>
       <y>310</y>
       <width>211</width>
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
      <string notr="true">border-radius: 15px;
color: white;
background-color:rgba(178, 34, 34, 210);
border: 5px solid rgba(255, 255, 255, 250);</string>
     </property>
     <property name="text">
      <string>Источник расходов</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QPushButton" name="addExpense">
     <property name="geometry">
      <rect>
       <x>610</x>
       <y>410</y>
       <width>191</width>
       <height>41</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial</family>
       <pointsize>14</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton{
color: white;
background-color:rgba(178, 34, 34, 210);
border: 3px solid rgba(255, 255, 255, 250);
}

QPushButton:hover {
background-color:rgba(178, 34, 34, 100);
}</string>
     </property>
     <property name="text">
      <string>Добавить</string>
     </property>
    </widget>
    <widget class="QPushButton" name="createExpenseFileGraphicDiagramButton">
     <property name="geometry">
      <rect>
       <x>480</x>
       <y>470</y>
       <width>451</width>
       <height>51</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial</family>
       <pointsize>14</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton{
color: white;
background-color:rgba(178, 34, 34, 210);
border: 3px solid rgba(255, 255, 255, 250);
}

QPushButton:hover {
background-color:rgba(178, 34, 34, 100);
}</string>
     </property>
     <property name="text">
      <string>Создать файл/график/диаграмму</string>
     </property>
    </widget>
    <widget class="QLabel" name="addExpenseErrorLabel">
     <property name="geometry">
      <rect>
       <x>670</x>
       <y>20</y>
       <width>271</width>
       <height>41</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial Black</family>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">color: white;</string>
     </property>
     <property name="text">
      <string>TextLabel</string>
     </property>
    </widget>
   </widget>
   <widget class="QWidget" name="goalPlannerMenu" native="true">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>160</y>
      <width>961</width>
      <height>551</height>
     </rect>
    </property>
    <widget class="QLabel" name="goalPlannerPlace">
     <property name="geometry">
      <rect>
       <x>0</x>
       <y>0</y>
       <width>961</width>
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
    <widget class="QLabel" name="goalPlannerLabel">
     <property name="geometry">
      <rect>
       <x>320</x>
       <y>10</y>
       <width>330</width>
       <height>50</height>
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
      <string>Планировщик целей</string>
     </property>
    </widget>
    <widget class="QProgressBar" name="goalProgress1">
     <property name="geometry">
      <rect>
       <x>70</x>
       <y>100</y>
       <width>311</width>
       <height>41</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial Black</family>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QProgressBar{
background-color: rgb(124, 113, 116);
border-radius: 12px;
color: white;
text-align: center;
border: 2px solid rgba(255, 255, 255, 250);
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
    <widget class="QLabel" name="goalProgressLabel1">
     <property name="geometry">
      <rect>
       <x>70</x>
       <y>60</y>
       <width>311</width>
       <height>41</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial Black</family>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">color: white;</string>
     </property>
     <property name="text">
      <string>Не используется</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QLabel" name="goalProgressLabel2">
     <property name="geometry">
      <rect>
       <x>70</x>
       <y>170</y>
       <width>311</width>
       <height>41</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial Black</family>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">color: white;</string>
     </property>
     <property name="text">
      <string>Не используется</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QProgressBar" name="goalProgress2">
     <property name="geometry">
      <rect>
       <x>70</x>
       <y>210</y>
       <width>311</width>
       <height>41</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial Black</family>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QProgressBar{
background-color: rgb(124, 113, 116);
border-radius: 12px;
color: white;
text-align: center;
border: 2px solid rgba(255, 255, 255, 250);
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
    <widget class="QLabel" name="goalProgressLabel3">
     <property name="geometry">
      <rect>
       <x>70</x>
       <y>280</y>
       <width>311</width>
       <height>41</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial Black</family>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">color: white;</string>
     </property>
     <property name="text">
      <string>Не используется</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QProgressBar" name="goalProgress3">
     <property name="geometry">
      <rect>
       <x>70</x>
       <y>320</y>
       <width>311</width>
       <height>41</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial Black</family>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QProgressBar{
background-color: rgb(124, 113, 116);
border-radius: 12px;
color: white;
text-align: center;
border: 2px solid rgba(255, 255, 255, 250);
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
    <widget class="QLabel" name="goalProgressLabel4">
     <property name="geometry">
      <rect>
       <x>70</x>
       <y>390</y>
       <width>311</width>
       <height>41</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial Black</family>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">color: white;</string>
     </property>
     <property name="text">
      <string>Не используется</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QProgressBar" name="goalProgress4">
     <property name="geometry">
      <rect>
       <x>70</x>
       <y>430</y>
       <width>311</width>
       <height>41</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial Black</family>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QProgressBar{
background-color: rgb(124, 113, 116);
border-radius: 12px;
color: white;
text-align: center;
border: 2px solid rgba(255, 255, 255, 250);
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
    <widget class="QLabel" name="goalProgressLabel5">
     <property name="geometry">
      <rect>
       <x>580</x>
       <y>60</y>
       <width>311</width>
       <height>41</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial Black</family>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">color: white;</string>
     </property>
     <property name="text">
      <string>Не используется</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QProgressBar" name="goalProgress5">
     <property name="geometry">
      <rect>
       <x>580</x>
       <y>100</y>
       <width>311</width>
       <height>41</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial Black</family>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QProgressBar{
background-color: rgb(124, 113, 116);
border-radius: 12px;
color: white;
text-align: center;
border: 2px solid rgba(255, 255, 255, 250);
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
    <widget class="QLabel" name="goalProgressLabel6">
     <property name="geometry">
      <rect>
       <x>580</x>
       <y>170</y>
       <width>311</width>
       <height>41</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial Black</family>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">color: white;</string>
     </property>
     <property name="text">
      <string>Не используется</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QProgressBar" name="goalProgress6">
     <property name="geometry">
      <rect>
       <x>580</x>
       <y>210</y>
       <width>311</width>
       <height>41</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial Black</family>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QProgressBar{
background-color: rgb(124, 113, 116);
border-radius: 12px;
color: white;
text-align: center;
border: 2px solid rgba(255, 255, 255, 250);
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
    <widget class="QLabel" name="goalProgressLabel7">
     <property name="geometry">
      <rect>
       <x>580</x>
       <y>280</y>
       <width>311</width>
       <height>41</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial Black</family>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">color: white;</string>
     </property>
     <property name="text">
      <string>Не используется</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QProgressBar" name="goalProgress7">
     <property name="geometry">
      <rect>
       <x>580</x>
       <y>320</y>
       <width>311</width>
       <height>41</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial Black</family>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QProgressBar{
background-color: rgb(124, 113, 116);
border-radius: 12px;
color: white;
text-align: center;
border: 2px solid rgba(255, 255, 255, 250);
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
    <widget class="QLabel" name="goalProgressLabel8">
     <property name="geometry">
      <rect>
       <x>580</x>
       <y>390</y>
       <width>311</width>
       <height>41</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial Black</family>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">color: white;</string>
     </property>
     <property name="text">
      <string>Не используется</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QProgressBar" name="goalProgress8">
     <property name="geometry">
      <rect>
       <x>580</x>
       <y>430</y>
       <width>311</width>
       <height>41</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial Black</family>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QProgressBar{
background-color: rgb(124, 113, 116);
border-radius: 12px;
color: white;
text-align: center;
border: 2px solid rgba(255, 255, 255, 250);
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
    <widget class="QPushButton" name="updateGoals">
     <property name="geometry">
      <rect>
       <x>410</x>
       <y>102</y>
       <width>141</width>
       <height>41</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial Black</family>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton{
border-radius: 10px;
background-color:qlineargradient(spread:reflect, x1:0, y1:0.011, x2:1, y2:0, stop:0 rgba(189, 36, 126, 243), stop:1 rgba(255, 255, 255, 255));
color: white;
border: 2px solid rgba(255, 33, 100, 230);
}

QPushButton:hover {
background-color: qlineargradient(spread:reflect, x1:0, y1:0.011, x2:1, y2:0, stop:0 rgba(189, 36, 126, 200), stop:1 rgba(255, 255, 255, 200));
}
</string>
     </property>
     <property name="text">
      <string>Обновить</string>
     </property>
    </widget>
    <widget class="QPushButton" name="createGoal">
     <property name="geometry">
      <rect>
       <x>410</x>
       <y>180</y>
       <width>141</width>
       <height>41</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial Black</family>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton{
border-radius: 10px;
background-color:qlineargradient(spread:reflect, x1:0, y1:0.011, x2:1, y2:0, stop:0 rgba(189, 36, 126, 243), stop:1 rgba(255, 255, 255, 255));
color: white;
border: 2px solid rgba(255, 33, 100, 230);
}

QPushButton:hover {
background-color: qlineargradient(spread:reflect, x1:0, y1:0.011, x2:1, y2:0, stop:0 rgba(189, 36, 126, 200), stop:1 rgba(255, 255, 255, 200));
}

</string>
     </property>
     <property name="text">
      <string>Создать</string>
     </property>
    </widget>
    <widget class="QPushButton" name="editGoal">
     <property name="geometry">
      <rect>
       <x>410</x>
       <y>260</y>
       <width>141</width>
       <height>41</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial Black</family>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton{
border-radius: 10px;
background-color:qlineargradient(spread:reflect, x1:0, y1:0.011, x2:1, y2:0, stop:0 rgba(189, 36, 126, 243), stop:1 rgba(255, 255, 255, 255));
color: white;
border: 2px solid rgba(255, 33, 100, 230);
}

QPushButton:hover {
background-color: qlineargradient(spread:reflect, x1:0, y1:0.011, x2:1, y2:0, stop:0 rgba(189, 36, 126, 200), stop:1 rgba(255, 255, 255, 200));
}

</string>
     </property>
     <property name="text">
      <string>Редактировать</string>
     </property>
    </widget>
    <widget class="QWidget" name="addGoal" native="true">
     <property name="geometry">
      <rect>
       <x>329</x>
       <y>49</y>
       <width>321</width>
       <height>461</height>
      </rect>
     </property>
     <property name="styleSheet">
      <string notr="true">border-radius: 10px;
background-color: qlineargradient(spread:reflect, x1:0, y1:0.011, x2:1, y2:0, stop:0 rgba(189, 36, 126, 243), stop:1 rgba(255, 255, 255, 255));</string>
     </property>
     <widget class="QLabel" name="addGoalLabel">
      <property name="geometry">
       <rect>
        <x>0</x>
        <y>30</y>
        <width>321</width>
        <height>41</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Arial Black</family>
        <pointsize>14</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="styleSheet">
       <string notr="true">color: white;</string>
      </property>
      <property name="text">
       <string>Создать цель</string>
      </property>
      <property name="alignment">
       <set>Qt::AlignCenter</set>
      </property>
     </widget>
     <widget class="QLabel" name="goalNameLabel">
      <property name="geometry">
       <rect>
        <x>0</x>
        <y>70</y>
        <width>321</width>
        <height>41</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Arial Black</family>
        <pointsize>14</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="styleSheet">
       <string notr="true">color: white;</string>
      </property>
      <property name="text">
       <string>Название</string>
      </property>
      <property name="alignment">
       <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
      </property>
     </widget>
     <widget class="QLabel" name="goalTargetLabel">
      <property name="geometry">
       <rect>
        <x>0</x>
        <y>150</y>
        <width>321</width>
        <height>41</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Arial Black</family>
        <pointsize>14</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="styleSheet">
       <string notr="true">color: white;</string>
      </property>
      <property name="text">
       <string>Цель</string>
      </property>
      <property name="alignment">
       <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
      </property>
     </widget>
     <widget class="QLabel" name="selectColorLabel">
      <property name="geometry">
       <rect>
        <x>0</x>
        <y>240</y>
        <width>321</width>
        <height>41</height>
       </rect>
      </property>
      <property name="font">
       <font>
        <family>Arial Black</family>
        <pointsize>14</pointsize>
        <weight>75</weight>
        <bold>true</bold>
       </font>
      </property>
      <property name="styleSheet">
       <string notr="true">color: white;</string>
      </property>
      <property name="text">
       <string>Цвет</string>
      </property>
      <property name="alignment">
       <set>Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter</set>
      </property>
     </widget>
     <widget class="QLineEdit" name="enterGoalName">
      <property name="geometry">
       <rect>
        <x>12</x>
        <y>115</y>
        <width>301</width>
        <height>41</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">QLineEdit {
background-color: rgba(0,0,0,0);
border: 2px solid rgba(255, 33, 100, 230);
border-radius: 3px;
padding: 10px;
font-size: 10pt;
color: rgba(255, 255, 255, 200);
}

</string>
      </property>
     </widget>
     <widget class="QLineEdit" name="enterGoalTarget">
      <property name="geometry">
       <rect>
        <x>10</x>
        <y>195</y>
        <width>301</width>
        <height>41</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">QLineEdit {
background-color: rgba(0,0,0,0);
border: 2px solid rgba(255, 33, 100, 230);
border-radius: 3px;
padding: 10px;
font-size: 10pt;
color: rgba(255, 255, 255, 200);
}

</string>
      </property>
     </widget>
     <widget class="QComboBox" name="selectColor">
      <property name="geometry">
       <rect>
        <x>20</x>
        <y>281</y>
        <width>171</width>
        <height>41</height>
       </rect>
      </property>
      <property name="styleSheet">
       <string notr="true">background-color: rgba(0,0,0,0);
border: 2px solid rgba(255, 33, 100, 230);
border-radius: 3px;
padding: 10px;
font-size: 10pt;
color: rgba(255, 255, 255, 200);</string>
      </property>
      <item>
       <property name="text">
        <string>Синий</string>
       </property>
      </item>
      <item>
       <property name="text">
        <string>Красный</string>
       </property>
      </item>
      <item>
       <property name="text">
        <string>Жёлтый</string>
       </property>
      </item>
      <item>
       <property name="text">
        <string>Чёрный</string>
       </property>
      </item>
      <item>
       <property name="text">
        <string>Фиолетовый</string>
       </property>
      </item>
      <item>
       <property name="text">
        <string>Зелёный</string>
       </property>
      </item>
      <item>
       <property name="text">
        <string>Оранжевый</string>
       </property>
      </item>
      <item>
       <property name="text">
        <string>Розовый</string>
       </property>
      </item>
     </widget>
     <widget class="QPushButton" name="addGoalButton">
      <property name="geometry">
       <rect>
        <x>60</x>
        <y>330</y>
        <width>211</width>
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
       <string>Создать</string>
      </property>
     </widget>
     <widget class="QPushButton" name="closeAddGoalWindowButton">
      <property name="geometry">
       <rect>
        <x>270</x>
        <y>10</y>
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
     <widget class="QLabel" name="addGoalResult">
      <property name="geometry">
       <rect>
        <x>0</x>
        <y>390</y>
        <width>321</width>
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
       <string notr="true">color:white;</string>
      </property>
      <property name="text">
       <string/>
      </property>
     </widget>
    </widget>
    <widget class="QLabel" name="goalNumber_1">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>100</y>
       <width>41</width>
       <height>41</height>
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
      <string notr="true">color:white;</string>
     </property>
     <property name="text">
      <string>1</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QLabel" name="goalNumber_2">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>210</y>
       <width>41</width>
       <height>41</height>
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
      <string notr="true">color:white;</string>
     </property>
     <property name="text">
      <string>2</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QLabel" name="goalNumber_3">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>320</y>
       <width>41</width>
       <height>41</height>
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
      <string notr="true">color:white;</string>
     </property>
     <property name="text">
      <string>3</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QLabel" name="goalNumber_4">
     <property name="geometry">
      <rect>
       <x>20</x>
       <y>430</y>
       <width>41</width>
       <height>41</height>
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
      <string notr="true">color:white;</string>
     </property>
     <property name="text">
      <string>4</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QLabel" name="goalNumber_5">
     <property name="geometry">
      <rect>
       <x>900</x>
       <y>100</y>
       <width>41</width>
       <height>41</height>
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
      <string notr="true">color:white;</string>
     </property>
     <property name="text">
      <string>5</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QLabel" name="goalNumber_6">
     <property name="geometry">
      <rect>
       <x>900</x>
       <y>210</y>
       <width>41</width>
       <height>41</height>
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
      <string notr="true">color:white;</string>
     </property>
     <property name="text">
      <string>6</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QLabel" name="goalNumber_7">
     <property name="geometry">
      <rect>
       <x>900</x>
       <y>320</y>
       <width>41</width>
       <height>41</height>
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
      <string notr="true">color:white;</string>
     </property>
     <property name="text">
      <string>7</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QLabel" name="goalNumber_8">
     <property name="geometry">
      <rect>
       <x>900</x>
       <y>430</y>
       <width>41</width>
       <height>41</height>
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
      <string notr="true">color:white;</string>
     </property>
     <property name="text">
      <string>8</string>
     </property>
     <property name="alignment">
      <set>Qt::AlignCenter</set>
     </property>
    </widget>
    <widget class="QPushButton" name="addProgress">
     <property name="geometry">
      <rect>
       <x>410</x>
       <y>340</y>
       <width>141</width>
       <height>41</height>
      </rect>
     </property>
     <property name="font">
      <font>
       <family>Arial Black</family>
       <pointsize>10</pointsize>
       <weight>75</weight>
       <bold>true</bold>
      </font>
     </property>
     <property name="styleSheet">
      <string notr="true">QPushButton{
border-radius: 10px;
background-color:qlineargradient(spread:reflect, x1:0, y1:0.011, x2:1, y2:0, stop:0 rgba(189, 36, 126, 243), stop:1 rgba(255, 255, 255, 255));
color: white;
border: 2px solid rgba(255, 33, 100, 230);
}

QPushButton:hover {
background-color: qlineargradient(spread:reflect, x1:0, y1:0.011, x2:1, y2:0, stop:0 rgba(189, 36, 126, 200), stop:1 rgba(255, 255, 255, 200));
}

</string>
     </property>
     <property name="text">
      <string>Добавить
прогреcc  цели</string>
     </property>
    </widget>
    <zorder>goalPlannerPlace</zorder>
    <zorder>goalPlannerLabel</zorder>
    <zorder>goalProgress1</zorder>
    <zorder>goalProgressLabel1</zorder>
    <zorder>goalProgressLabel2</zorder>
    <zorder>goalProgress2</zorder>
    <zorder>goalProgressLabel3</zorder>
    <zorder>goalProgress3</zorder>
    <zorder>goalProgressLabel4</zorder>
    <zorder>goalProgress4</zorder>
    <zorder>goalProgressLabel5</zorder>
    <zorder>goalProgress5</zorder>
    <zorder>goalProgressLabel6</zorder>
    <zorder>goalProgress6</zorder>
    <zorder>goalProgressLabel7</zorder>
    <zorder>goalProgress7</zorder>
    <zorder>goalProgressLabel8</zorder>
    <zorder>goalProgress8</zorder>
    <zorder>updateGoals</zorder>
    <zorder>createGoal</zorder>
    <zorder>editGoal</zorder>
    <zorder>goalNumber_1</zorder>
    <zorder>goalNumber_2</zorder>
    <zorder>goalNumber_3</zorder>
    <zorder>goalNumber_4</zorder>
    <zorder>goalNumber_5</zorder>
    <zorder>goalNumber_6</zorder>
    <zorder>goalNumber_7</zorder>
    <zorder>goalNumber_8</zorder>
    <zorder>addProgress</zorder>
    <zorder>addGoal</zorder>
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
   <zorder>revenueManagerMenu</zorder>
   <zorder>expenseManagerMenu</zorder>
   <zorder>goalPlannerMenu</zorder>
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
        con = sqlite3.connect('Databases/RecordedLoginAndPassword')
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
            con = sqlite3.connect('Databases/LoginsAndPasswords')
            cur = con.cursor()
            LoginAndPassword = cur.execute(f"""SELECT * FROM logpass WHERE
             login = '{self.enterLogin.text()}'""").fetchall()
            if LoginAndPassword != [] and LoginAndPassword[0][1] == self.enterPassword.text():
                con1 = sqlite3.connect('Databases/RecordedLoginAndPassword')
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
            con = sqlite3.connect('Databases/LoginsAndPasswords')
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
                date = datetime.now().date()
                con1 = sqlite3.connect('Databases/UsersInformat')
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
        with open('OtherFiles/LoadCheckbox.txt', mode='r', encoding='UTF-8') as file:
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
            with open('OtherFiles/LoadCheckbox.txt', mode='w', encoding='UTF-8') as file:
                file.write('True')
        con = sqlite3.connect('Databases/UsersInformat')
        cur = con.cursor()
        count = cur.execute(f"SELECT numberofauthorizations FROM inf WHERE username = '{self.login}'").fetchall()[0][0]
        count = int(count) + 1
        cur.execute(f"UPDATE inf SET numberofauthorizations = {count} WHERE username = '{self.login}'")
        con.commit()
        con.close()
        self.hide()
        self.app2 = MainWindow(self.login)
        self.app2.show()

class MainWindow(QMainWindow):
    def __init__(self, login):
        self.loginText = login
        super().__init__()
        f = io.StringIO(MainWindowTemplate)
        uic.loadUi(f, self)
        self.BackgroundUpdate(NAME)
        self.WindowTransparency()
        self.UpdateInformation()
        self.hideMenu()
        self.sortRevenueParameter.addItem('Источник')
        self.MainMenu.show()
        self.addRevenueErrorLabel.setText('')
        self.mainMenu.clicked.connect(self.OpenMainMenu)
        self.revenueManager.clicked.connect(self.OpenRevenueManager)
        self.expenseManager.clicked.connect(self.OpenExpenseManager)
        self.goalPlanner.clicked.connect(self.OpenGoalPlannerMenu)
        self.settings.clicked.connect(self.OpenSettings)
        self.createGoal.clicked.connect(self.OpenAddGoal)
        self.addRevenue.clicked.connect(self.createRevenue)
        self.addExpense.clicked.connect(self.createExpense)
        self.updateRevenueButton.clicked.connect(self.UpdateRevenueTransactions)
        self.updateExpenseButton.clicked.connect(self.UpdateExpenseTransactions)
        self.closeAddGoalWindowButton.clicked.connect(self.closeAddGoalWindow)
        self.addGoalButton.clicked.connect(self.addGoalFunction)
        self.colors = {'Синий': 'blue', 'Красный': 'red', 'Жёлтый': 'yellow', 'Чёрный': 'black', 'Фиолетовый': 'violet',
                       'Зелёный': 'green', 'Оранжевый': 'orange', 'Розовый': 'pink', 'Голубой': 'yellow'}

    def hideMenu(self):
        self.expenseManagerMenu.hide()
        self.revenueManagerMenu.hide()
        self.goalPlannerMenu.hide()
        self.MainMenu.hide()

    def BackgroundUpdate(self, fileName):
        self.background.setStyleSheet("""border-image: url(:/pictures/images.jpg);
                border-radius: 35px""")
        self.avatarFrame.setStyleSheet("""border-image: url(:/pictures/Рамка для аватарки.png)""")

    def WindowTransparency(self):
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def UpdateInformation(self):
        self.login.setText(self.loginText)
        con1 = sqlite3.connect('Databases/UsersInformat')
        cur1 = con1.cursor()
        data = cur1.execute(f"SELECT balance, registrationdate, numberoftransactions FROM inf WHERE username "
                            f"= '{self.loginText}'").fetchall()
        self.balance.setText(f'Ваш баланс: {data[0][0]}')
        date = datetime.now().date()
        date1 = data[0][1]
        date1 = '/'.join(date1.split('-')[::-1])
        date2 = datetime.strptime(f'{date1}', '%d/%m/%Y')
        self.userInformation.setText(f'Информация:\n\nДата регистрации:\n\n{data[0][1]}\n\nВ приложении:'
                                     f'\n\n{(date - date2.date()).days} дней\n\nКоличество транзакций:\n\n{data[0][2]}')
        con1.close()
        self.recentTransactions.clear()
        self.recentTransactions.setRowCount(0)
        wb = load_workbook('ДенежныеТранзакции.xlsx')
        sheetnames = wb.sheetnames
        self.recentTransactions.setColumnCount(5)
        self.recentTransactions.setHorizontalHeaderLabels(['Доходы\nРасходы','Сумма', 'Источник', 'Категория', 'Дата'])
        if self.loginText in sheetnames:
            ws = wb[self.loginText]
            indexation = 1
            data = []
            while ws[f'E{indexation}'].value is not None:
                data.append([ws[f'E{indexation}'].value, ws[f'A{indexation}'].value, ws[f'B{indexation}'].value,
                             ws[f'C{indexation}'].value, ws[f'D{indexation}'].value])
                indexation += 1
            for i, row in enumerate(data[::-1][0:10]):
                self.recentTransactions.setRowCount(self.recentTransactions.rowCount() + 1)
                self.recentTransactions.setItem(i, 0, QTableWidgetItem(str(row[0])))
                self.recentTransactions.setItem(i, 2, QTableWidgetItem(str(row[2])))
                self.recentTransactions.setItem(i, 1, QTableWidgetItem(str(row[1])))
                self.recentTransactions.setItem(i, 3, QTableWidgetItem(str(row[3])))
                self.recentTransactions.setItem(i, 4, QTableWidgetItem(str(row[4])))
            wb.close()

    def OpenMainMenu(self):
        self.hideMenu()
        self.UpdateInformation()
        self.MainMenu.show()
    def OpenRevenueManager(self):
        self.hideMenu()
        self.UpdateRevenueTransactions()
        self.revenueManagerMenu.show()

    def OpenAddGoal(self):
        self.hideMenu()
        self.OpenGoalPlannerMenu()
        self.addGoal.show()

    def OpenGoalPlannerMenu(self):
        self.hideMenu()
        self.addGoal.hide()
        self.goalPlannerMenu.show()

    def createRevenue(self):
        try:
            a = int(self.revenueSummaEnter.text())
            if a < 0:
                self.addRevenueErrorLabel.setText('Ошибка: Укажите сумму без минуса')
            else:
                if (self.revenueSummaEnter.text() == '' or self.revenueSourceEnter.text() == ''
                        or self.revenueCategoryEnter.text() == ''):
                    self.addRevenueErrorLabel.setText('Ошибка: Заполните все поля')
                else:
                    wb = load_workbook('ДенежныеТранзакции.xlsx')
                    sheetnames = wb.sheetnames
                    if self.loginText in sheetnames:
                        ws = wb[self.loginText]
                    else:
                        ws = wb.create_sheet(self.loginText)
                    ws.append([self.revenueSummaEnter.text(), self.revenueSourceEnter.text(), self.revenueCategoryEnter.text(),
                               datetime.now(), 'Д'])
                    wb.save('ДенежныеТранзакции.xlsx')
                    wb.close()
                    con = sqlite3.connect('Databases/UsersInformat')
                    cur = con.cursor()
                    balance = cur.execute(f"SELECT balance FROM inf WHERE username = '{self.loginText}'").fetchall()[0][0]
                    count = cur.execute(f"SELECT numberoftransactions FROM inf WHERE username"
                                        f" = '{self.loginText}'").fetchall()[0][0]
                    count = int(count) + 1
                    balance = int(balance) + int(self.revenueSummaEnter.text())
                    cur.execute(f"UPDATE inf SET numberoftransactions = {count} WHERE username = '{self.loginText}'")
                    cur.execute(f"UPDATE inf SET balance = {balance} WHERE username = '{self.loginText}'")
                    con.commit()
                    con.close()
                    self.revenueSummaEnter.setText('')
                    self.revenueSourceEnter.setText('')
                    self.revenueCategoryEnter.setText('')
                    self.addRevenueErrorLabel.setText('')
        except Exception:
            self.addRevenueErrorLabel.setText('Ошибка: Сумма должна \nсостоять из цифр')


    def UpdateRevenueTransactions(self):
        self.revenueTransactions.clear()
        self.revenueTransactions.setRowCount(0)
        wb = load_workbook('ДенежныеТранзакции.xlsx')
        sheetnames = wb.sheetnames
        if self.loginText in sheetnames:
            ws = wb[self.loginText]
            indexation = 1
            data = []
            while ws[f'E{indexation}'].value is not None:
                if ws[f'E{indexation}'].value == 'Д':
                    data.append([ws[f'A{indexation}'].value, ws[f'B{indexation}'].value, ws[f'C{indexation}'].value,
                                ws[f'D{indexation}'].value])
                indexation += 1
            self.revenueTransactions.setColumnCount(4)
            self.revenueTransactions.setHorizontalHeaderLabels(['Сумма', 'Источник', 'Категория', 'Дата'])
            if self.sortRevenueParameter.currentText() == 'Дата':
                data = data[::-1]
            elif self.sortRevenueParameter.currentText() == 'Категория':
                data = sorted(data, key=lambda x: (x[2], int(x[0])))[::-1]
            elif self.sortRevenueParameter.currentText() == 'От максимального':
                data = sorted(data, key=lambda x: int(x[0]))[::-1]
            elif self.sortRevenueParameter.currentText() == 'От минимального':
                data = sorted(data, key=lambda x: int(x[0]))
            elif self.sortRevenueParameter.currentText() == 'Источник':
                data = sorted(data, key=lambda x: (x[1], int(x[0])))[::-1]
            for i, row in enumerate(data):
                self.revenueTransactions.setRowCount(self.revenueTransactions.rowCount() + 1)
                self.revenueTransactions.setItem(i, 0, QTableWidgetItem(str(row[0])))
                self.revenueTransactions.setItem(i, 2, QTableWidgetItem(str(row[2])))
                self.revenueTransactions.setItem(i, 1, QTableWidgetItem(str(row[1])))
                self.revenueTransactions.setItem(i, 3, QTableWidgetItem(str(row[3])))
            wb.close()

    def UpdateExpenseTransactions(self):
        self.expenseTransactions.clear()
        self.expenseTransactions.setRowCount(0)
        wb = load_workbook('ДенежныеТранзакции.xlsx')
        sheetnames = wb.sheetnames
        if self.loginText in sheetnames:
            ws = wb[self.loginText]
            indexation = 1
            data = []
            while ws[f'E{indexation}'].value is not None:
                if ws[f'E{indexation}'].value == 'Р':
                    data.append([ws[f'A{indexation}'].value, ws[f'B{indexation}'].value, ws[f'C{indexation}'].value,
                                ws[f'D{indexation}'].value])
                indexation += 1
            self.expenseTransactions.setColumnCount(4)
            self.expenseTransactions.setHorizontalHeaderLabels(['Сумма', 'Источник', 'Категория', 'Дата'])
            if self.sortExpenseParameter.currentText() == 'Дата':
                data = data[::-1]
            elif self.sortExpenseParameter.currentText() == 'Категория':
                data = sorted(data, key=lambda x: (x[2], int(x[0])))[::-1]
            elif self.sortExpenseParameter.currentText() == 'От максимальной суммы':
                data = sorted(data, key=lambda x: int(x[0]))[::-1]
            elif self.sortExpenseParameter.currentText() == 'От минимальной суммы':
                data = sorted(data, key=lambda x: int(x[0]))
            elif self.sortExpenseParameter.currentText() == 'Источник':
                data = sorted(data, key=lambda x: (x[1], int(x[0])))[::-1]
            for i, row in enumerate(data):
                self.expenseTransactions.setRowCount(self.expenseTransactions.rowCount() + 1)
                self.expenseTransactions.setItem(i, 0, QTableWidgetItem(str(row[0])))
                self.expenseTransactions.setItem(i, 2, QTableWidgetItem(str(row[2])))
                self.expenseTransactions.setItem(i, 1, QTableWidgetItem(str(row[1])))
                self.expenseTransactions.setItem(i, 3, QTableWidgetItem(str(row[3])))

            wb.close()

    def createExpense(self):
        try:
            a = int(self.expenseSummaEnter.text())
            if a < 0:
                self.addExpenseErrorLabel.setText('Ошибка: Укажите сумму без минуса')
            else:
                if (self.expenseSummaEnter.text() == '' or self.expenseSourceEnter.text() == ''
                        or self.expenseCategoryEnter.text() == ''):
                    self.addExpenseErrorLabel.setText('Ошибка: Заполните все поля')
                else:
                    wb = load_workbook('ДенежныеТранзакции.xlsx')
                    sheetnames = wb.sheetnames
                    if self.loginText in sheetnames:
                        ws = wb[self.loginText]
                    else:
                        ws = wb.create_sheet(self.loginText)
                    ws.append(
                        [self.expenseSummaEnter.text(), self.expenseSourceEnter.text(), self.expenseCategoryEnter.text(),
                         datetime.now(), 'Р'])
                    wb.save('ДенежныеТранзакции.xlsx')
                    wb.close()
                    con = sqlite3.connect('Databases/UsersInformat')
                    cur = con.cursor()
                    balance = cur.execute(f"SELECT balance FROM inf WHERE username = '{self.loginText}'").fetchall()[0][0]
                    count = cur.execute(f"SELECT numberoftransactions FROM inf WHERE username"
                                        f" = '{self.loginText}'").fetchall()[0][0]
                    count = int(count) + 1
                    balance = int(balance) - int(self.expenseSummaEnter.text())
                    cur.execute(f"UPDATE inf SET numberoftransactions = {count} WHERE username = '{self.loginText}'")
                    cur.execute(f"UPDATE inf SET balance = {balance} WHERE username = '{self.loginText}'")
                    con.commit()
                    con.close()
                    self.expenseSummaEnter.setText('')
                    self.expenseSourceEnter.setText('')
                    self.expenseCategoryEnter.setText('')
                    self.addExpenseErrorLabel.setText('')
        except Exception:
            self.addExpenseErrorLabel.setText('Ошибка: Сумма должна \nсостоять из цифр')

    def addGoalFunction(self):
        try:
            if self.enterGoalTarget.text() == '' or self.enterGoalName.text() == '':
                self.addGoalResult.setText('Ошибка: Заполните все поля')
            else:
                a = int(self.enterGoalTarget.text())
                if a < 0:
                    self.addExpenseErrorLabel.setText('Ошибка: Укажите цель без минуса')
                else:
                    con = sqlite3.connect('Goals')
                    cur = con.cursor()
                    print(1)
                    data = cur.execute("SELECT * FROM goalsCondition").fetchall()
                    print(1)
                    print(data)
                    con.commit()
                    con.close()
        except Exception:
            self.addGoalResult.setText('Ошибка: Цель должна \nсостоять из цифр')
    def OpenExpenseManager(self):
        self.hideMenu()
        self.UpdateExpenseTransactions()
        self.expenseManagerMenu.show()
    def OpenSettings(self):
        self.app4 = SettingsWindow()
        self.app4.show()

    def closeAddGoalWindow(self):
        self.addGoal.hide()

class SettingsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(settingsTemplate)
        uic.loadUi(f, self)
        self.BackgroundUpdate(NAME)
        self.WindowTransparency()
        self.disableAutomaticLoginButton.clicked.connect(self.DisableAutomaticLoginFunction)
        self.exitButton.clicked.connect(self.ExitProgram)
        self.closeSettingsButton.clicked.connect(self.closeSettings)

    def BackgroundUpdate(self, fileName):
        self.background.setStyleSheet("""border-image: url(:/pictures/Картинка для настроек.jpg);
                border-radius: 35px""")

    def WindowTransparency(self):
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def DisableAutomaticLoginFunction(self):
        with open('OtherFiles/LoadCheckbox.txt', mode='r', encoding='UTF-8') as file:
            condition = file.readline()
        if condition == 'True':
            with open('OtherFiles/LoadCheckbox.txt', mode='w', encoding='UTF-8') as file:
                file.write('False')
        else:
            self.app5 = ErrorDisableAutomaticLoginWindow()
            self.app5.show()

    def ExitProgram(self):
        sys.exit(app.exec_())

    def closeSettings(self):
        self.hide()

class ErrorDisableAutomaticLoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(errorDisableAutomaticLoginTemplate)
        uic.loadUi(f, self)
        self.BackgroundUpdate(NAME)
        self.WindowTransparency()
        self.exitFromError.clicked.connect(self.closeError)

    def BackgroundUpdate(self, fileName):
        self.background.setStyleSheet("""border-image: url(:/pictures/ErrorBackground.jpg);
                border-radius: 35px""")

    def WindowTransparency(self):
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)

    def closeError(self):
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RegistrationWindow()
    ex.show()
    sys.exit(app.exec_())