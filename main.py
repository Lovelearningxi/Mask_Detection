#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/31 15:43
# @Author  : WangXi
# @Site    : 
# @File    : main.py
# @Software: PyCharm
import csv
import sys
import time

import cv2
import numpy
import PyQt5.sip
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from detection import Mask_detect
from form import Ui_Form


class MyDesiger(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyDesiger, self).__init__(parent)
        self.setupUi(self)
        self.star_show()
        self.info = [["姓名", "学号", "学院", "口罩佩戴情况", "日期"]]
        self.VideoTimer = Video()
        self.VideoTimer.changePixmap.connect(self.setImage)
        self.VideoTimer.detectPixmap.connect(self.setDetect)
        self.VideoTimer.run_over.connect(self.finish_detect)
        self.VideoTimer.update_data.connect(self.add_data)

    def shoot_play(self):  # 摄像头展示
        if self.name.text() == '' or self.ID.text() == '' or self.college.text() == '':
            QMessageBox.information(self, '信息不完整', '请正确填写完整信息', QMessageBox.Yes)
        else:
            self.VideoTimer.working = True  # 使摄像和检测线程能工作
            self.VideoTimer.start()

    def frame_detect(self):  # 检测每一帧
        if self.VideoTimer.working:
            self.VideoTimer.setDetect()

    def detect_quit(self):  # 结束检测
        self.close()

    def getinfo(self):  # 导出文件
        with open('resourse/info.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in self.info:
                writer.writerow(row)
        QMessageBox.information(self, '导出成功', '文件保存路径为:resourse/info.csv', QMessageBox.Yes)

    def star_show(self):  # 初始化显示界面
        frame = QPixmap('resourse/sample.jpg').scaled(self.labelplay.width(), self.labelplay.height())
        self.labelplay.setPixmap(frame)
        image = QPixmap('resourse/sample_detection.jpg').scaled(self.labeldete.width(), self.labeldete.height())
        self.labeldete.setPixmap(image)
        paddlehub = QPixmap('resourse/showimg.png').scaled(self.labelpaddle.width(), self.labelpaddle.height())
        self.labelpaddle.setPixmap(paddlehub)

    def finish_detect(self, kz):  # 检测完毕
        self.star_show()
        QMessageBox.information(self, '检测结果:', kz + '!!', QMessageBox.Yes)
        self.name.clear()
        self.ID.clear()
        self.college.clear()

    def add_data(self, kz):  # 记录表信息更新
        self.model.appendRow([
            QStandardItem(self.name.text()),
            QStandardItem(self.ID.text()),
            QStandardItem(self.college.text()),
            QStandardItem(kz),
            QStandardItem(time.strftime('%Y.%m.%d', time.localtime(time.time()))),
        ])
        self.info.append([self.name.text(), self.ID.text(), self.college.text(), kz,
                          time.strftime('%Y.%m.%d', time.localtime(time.time()))])

    def setImage(self, frame):
        self.labelplay.setPixmap(
            QPixmap.fromImage(QImage(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), 640 / 2, 480 / 2, 13)))

    def setDetect(self, image):
        self.labeldete.setPixmap(
            QPixmap.fromImage(QImage(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), 640 / 2, 480 / 2, 13)))


class Video(QThread):
    changePixmap = pyqtSignal(numpy.ndarray)
    detectPixmap = pyqtSignal(numpy.ndarray)
    update_data = pyqtSignal(str)
    run_over = pyqtSignal(str)

    def __init__(self):
        QThread.__init__(self)
        self.detect = False  # 是否能检测
        self.working = False  # 是否能工作
        self.count = 0  # 检测到人脸的次数

    def run(self):
        #source = "http://admin:admin@192.168.2.137:8081/video"
        cap = cv2.VideoCapture(0)
        while self.working:
            ret, frame = cap.read()
            frame = cv2.resize(frame, (320, 240))
            self.changePixmap.emit(frame)
            if self.detect:
                img = frame.copy()
                detected_image, num, kz = Mask_detect(img)  # 口罩检测
                self.detectPixmap.emit(detected_image)
                if num > 0:
                    self.count += 1
            if self.count >= 6:  # 超过6帧检测到人脸就停止检测
                self.detect = False
                self.working = False
                self.count = 0  # 计数清零
                self.run_over.emit(kz)
                self.update_data.emit(kz)
        cap.release()

    def setDetect(self):
        self.detect = True

    def setquit(self):
        self.detect = False
        self.working = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MyDesiger()
    ui.show()
    sys.exit(app.exec_())
