#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 13:49
# @Author  : WangXi
# @Site    : 
# @File    : form.py
# @Software: PyCharm

import time
from tkinter.tix import Form

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 800)
        self.label5 = QtWidgets.QLabel(Form)
        self.label5.setGeometry(QtCore.QRect(0, 240, 1000, 560))
        self.label5.setObjectName("label5")
        self.label5.setStyleSheet(
            '''QLabel{background:#76789E}''')

        '''tableView设计'''
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(180, 290, 820, 560))
        self.tableView.setObjectName("tableview")
        '''设置五个水平头部标签'''
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['姓名', '学号', '学院', '口罩佩戴情况', '日期'])
        self.tableView.setModel(self.model)
        '''设置水平方向剩下的窗口部分，填满表格'''
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        '''设计tableview的样式'''
        self.tableView.setStyleSheet(
            '''QTableView{
                        border:1px solid #74E9FF;
                        border-radius:10px;
                        padding:2px 4px;
                }''')

        self.tableView.horizontalHeader().setStyleSheet("QHeaderView::section{background:#87C9FF;}")
        '''表头权限设置不可被点击'''
        self.tableView.horizontalHeader().setSectionsClickable(False)
        self.tableView.verticalHeader().setSectionsClickable(False)
        self.tableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.model.appendRow([
            QtGui.QStandardItem('王玺'),
            QtGui.QStandardItem('18380320128'),
            QtGui.QStandardItem('数据科学与大数据'),
            QtGui.QStandardItem('未戴口罩'),
            QtGui.QStandardItem(time.strftime('%Y.%m.%d', time.localtime(time.time()))),
        ])

        '''LineEdit输入框设置'''
        self.name = QtWidgets.QLineEdit(Form)
        self.name.setGeometry(QtCore.QRect(40, 430, 100, 28))
        self.name.setObjectName("name")
        self.name.setPlaceholderText("输入姓名")

        self.ID = QtWidgets.QLineEdit(Form)
        self.ID.setGeometry(QtCore.QRect(40, 490, 100, 28))
        self.ID.setObjectName("ID")
        self.ID.setPlaceholderText("输入学号")

        self.college = QtWidgets.QLineEdit(Form)
        self.college.setGeometry(QtCore.QRect(40, 550, 100, 28))
        self.college.setObjectName("college")
        self.college.setPlaceholderText("输入学院")

        self.name.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')

        self.ID.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')

        self.college.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')

        '''QLabel设计'''
        self.labelplay = QtWidgets.QLabel(Form)
        self.labelplay.setGeometry(QtCore.QRect(0, 0, 320, 240))
        self.labelplay.setObjectName("labelplay")

        self.labeldete = QtWidgets.QLabel(Form)
        self.labeldete.setGeometry(QtCore.QRect(680, 0, 320, 240))
        self.labeldete.setObjectName("labeldete")

        self.labelname = QtWidgets.QLabel(Form)
        self.labelname.setGeometry(QtCore.QRect(5, 430, 30, 28))
        self.labelname.setObjectName("labelname")

        self.labelid = QtWidgets.QLabel(Form)
        self.labelid.setGeometry(QtCore.QRect(5, 490, 30, 28))
        self.labelid.setObjectName("labelid")

        self.labelxy = QtWidgets.QLabel(Form)
        self.labelxy.setGeometry(QtCore.QRect(5, 550, 30, 28))
        self.labelxy.setObjectName("labelxueyuan")

        self.labelinfo = QtWidgets.QLabel(Form)
        self.labelinfo.setGeometry(QtCore.QRect(180, 260, 300, 28))
        self.labelinfo.setObjectName("labelinfo")

        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPixelSize(16)

        self.labelpaddle = QtWidgets.QLabel(Form)
        self.labelpaddle.setGeometry(QtCore.QRect(320, 0, 360, 240))
        self.labelpaddle.setObjectName("labelpaddle")


        self.labell = QtWidgets.QLabel(Form)
        self.labell.setGeometry(QtCore.QRect(320, 0, 180, 30))
        self.labell.setObjectName("labell")

        self.labelr = QtWidgets.QLabel(Form)
        self.labelr.setGeometry(QtCore.QRect(500, 0, 180, 30))
        self.labelr.setObjectName("labelr")

        self.labell.setFont(font)
        self.labelr.setFont(font)
        self.labell.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)  # 文本显示位置
        self.labelr.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTop | QtCore.Qt.AlignTrailing)  # 文本显示位置

        self.labelplay.setStyleSheet(
            '''QLabel{
                    border:1px solid red;
            }''')

        self.labeldete.setStyleSheet(
            '''QLabel{
                    border:1px solid red;
            }''')

        self.labelpaddle.setStyleSheet(
            '''QLabel{
                    border:1px solid #E8B735;
            }''')

        self.labell.setStyleSheet("color:white")
        self.labelr.setStyleSheet("color:white")

        '''Button设计'''
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(12)

        self.play = QtWidgets.QPushButton(Form)
        self.play.setGeometry(QtCore.QRect(10, 260, 100, 28))
        self.play.setObjectName("play")

        self.dete = QtWidgets.QPushButton(Form)
        self.dete.setGeometry(QtCore.QRect(10, 310, 100, 28))
        self.dete.setObjectName("dete")

        self.quit = QtWidgets.QPushButton(Form)
        self.quit.setGeometry(QtCore.QRect(10, 360, 100, 28))
        self.quit.setObjectName("quit")

        self.export = QtWidgets.QPushButton(Form)
        self.export.setGeometry(QtCore.QRect(5, 650, 150, 28))
        self.export.setObjectName("export")

        self.play.setFont(font)
        self.dete.setFont(font)
        self.quit.setFont(font)
        # self.export.setFont(font)

        self.play.setStyleSheet(
            '''QPushButton{background:#87C9FF;border-radius:5px;}QPushButton:hover{background:blue;}''')
        self.dete.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.quit.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
        self.export.setStyleSheet(
            '''QPushButton{background:#F4605F;border-radius:5px;}QPushButton:hover{background:red;}''')

        self.retranslateUi(Form)
        self.play.clicked.connect(Form.shoot_play)
        self.dete.clicked.connect(Form.frame_detect)
        self.quit.clicked.connect(Form.detect_quit)
        self.export.clicked.connect(Form.getinfo)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "学生口罩监测登记系统"))
        self.labelplay.setText(_translate("Form", "TextLabel"))
        self.labeldete.setText(_translate("Form", "TextLabel"))
        self.labell.setText(_translate("Form", "摄像区"))
        self.labelr.setText(_translate("Form", "检测区"))
        self.labelname.setText(_translate("Form", "姓名"))
        self.labelid.setText(_translate("Form", "学号"))
        self.labelxy.setText(_translate("Form", "学院"))
        self.labelinfo.setText(_translate("Form", "学生口罩佩戴情况记录:"))
        self.labelpaddle.setText(_translate("Form", "paddle"))
        self.play.setText(_translate("Form", "开启摄像"))
        self.dete.setText(_translate("Form", "检测口罩"))
        self.quit.setText(_translate("Form", "结束检测"))
        self.export.setText(_translate("Form", "导出检测信息表"))


if __name__ == "__main__":
    ui = Ui_Form()
    ui.show()
