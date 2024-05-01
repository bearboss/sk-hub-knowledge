import sys
import psutil
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPainter, QFont, QColor, QPen, QBrush
from PyQt5.QtChart import QChart, QChartView, QLineSeries, QDateTimeAxis, QValueAxis
from PyQt5.QtCore import Qt, QTimer, QMargins, QDateTime
import psutil
import time


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Flow Monitor')
        self.resize(800, 600)
        self.last_time = QDateTime.currentDateTime()
        self.last_upload_bytes = 1
        self.download_bytes = 0
        self.last_download_bytes = 0
        self.upload_bytes = 0

        # 初始化折线图
        self.chart = QChart()
        self.chart.setTitle('Network Traffic')
        self.chart.legend().hide()

        self.series = QLineSeries()
        self.chart.addSeries(self.series)

        self.axisX = QDateTimeAxis()
        self.axisX.setTickCount(10)
        self.axisX.setFormat('hh:mm:ss')
        self.axisX.setTitleText('Time')
        self.chart.addAxis(self.axisX, Qt.AlignmentFlag.AlignBottom)
        self.series.attachAxis(self.axisX)

        self.axisY = QValueAxis()
        self.axisY.setLabelFormat('%i KB/s')
        self.axisY.setTitleText('Speed')
        self.chart.addAxis(self.axisY, Qt.AlignmentFlag.AlignLeft)
        self.series.attachAxis(self.axisY)


        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        self.initUI()

         # 创建定时器
        timer = QTimer(self)
        timer.timeout.connect(self.update_data)
        timer.start(1000) # 每秒钟更新一次数据

    def initUI(self):
         # 创建一个主窗口中心部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # 创建一个垂直布局，用于放置界面元素
        vlayout = QVBoxLayout()

        # 创建一个水平布局，用于放置工具导航栏和折线图
        hlayout1 = QHBoxLayout()

        # 创建工具导航栏并添加到水平布局中
        button1 = QPushButton('按钮1')
        button2 = QPushButton('按钮2')
        button3 = QPushButton('按钮3')
        button1.setFixedSize(100, 30)
        button2.setFixedSize(100, 30)
        button3.setFixedSize(100, 30)
        hlayout1.addWidget(button1)
        hlayout1.addWidget(button2)
        hlayout1.addWidget(button3)
        hlayout1.setAlignment(Qt.AlignmentFlag.AlignLeft)
        # 将水平布局1添加到垂直布局中
        vlayout.addLayout(hlayout1)

        # 创建一个水平布局，用于放置折线图和流量数据
        hlayout2 = QHBoxLayout()

        # 创建折线图并添加到水平布局中
        self.chart = QChart()
        self.chart.setBackgroundBrush(QBrush(QColor(255, 255, 255, 0)))
        self.chart.setMargins(QMargins(0, 0, 0, 0))
        self.chart.setContentsMargins(-5, -5, -5, -5)
        self.chart.legend().hide()
        series = QLineSeries()
        series.setPen(QPen(QColor(0, 255, 0), 2))
        self.chart.addSeries(series)
        self.chart.createDefaultAxes()
        self.chart.axisX().setRange(0, 60)
        self.chart.axisY().setRange(0, 100)
        chart_view = QChartView(self.chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        chart_view.setContentsMargins(0, 0, 0, 0)
        chart_view.setStyleSheet('border: none;')
        hlayout2.addWidget(chart_view)

        # 创建一个水平布局，用于放置流量数据
        hlayout3 = QHBoxLayout()

        # 创建三个标签用于显示统计数值，并添加到水平布局3中
        self.upload_label = QLabel('Upload: 0 kbps')
        self.upload_label.setStyleSheet('color: #00FF00; font-size: 20px;')
        self.download_label = QLabel('Download: 0 kbps')
        self.download_label.setStyleSheet('color: #00FF00; font-size: 20px;')
        self.total_label = QLabel('Total: 0 MB')
        self.total_label.setStyleSheet('color: #00FF00; font-size: 20px;')
        hlayout3.addWidget(self.upload_label)
        hlayout3.addWidget(self.download_label)
        hlayout3.addWidget(self.total_label)

        # 将水平布局2和水平布局3添加到垂直布局中
        vlayout.addLayout(hlayout2)
        vlayout.addLayout(hlayout3)

        # 将垂直布局添加到主窗口中心部件中
        central_widget.setLayout(vlayout)
        self.update_data()

    def update_data(self):
        # 获取当前时间和上一次更新时间
        current_time = QDateTime.currentDateTime()
        elapsed_time = self.last_time.secsTo(current_time)
        if elapsed_time == 0:
            elapsed_time = 1

        # 获取网络接口数据
        sent_before = psutil.net_io_counters().bytes_sent  # 已发送的流量
        recv_before = psutil.net_io_counters().bytes_recv  # 已接收的流量
        time.sleep(1)
        sent_now = psutil.net_io_counters().bytes_sent
        recv_now = psutil.net_io_counters().bytes_recv
        sent = (sent_now - sent_before)/1024  # 算出1秒后的差值
        recv = (recv_now - recv_before)/1024


        print('upload', f"{sent:.2f}")
        print('download', f"{recv:.2f}")

        # 计算上传和下载速度和总流量
        # upload_speed = (sent - self.last_upload_bytes) / elapsed_time / 8
        # download_speed = (recv - self.last_download_bytes) / elapsed_time / 8
        # total_data = (sent + recv) / 1024

        # 更新标签显示
        self.upload_label.setText(f"Upload: {sent:.2f} kbps")
        print('download_bytes ===============', recv)
        if recv < 100:
            self.chart.axisY().setRange(0, 100)
            self.chart.axisY().setTitleText("Download Speed (kbps)")
            self.chart.axisY().setLabelFormat("%0.0f")
            self.download_label.setText(f"Download: {recv:.2f} kbps")
            max_download_data = 1000
            unit = 'kbps'
        elif recv < 1000:
            self.chart.axisY().setRange(0, 1000)
            self.chart.axisY().setTitleText("Download Speed (kbps)")
            self.chart.axisY().setLabelFormat("%0.0f")
            self.download_label.setText(f"Download: {recv:.2f} kbps")
            max_download_data = 1000
            unit = 'kbps'
        elif recv < 10*1024:
            print('current show mb ')
            self.chart.axisY().setRange(0, 10)
            self.chart.axisY().setTitleText("Download Speed (Mbps)")
            self.chart.axisY().setLabelFormat("%0.0f")
            # 下载大小在1GB~1000GB之间，以mbps为单位，最多显示1000mb
            self.download_label.setText(f"Download: {recv/1024:.2f} mbps")
            max_download_data = 1000
            unit = 'mbps'
        elif recv < 100*1024*1024:
            print('current show mb ')
            self.chart.axisY().setRange(0, 100)
            self.chart.axisY().setTitleText("Download Speed (Mbps)")
            self.chart.axisY().setLabelFormat("%0.0f")
            # 下载大小在1GB~1000GB之间，以mbps为单位，最多显示1000mb
            self.download_label.setText(f"Download: {recv/1024:.2f} mbps")
            max_download_data = 1000
            unit = 'mbps'
        elif recv < 1000*1024*1024:
            self.chart.axisY().setRange(0, 1000)
            self.chart.axisY().setTitleText("Download Speed (Mbps)")
            self.chart.axisY().setLabelFormat("%0.0f")
            # 下载大小在1GB~1000GB之间，以mbps为单位，最多显示1000mb
            self.download_label.setText(f"Download: {recv/1024:.2f} mbps")
            max_download_data = 1000
            unit = 'mbps'
        else:
            self.chart.axisY().setRange(0, 100)
            self.chart.axisY().setTitleText("Download Speed (Gbps)")
            self.chart.axisY().setLabelFormat("%0.1f")
            # 下载大小在1000GB以上，以gbps为单位，最多显示100g
            self.download_label.setText(f"Download: {recv/1024/1024:.2f} gbps")
            max_download_data = 100
            unit = 'gbps'
        self.chart.axisY().setTitleText(f'Download Speed ({unit})')
        self.chart.axisY().setRange(0, max_download_data)

        # 更新折线图
        series = self.chart.series()[0]
        series.append(current_time.toMSecsSinceEpoch(), sent)
        if series.count() > 60:
            series.removePoints(0, 1)
        self.chart.axisX().setRange(current_time.addSecs(-60).toMSecsSinceEpoch(), current_time.toMSecsSinceEpoch())

        # 保存上一次更新时间和流量数据
        self.last_time = current_time
        self.last_upload_bytes = sent
        self.last_download_bytes = recv

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
