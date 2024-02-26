# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'principal.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFormLayout, QFrame,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QProgressBar,
    QPushButton, QSizePolicy, QSlider, QSpinBox,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)
import UI.resources.Thermography_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(975, 754)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionOpen.setCheckable(True)
        icon = QIcon()
        iconThemeName = u"system-file-manager"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.actionOpen.setIcon(icon)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon1 = QIcon()
        iconThemeName = u"document-save"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.actionSave.setIcon(icon1)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon2 = QIcon()
        iconThemeName = u"application-exit"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.actionExit.setIcon(icon2)
        self.actionExecute = QAction(MainWindow)
        self.actionExecute.setObjectName(u"actionExecute")
        self.actionImage_Generation = QAction(MainWindow)
        self.actionImage_Generation.setObjectName(u"actionImage_Generation")
        self.actionLockIn = QAction(MainWindow)
        self.actionLockIn.setObjectName(u"actionLockIn")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.Cabecera = QFrame(self.centralwidget)
        self.Cabecera.setObjectName(u"Cabecera")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Cabecera.sizePolicy().hasHeightForWidth())
        self.Cabecera.setSizePolicy(sizePolicy1)
        self.Cabecera.setMinimumSize(QSize(0, 150))
        self.Cabecera.setMaximumSize(QSize(16777215, 150))
        self.Cabecera.setBaseSize(QSize(0, 150))
        self.Cabecera.setFrameShape(QFrame.Box)
        self.Cabecera.setFrameShadow(QFrame.Raised)
        self.Cabecera.setLineWidth(2)
        self.horizontalLayout = QHBoxLayout(self.Cabecera)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.LogoCicata = QLabel(self.Cabecera)
        self.LogoCicata.setObjectName(u"LogoCicata")
        self.LogoCicata.setMinimumSize(QSize(120, 120))
        self.LogoCicata.setMaximumSize(QSize(120, 150))
        self.LogoCicata.setFrameShape(QFrame.Box)
        self.LogoCicata.setFrameShadow(QFrame.Raised)
        self.LogoCicata.setLineWidth(2)
        self.LogoCicata.setPixmap(QPixmap(u":/Header/IPN_CICATA.png"))
        self.LogoCicata.setScaledContents(True)

        self.horizontalLayout.addWidget(self.LogoCicata)

        self.label = QLabel(self.Cabecera)
        self.label.setObjectName(u"label")
        self.label.setFrameShape(QFrame.Box)
        self.label.setFrameShadow(QFrame.Raised)
        self.label.setLineWidth(2)
        self.label.setTextFormat(Qt.RichText)

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.Cabecera)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMinimumSize(QSize(120, 120))
        self.label_2.setMaximumSize(QSize(120, 150))
        self.label_2.setBaseSize(QSize(120, 120))
        self.label_2.setFrameShape(QFrame.Box)
        self.label_2.setFrameShadow(QFrame.Raised)
        self.label_2.setLineWidth(2)
        self.label_2.setPixmap(QPixmap(u":/Header/LOGO POLI PANTONE 222 C.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 80)
        self.horizontalLayout.setStretch(2, 5)

        self.verticalLayout.addWidget(self.Cabecera)

        self.Cuerpo = QFrame(self.centralwidget)
        self.Cuerpo.setObjectName(u"Cuerpo")
        self.Cuerpo.setFrameShape(QFrame.Box)
        self.Cuerpo.setFrameShadow(QFrame.Raised)
        self.Cuerpo.setLineWidth(2)
        self.horizontalLayout_2 = QHBoxLayout(self.Cuerpo)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Parameters = QFrame(self.Cuerpo)
        self.Parameters.setObjectName(u"Parameters")
        self.Parameters.setFrameShape(QFrame.Box)
        self.Parameters.setFrameShadow(QFrame.Raised)
        self.Parameters.setLineWidth(2)
        self.verticalLayout_2 = QVBoxLayout(self.Parameters)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 5, 2, 5)
        self.parms_control = QFrame(self.Parameters)
        self.parms_control.setObjectName(u"parms_control")
        self.parms_control.setFrameShape(QFrame.StyledPanel)
        self.parms_control.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.parms_control)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.lblParameters = QLabel(self.parms_control)
        self.lblParameters.setObjectName(u"lblParameters")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lblParameters.sizePolicy().hasHeightForWidth())
        self.lblParameters.setSizePolicy(sizePolicy3)
        self.lblParameters.setFrameShape(QFrame.Box)
        self.lblParameters.setFrameShadow(QFrame.Raised)
        self.lblParameters.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lblParameters)

        self.ctlProcess = QFrame(self.parms_control)
        self.ctlProcess.setObjectName(u"ctlProcess")
        self.ctlProcess.setFrameShape(QFrame.StyledPanel)
        self.ctlProcess.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.ctlProcess)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setHorizontalSpacing(5)
        self.formLayout.setVerticalSpacing(5)
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.initFrameLabel = QLabel(self.ctlProcess)
        self.initFrameLabel.setObjectName(u"initFrameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.initFrameLabel)

        self.initFrameSpinBox = QSpinBox(self.ctlProcess)
        self.initFrameSpinBox.setObjectName(u"initFrameSpinBox")
        sizePolicy.setHeightForWidth(self.initFrameSpinBox.sizePolicy().hasHeightForWidth())
        self.initFrameSpinBox.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.initFrameSpinBox)

        self.finalFrameLabel = QLabel(self.ctlProcess)
        self.finalFrameLabel.setObjectName(u"finalFrameLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.finalFrameLabel)

        self.finalFrameSpinBox = QSpinBox(self.ctlProcess)
        self.finalFrameSpinBox.setObjectName(u"finalFrameSpinBox")
        sizePolicy.setHeightForWidth(self.finalFrameSpinBox.sizePolicy().hasHeightForWidth())
        self.finalFrameSpinBox.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.finalFrameSpinBox)

        self.modulationLabel = QLabel(self.ctlProcess)
        self.modulationLabel.setObjectName(u"modulationLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.modulationLabel)

        self.modulation = QDoubleSpinBox(self.ctlProcess)
        self.modulation.setObjectName(u"modulation")
        sizePolicy.setHeightForWidth(self.modulation.sizePolicy().hasHeightForWidth())
        self.modulation.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.modulation)


        self.verticalLayout_3.addWidget(self.ctlProcess)


        self.verticalLayout_2.addWidget(self.parms_control)

        self.parms_info = QFrame(self.Parameters)
        self.parms_info.setObjectName(u"parms_info")
        self.parms_info.setFrameShape(QFrame.StyledPanel)
        self.parms_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.parms_info)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.lblInfo = QLabel(self.parms_info)
        self.lblInfo.setObjectName(u"lblInfo")
        sizePolicy3.setHeightForWidth(self.lblInfo.sizePolicy().hasHeightForWidth())
        self.lblInfo.setSizePolicy(sizePolicy3)
        self.lblInfo.setFrameShape(QFrame.Box)
        self.lblInfo.setFrameShadow(QFrame.Raised)
        self.lblInfo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lblInfo)

        self.info_data = QFrame(self.parms_info)
        self.info_data.setObjectName(u"info_data")
        self.info_data.setFrameShape(QFrame.StyledPanel)
        self.info_data.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.info_data)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(5)
        self.formLayout_2.setVerticalSpacing(5)
        self.formLayout_2.setContentsMargins(5, 5, 5, 5)
        self.framesLabel = QLabel(self.info_data)
        self.framesLabel.setObjectName(u"framesLabel")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.framesLabel)

        self.framesSpinBox = QSpinBox(self.info_data)
        self.framesSpinBox.setObjectName(u"framesSpinBox")
        sizePolicy.setHeightForWidth(self.framesSpinBox.sizePolicy().hasHeightForWidth())
        self.framesSpinBox.setSizePolicy(sizePolicy)
        self.framesSpinBox.setMaximum(100000)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.framesSpinBox)

        self.frameRateLabel = QLabel(self.info_data)
        self.frameRateLabel.setObjectName(u"frameRateLabel")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.frameRateLabel)

        self.frameRate = QSpinBox(self.info_data)
        self.frameRate.setObjectName(u"frameRate")
        sizePolicy.setHeightForWidth(self.frameRate.sizePolicy().hasHeightForWidth())
        self.frameRate.setSizePolicy(sizePolicy)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.frameRate)

        self.heightLabel = QLabel(self.info_data)
        self.heightLabel.setObjectName(u"heightLabel")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.heightLabel)

        self.framesHeight = QSpinBox(self.info_data)
        self.framesHeight.setObjectName(u"framesHeight")
        sizePolicy.setHeightForWidth(self.framesHeight.sizePolicy().hasHeightForWidth())
        self.framesHeight.setSizePolicy(sizePolicy)
        self.framesHeight.setMaximum(4096)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.framesHeight)

        self.widthLabel = QLabel(self.info_data)
        self.widthLabel.setObjectName(u"widthLabel")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.widthLabel)

        self.frameWidth = QSpinBox(self.info_data)
        self.frameWidth.setObjectName(u"frameWidth")
        sizePolicy.setHeightForWidth(self.frameWidth.sizePolicy().hasHeightForWidth())
        self.frameWidth.setSizePolicy(sizePolicy)
        self.frameWidth.setMaximum(2048)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.frameWidth)

        self.durationLabel = QLabel(self.info_data)
        self.durationLabel.setObjectName(u"durationLabel")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.durationLabel)

        self.duration = QLineEdit(self.info_data)
        self.duration.setObjectName(u"duration")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.duration)


        self.verticalLayout_4.addWidget(self.info_data)


        self.verticalLayout_2.addWidget(self.parms_info)

        self.btnFullImage = QPushButton(self.Parameters)
        self.btnFullImage.setObjectName(u"btnFullImage")
        self.btnFullImage.setCheckable(True)

        self.verticalLayout_2.addWidget(self.btnFullImage)


        self.horizontalLayout_2.addWidget(self.Parameters)

        self.Process = QTabWidget(self.Cuerpo)
        self.Process.setObjectName(u"Process")
        self.Process.setDocumentMode(False)
        self.tabVideo = QWidget()
        self.tabVideo.setObjectName(u"tabVideo")
        self.tabVideo.setFocusPolicy(Qt.TabFocus)
        self.verticalLayout_8 = QVBoxLayout(self.tabVideo)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.frame_10 = QFrame(self.tabVideo)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Box)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.frame_12.setLineWidth(2)
        self.verticalLayout_16 = QVBoxLayout(self.frame_12)
        self.verticalLayout_16.setSpacing(3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(3, 3, 3, 3)
        self.mediaPlayer = QVideoWidget(self.frame_12)
        self.mediaPlayer.setObjectName(u"mediaPlayer")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.mediaPlayer.sizePolicy().hasHeightForWidth())
        self.mediaPlayer.setSizePolicy(sizePolicy4)

        self.verticalLayout_16.addWidget(self.mediaPlayer)


        self.horizontalLayout_6.addWidget(self.frame_12)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Box)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.frame_11.setLineWidth(2)
        self.verticalLayout_15 = QVBoxLayout(self.frame_11)
        self.verticalLayout_15.setSpacing(4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(2, 2, 2, 2)
        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy5)
        self.label_4.setFrameShape(QFrame.Box)
        self.label_4.setFrameShadow(QFrame.Raised)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_4)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setContentsMargins(2, 2, -1, -1)

        self.verticalLayout_15.addLayout(self.formLayout_4)


        self.horizontalLayout_6.addWidget(self.frame_11)

        self.horizontalLayout_6.setStretch(0, 4)
        self.horizontalLayout_6.setStretch(1, 2)

        self.verticalLayout_8.addWidget(self.frame_10)

        self.play_control = QFrame(self.tabVideo)
        self.play_control.setObjectName(u"play_control")
        self.play_control.setFrameShape(QFrame.StyledPanel)
        self.play_control.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.play_control)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.btnRew = QPushButton(self.play_control)
        self.btnRew.setObjectName(u"btnRew")
        self.btnRew.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.btnRew)

        self.btnStart = QPushButton(self.play_control)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.btnStart)

        self.btnStop = QPushButton(self.play_control)
        self.btnStop.setObjectName(u"btnStop")
        self.btnStop.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.btnStop)

        self.btnFor = QPushButton(self.play_control)
        self.btnFor.setObjectName(u"btnFor")
        self.btnFor.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.btnFor)

        self.videoSlider = QSlider(self.play_control)
        self.videoSlider.setObjectName(u"videoSlider")
        self.videoSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.videoSlider)


        self.verticalLayout_8.addWidget(self.play_control)

        self.verticalLayout_8.setStretch(0, 4)
        self.Process.addTab(self.tabVideo, "")
        self.tabFourierMethod = QWidget()
        self.tabFourierMethod.setObjectName(u"tabFourierMethod")
        self.verticalLayout_9 = QVBoxLayout(self.tabFourierMethod)
        self.verticalLayout_9.setSpacing(2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.frame_2 = QFrame(self.tabFourierMethod)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(2)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setSpacing(3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.Fourier_plot = QWidget(self.frame_2)
        self.Fourier_plot.setObjectName(u"Fourier_plot")
        self.horizontalLayout_8 = QHBoxLayout(self.Fourier_plot)
        self.horizontalLayout_8.setSpacing(4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.frame_6 = QFrame(self.Fourier_plot)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(4, 4, 4, 4)
        self.lblPhase = QLabel(self.frame_6)
        self.lblPhase.setObjectName(u"lblPhase")
        sizePolicy3.setHeightForWidth(self.lblPhase.sizePolicy().hasHeightForWidth())
        self.lblPhase.setSizePolicy(sizePolicy3)
        self.lblPhase.setScaledContents(False)
        self.lblPhase.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.lblPhase)

        self.imgThermogramAmplitud = QLabel(self.frame_6)
        self.imgThermogramAmplitud.setObjectName(u"imgThermogramAmplitud")
        self.imgThermogramAmplitud.setFrameShape(QFrame.Box)
        self.imgThermogramAmplitud.setFrameShadow(QFrame.Raised)
        self.imgThermogramAmplitud.setLineWidth(2)

        self.verticalLayout_6.addWidget(self.imgThermogramAmplitud)

        self.lblPhase_2 = QLabel(self.frame_6)
        self.lblPhase_2.setObjectName(u"lblPhase_2")
        sizePolicy3.setHeightForWidth(self.lblPhase_2.sizePolicy().hasHeightForWidth())
        self.lblPhase_2.setSizePolicy(sizePolicy3)
        self.lblPhase_2.setScaledContents(False)
        self.lblPhase_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.lblPhase_2)

        self.imgThermogramPhase = QLabel(self.frame_6)
        self.imgThermogramPhase.setObjectName(u"imgThermogramPhase")
        self.imgThermogramPhase.setFrameShape(QFrame.Box)
        self.imgThermogramPhase.setFrameShadow(QFrame.Raised)
        self.imgThermogramPhase.setLineWidth(2)

        self.verticalLayout_6.addWidget(self.imgThermogramPhase)


        self.horizontalLayout_8.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.Fourier_plot)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_7)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.lblPhase_3 = QLabel(self.frame_7)
        self.lblPhase_3.setObjectName(u"lblPhase_3")
        sizePolicy3.setHeightForWidth(self.lblPhase_3.sizePolicy().hasHeightForWidth())
        self.lblPhase_3.setSizePolicy(sizePolicy3)
        self.lblPhase_3.setScaledContents(False)
        self.lblPhase_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.lblPhase_3)

        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Box)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.frame_8.setLineWidth(2)
        self.verticalLayout_13 = QVBoxLayout(self.frame_8)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_19 = QFrame(self.frame_8)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy)
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)

        self.verticalLayout_13.addWidget(self.frame_19)

        self.btnSaveAmplitude = QPushButton(self.frame_8)
        self.btnSaveAmplitude.setObjectName(u"btnSaveAmplitude")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.btnSaveAmplitude.sizePolicy().hasHeightForWidth())
        self.btnSaveAmplitude.setSizePolicy(sizePolicy6)

        self.verticalLayout_13.addWidget(self.btnSaveAmplitude)

        self.frame_20 = QFrame(self.frame_8)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)

        self.verticalLayout_13.addWidget(self.frame_20)

        self.btnSaveAmplitudeData = QPushButton(self.frame_8)
        self.btnSaveAmplitudeData.setObjectName(u"btnSaveAmplitudeData")

        self.verticalLayout_13.addWidget(self.btnSaveAmplitudeData)

        self.frame_21 = QFrame(self.frame_8)
        self.frame_21.setObjectName(u"frame_21")
        sizePolicy.setHeightForWidth(self.frame_21.sizePolicy().hasHeightForWidth())
        self.frame_21.setSizePolicy(sizePolicy)
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.verticalLayout_13.addWidget(self.frame_21)


        self.verticalLayout_11.addWidget(self.frame_8)

        self.lblPhase_4 = QLabel(self.frame_7)
        self.lblPhase_4.setObjectName(u"lblPhase_4")
        sizePolicy3.setHeightForWidth(self.lblPhase_4.sizePolicy().hasHeightForWidth())
        self.lblPhase_4.setSizePolicy(sizePolicy3)
        self.lblPhase_4.setScaledContents(False)
        self.lblPhase_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.lblPhase_4)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Box)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_9.setLineWidth(2)
        self.verticalLayout_14 = QVBoxLayout(self.frame_9)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_22 = QFrame(self.frame_9)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy)
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)

        self.verticalLayout_14.addWidget(self.frame_22)

        self.btnSavePhase = QPushButton(self.frame_9)
        self.btnSavePhase.setObjectName(u"btnSavePhase")
        sizePolicy6.setHeightForWidth(self.btnSavePhase.sizePolicy().hasHeightForWidth())
        self.btnSavePhase.setSizePolicy(sizePolicy6)

        self.verticalLayout_14.addWidget(self.btnSavePhase)

        self.frame_23 = QFrame(self.frame_9)
        self.frame_23.setObjectName(u"frame_23")
        sizePolicy.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy)
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)

        self.verticalLayout_14.addWidget(self.frame_23)

        self.btnSavePhaseData = QPushButton(self.frame_9)
        self.btnSavePhaseData.setObjectName(u"btnSavePhaseData")

        self.verticalLayout_14.addWidget(self.btnSavePhaseData)

        self.frame_24 = QFrame(self.frame_9)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy)
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)

        self.verticalLayout_14.addWidget(self.frame_24)


        self.verticalLayout_11.addWidget(self.frame_9)


        self.horizontalLayout_8.addWidget(self.frame_7)


        self.horizontalLayout_4.addWidget(self.Fourier_plot)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_3)
        self.verticalLayout_7.setSpacing(4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(4, 4, 4, 4)
        self.lblInfo_Fourier = QLabel(self.frame_3)
        self.lblInfo_Fourier.setObjectName(u"lblInfo_Fourier")
        sizePolicy3.setHeightForWidth(self.lblInfo_Fourier.sizePolicy().hasHeightForWidth())
        self.lblInfo_Fourier.setSizePolicy(sizePolicy3)
        self.lblInfo_Fourier.setFrameShape(QFrame.Box)
        self.lblInfo_Fourier.setLineWidth(2)
        self.lblInfo_Fourier.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.lblInfo_Fourier)

        self.formFrame = QFrame(self.frame_3)
        self.formFrame.setObjectName(u"formFrame")
        self.formFrame.setFrameShape(QFrame.Box)
        self.formFrame.setFrameShadow(QFrame.Raised)
        self.formFrame.setLineWidth(2)
        self.verticalLayout_10 = QVBoxLayout(self.formFrame)
        self.verticalLayout_10.setSpacing(4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(4, 4, 4, 4)
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setContentsMargins(4, 4, 4, 4)
        self.digitalFrequencyLabel = QLabel(self.formFrame)
        self.digitalFrequencyLabel.setObjectName(u"digitalFrequencyLabel")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.digitalFrequencyLabel)

        self.digitalFrequency = QDoubleSpinBox(self.formFrame)
        self.digitalFrequency.setObjectName(u"digitalFrequency")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.digitalFrequency)

        self.frameRateLabel_2 = QLabel(self.formFrame)
        self.frameRateLabel_2.setObjectName(u"frameRateLabel_2")

        self.formLayout_5.setWidget(1, QFormLayout.LabelRole, self.frameRateLabel_2)

        self.frameRateSpinBox = QSpinBox(self.formFrame)
        self.frameRateSpinBox.setObjectName(u"frameRateSpinBox")

        self.formLayout_5.setWidget(1, QFormLayout.FieldRole, self.frameRateSpinBox)

        self.framesByLockInPeriodLabel = QLabel(self.formFrame)
        self.framesByLockInPeriodLabel.setObjectName(u"framesByLockInPeriodLabel")
        self.framesByLockInPeriodLabel.setScaledContents(True)
        self.framesByLockInPeriodLabel.setWordWrap(True)

        self.formLayout_5.setWidget(2, QFormLayout.LabelRole, self.framesByLockInPeriodLabel)

        self.framesByLockInPeriod = QSpinBox(self.formFrame)
        self.framesByLockInPeriod.setObjectName(u"framesByLockInPeriod")

        self.formLayout_5.setWidget(2, QFormLayout.FieldRole, self.framesByLockInPeriod)

        self.digitalFrequencyKLabel = QLabel(self.formFrame)
        self.digitalFrequencyKLabel.setObjectName(u"digitalFrequencyKLabel")

        self.formLayout_5.setWidget(3, QFormLayout.LabelRole, self.digitalFrequencyKLabel)

        self.digitalFrequencyK = QDoubleSpinBox(self.formFrame)
        self.digitalFrequencyK.setObjectName(u"digitalFrequencyK")

        self.formLayout_5.setWidget(3, QFormLayout.FieldRole, self.digitalFrequencyK)

        self.wNFactorLabel = QLabel(self.formFrame)
        self.wNFactorLabel.setObjectName(u"wNFactorLabel")

        self.formLayout_5.setWidget(4, QFormLayout.LabelRole, self.wNFactorLabel)

        self.wNFactor = QLineEdit(self.formFrame)
        self.wNFactor.setObjectName(u"wNFactor")

        self.formLayout_5.setWidget(4, QFormLayout.FieldRole, self.wNFactor)


        self.verticalLayout_10.addLayout(self.formLayout_5)

        self.label_3 = QLabel(self.formFrame)
        self.label_3.setObjectName(u"label_3")
        sizePolicy3.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy3)
        self.label_3.setFrameShape(QFrame.Box)
        self.label_3.setFrameShadow(QFrame.Raised)
        self.label_3.setLineWidth(2)

        self.verticalLayout_10.addWidget(self.label_3)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(6)
        self.formLayout_3.setVerticalSpacing(6)
        self.formLayout_3.setContentsMargins(4, 4, 4, 4)
        self.nCurrenLabel = QLabel(self.formFrame)
        self.nCurrenLabel.setObjectName(u"nCurrenLabel")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.nCurrenLabel)

        self.n_current = QSpinBox(self.formFrame)
        self.n_current.setObjectName(u"n_current")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.n_current)

        self.wKNLabel = QLabel(self.formFrame)
        self.wKNLabel.setObjectName(u"wKNLabel")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.wKNLabel)

        self.wKN_current = QLineEdit(self.formFrame)
        self.wKN_current.setObjectName(u"wKN_current")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.wKN_current)


        self.verticalLayout_10.addLayout(self.formLayout_3)


        self.verticalLayout_7.addWidget(self.formFrame)

        self.frame_25 = QFrame(self.frame_3)
        self.frame_25.setObjectName(u"frame_25")
        sizePolicy3.setHeightForWidth(self.frame_25.sizePolicy().hasHeightForWidth())
        self.frame_25.setSizePolicy(sizePolicy3)
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_9.setSpacing(4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(4, 4, 4, 4)
        self.btnResetProcessFourier = QPushButton(self.frame_25)
        self.btnResetProcessFourier.setObjectName(u"btnResetProcessFourier")
        self.btnResetProcessFourier.setEnabled(False)

        self.horizontalLayout_9.addWidget(self.btnResetProcessFourier)

        self.btnFourier_Execute = QPushButton(self.frame_25)
        self.btnFourier_Execute.setObjectName(u"btnFourier_Execute")
        self.btnFourier_Execute.setEnabled(False)
        self.btnFourier_Execute.setFlat(False)

        self.horizontalLayout_9.addWidget(self.btnFourier_Execute)


        self.verticalLayout_7.addWidget(self.frame_25)


        self.horizontalLayout_4.addWidget(self.frame_3)

        self.horizontalLayout_4.setStretch(0, 6)
        self.horizontalLayout_4.setStretch(1, 2)

        self.verticalLayout_9.addWidget(self.frame_2)

        self.Process.addTab(self.tabFourierMethod, "")
        self.tabGeometrical = QWidget()
        self.tabGeometrical.setObjectName(u"tabGeometrical")
        self.verticalLayout_17 = QVBoxLayout(self.tabGeometrical)
        self.verticalLayout_17.setSpacing(2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(2, 2, 2, 2)
        self.frame_13 = QFrame(self.tabGeometrical)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(4, 4, 4, 4)
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Box)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.frame_14.setLineWidth(2)
        self.verticalLayout_18 = QVBoxLayout(self.frame_14)
        self.verticalLayout_18.setSpacing(2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(4, 4, 4, 4)
        self.label_6 = QLabel(self.frame_14)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_6)

        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Box)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.frame_16.setLineWidth(2)

        self.verticalLayout_18.addWidget(self.frame_16)

        self.label_7 = QLabel(self.frame_14)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_7)

        self.frame_17 = QFrame(self.frame_14)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Box)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.frame_17.setLineWidth(2)

        self.verticalLayout_18.addWidget(self.frame_17)


        self.horizontalLayout_7.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Box)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.frame_15.setLineWidth(2)
        self.verticalLayout_19 = QVBoxLayout(self.frame_15)
        self.verticalLayout_19.setSpacing(4)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(4, 4, 4, 4)
        self.frame_18 = QFrame(self.frame_15)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Box)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.frame_18.setLineWidth(2)

        self.verticalLayout_19.addWidget(self.frame_18)

        self.btnGeometrical = QPushButton(self.frame_15)
        self.btnGeometrical.setObjectName(u"btnGeometrical")

        self.verticalLayout_19.addWidget(self.btnGeometrical)

        self.verticalLayout_19.setStretch(0, 8)
        self.verticalLayout_19.setStretch(1, 2)

        self.horizontalLayout_7.addWidget(self.frame_15)

        self.horizontalLayout_7.setStretch(0, 6)
        self.horizontalLayout_7.setStretch(1, 3)

        self.verticalLayout_17.addWidget(self.frame_13)

        self.Process.addTab(self.tabGeometrical, "")
        self.tabResult = QWidget()
        self.tabResult.setObjectName(u"tabResult")
        self.verticalLayout_5 = QVBoxLayout(self.tabResult)
        self.verticalLayout_5.setSpacing(2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.frame = QFrame(self.tabResult)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(2)
        self.horizontalLayout_5 = QHBoxLayout(self.frame)
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(4, 4, 4, 4)
        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_4)
        self.verticalLayout_12.setSpacing(2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(4, 4, 4, 4)
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        sizePolicy3.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy3)
        self.label_5.setFrameShape(QFrame.Box)
        self.label_5.setFrameShadow(QFrame.Raised)
        self.label_5.setLineWidth(2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_5)

        self.imgSegmentacionAmplitud = QLabel(self.frame_4)
        self.imgSegmentacionAmplitud.setObjectName(u"imgSegmentacionAmplitud")
        self.imgSegmentacionAmplitud.setFrameShape(QFrame.Box)
        self.imgSegmentacionAmplitud.setFrameShadow(QFrame.Raised)
        self.imgSegmentacionAmplitud.setLineWidth(2)

        self.verticalLayout_12.addWidget(self.imgSegmentacionAmplitud)

        self.btnSegment = QPushButton(self.frame_4)
        self.btnSegment.setObjectName(u"btnSegment")

        self.verticalLayout_12.addWidget(self.btnSegment)


        self.horizontalLayout_5.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_5)


        self.verticalLayout_5.addWidget(self.frame)

        self.Process.addTab(self.tabResult, "")

        self.horizontalLayout_2.addWidget(self.Process)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)

        self.verticalLayout.addWidget(self.Cuerpo)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 975, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuProcess = QMenu(self.menubar)
        self.menuProcess.setObjectName(u"menuProcess")
        self.menuManual = QMenu(self.menuProcess)
        self.menuManual.setObjectName(u"menuManual")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        icon3 = QIcon()
        iconThemeName = u"system-help"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.menuHelp.setIcon(icon3)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuProcess.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuProcess.addAction(self.actionExecute)
        self.menuProcess.addAction(self.menuManual.menuAction())
        self.menuManual.addAction(self.actionImage_Generation)
        self.menuManual.addAction(self.actionLockIn)

        self.retranslateUi(MainWindow)

        self.Process.setCurrentIndex(1)
        self.btnStart.setDefault(True)
        self.btnFourier_Execute.setDefault(True)
        self.btnGeometrical.setDefault(True)
        self.btnSegment.setDefault(True)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.actionExecute.setText(QCoreApplication.translate("MainWindow", u"Automatic", None))
#if QT_CONFIG(shortcut)
        self.actionExecute.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionImage_Generation.setText(QCoreApplication.translate("MainWindow", u"Image Generation", None))
        self.actionLockIn.setText(QCoreApplication.translate("MainWindow", u"LockIn", None))
        self.LogoCicata.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">D</span><span style=\" font-size:16pt;\">igital </span><span style=\" font-size:16pt; font-weight:700;\">I</span><span style=\" font-size:16pt;\">maging </span><span style=\" font-size:16pt; font-weight:700;\">T</span><span style=\" font-size:16pt;\">hermography </span><span style=\" font-size:16pt; font-weight:700;\">P</span><span style=\" font-size:16pt;\">rocessing</span></p><p align=\"center\"><span style=\" font-size:16pt;\">Developed  by PhD Eduardo Vargas Bernardino</span></p><p align=\"center\"><span style=\" font-size:16pt;\">CICATA Legaria, IPN, CITNOVA</span></p></body></html>", None))
        self.label_2.setText("")
        self.lblParameters.setText(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.initFrameLabel.setText(QCoreApplication.translate("MainWindow", u"Init Frame", None))
        self.finalFrameLabel.setText(QCoreApplication.translate("MainWindow", u"Final Frame", None))
        self.modulationLabel.setText(QCoreApplication.translate("MainWindow", u"Modulation", None))
        self.modulation.setSuffix(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.lblInfo.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.framesLabel.setText(QCoreApplication.translate("MainWindow", u"Frames", None))
        self.frameRateLabel.setText(QCoreApplication.translate("MainWindow", u"Frame Rate", None))
        self.frameRate.setSuffix(QCoreApplication.translate("MainWindow", u" fps", None))
        self.frameRate.setPrefix("")
        self.heightLabel.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.framesHeight.setSuffix(QCoreApplication.translate("MainWindow", u"px", None))
        self.widthLabel.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.frameWidth.setSuffix(QCoreApplication.translate("MainWindow", u"px", None))
        self.frameWidth.setPrefix("")
        self.durationLabel.setText(QCoreApplication.translate("MainWindow", u"Duration:", None))
        self.btnFullImage.setText(QCoreApplication.translate("MainWindow", u"Full Image", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Measurement related with", None))
        self.btnRew.setText(QCoreApplication.translate("MainWindow", u"REWIND", None))
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u"PLAY", None))
        self.btnStop.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.btnFor.setText(QCoreApplication.translate("MainWindow", u"FORWARD", None))
        self.Process.setTabText(self.Process.indexOf(self.tabVideo), QCoreApplication.translate("MainWindow", u"Video", None))
        self.lblPhase.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Amplitude</span></p></body></html>", None))
        self.imgThermogramAmplitud.setText("")
        self.lblPhase_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Phase</span></p></body></html>", None))
        self.imgThermogramPhase.setText("")
        self.lblPhase_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Amplitude</span></p></body></html>", None))
        self.btnSaveAmplitude.setText(QCoreApplication.translate("MainWindow", u"Export Graphic", None))
        self.btnSaveAmplitudeData.setText(QCoreApplication.translate("MainWindow", u"Export Data", None))
        self.lblPhase_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Phase</span></p></body></html>", None))
        self.btnSavePhase.setText(QCoreApplication.translate("MainWindow", u"Export Graphic", None))
        self.btnSavePhaseData.setText(QCoreApplication.translate("MainWindow", u"Export Data", None))
        self.lblInfo_Fourier.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Information</span></p></body></html>", None))
        self.digitalFrequencyLabel.setText(QCoreApplication.translate("MainWindow", u"Lock-In Frequency", None))
        self.digitalFrequency.setSuffix(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.frameRateLabel_2.setText(QCoreApplication.translate("MainWindow", u"Frame Rate", None))
        self.frameRateSpinBox.setSuffix(QCoreApplication.translate("MainWindow", u"fps", None))
        self.framesByLockInPeriodLabel.setText(QCoreApplication.translate("MainWindow", u"Frames by Lock-in Period (N)", None))
        self.digitalFrequencyKLabel.setText(QCoreApplication.translate("MainWindow", u"Digital Frequency (K)", None))
        self.wNFactorLabel.setText(QCoreApplication.translate("MainWindow", u"W Factor", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Current Frame</span></p></body></html>", None))
        self.nCurrenLabel.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.wKNLabel.setText(QCoreApplication.translate("MainWindow", u"W(K,N)", None))
        self.btnResetProcessFourier.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.btnFourier_Execute.setText(QCoreApplication.translate("MainWindow", u"Execute", None))
        self.Process.setTabText(self.Process.indexOf(self.tabFourierMethod), QCoreApplication.translate("MainWindow", u"Fourier Method", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Amplitude</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Phase</span></p></body></html>", None))
        self.btnGeometrical.setText(QCoreApplication.translate("MainWindow", u"Execute", None))
        self.Process.setTabText(self.Process.indexOf(self.tabGeometrical), QCoreApplication.translate("MainWindow", u"Geometrical Method", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Segmentation", None))
        self.imgSegmentacionAmplitud.setText("")
        self.btnSegment.setText(QCoreApplication.translate("MainWindow", u"Segment", None))
        self.Process.setTabText(self.Process.indexOf(self.tabResult), QCoreApplication.translate("MainWindow", u"Results", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuProcess.setTitle(QCoreApplication.translate("MainWindow", u"Process", None))
        self.menuManual.setTitle(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

