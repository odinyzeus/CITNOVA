import sys, cv2
import Function.Basics as Basics
from Function.Methods import Fourier as fm
from Function.Methods import Geometrical as gm
import numpy as np
from PySide6 import QtWidgets as Wigdets
from PySide6 import QtGui as Gui
from PySide6 import QtMultimedia as Media
from pathlib import Path
from UI.Ui_principal import Ui_MainWindow as Win
from cv2.typing import MatLike

# Only needed for access to command line arguments

# Define the main window class
class MainWindow(Wigdets.QMainWindow):
    ui                = Win()

    # Estas variables almacenan la carpeta de trabajo para procesamiento de video y el video a procesar
    __FilePath          = str             # Represents the complete path of the video to process
    __TempPath          = str             # Represents the path of the temporal work area
    mediaPlayer         = Media.QMediaPlayer()
    video               = MatLike # Esta Variable almacena el video para procesamiento por OpenCV
    dataExperiment      = {'FrameRate':int,'Modulation':float,'ModulationPeriod':float,'FramePeriod':int, 'FramesByPeriod':int , 'Periods': int , 'InitFrame': int,'Frames':int,'FullImage':False}
    count               = int         
    progress            = 0
    mf                  = fm()
    mg                  = gm()

    referenceSenSignal  = None
    referenceCosSignal  = None
    # __thermography      = tg()
    # __fourier_method    = fm()
    
    """ Lamda Functions Section"""
    __absPath = lambda _ , p :  str(Path(p).parent) # Returns the absolut path of the file passed

    # Se crea el modelo de datos para insertar datos en listas
    listModelItem = Gui.QStandardItemModel()
    
    def __init__(self):
        # construimos el menú
        super().__init__()
        self.ui.setupUi(self)


        self.ui.progressBar.setValue(0)
        self.ui.videoSlider.setValue(0)

        validator = Gui.QDoubleValidator()
        validator.setNotation(Gui.QDoubleValidator.ScientificNotation)
        self.ui.wNFactor.setValidator(validator)
        self.ui.wKN_current.setValidator(validator)

        self.ui.actionOpen.triggered.connect(lambda: Basics.openFile(self)) # Se configura la accion del menu para abrir archivo de video 
        self.mediaPlayer.setVideoOutput(self.ui.mediaPlayer)  # Se configura el control que servirà de repoductor multimedia 
        self.ui.frameRate.valueChanged.connect(lambda: self.setFrameRate())     # Se ejecuta cada que la frecuencia de muestreo del video Cambia
        self.ui.modulation.valueChanged.connect(lambda: self.setModulation())        # Se ejecuta cada que la frecuencia de modulacion cambia
        self.ui.initFrameSpinBox.valueChanged.connect(lambda: self.setInitFrame())           # InitFrame
        self.ui.finalFrameSpinBox.valueChanged.connect(lambda: self.setInitFrame())         # FinalFrame
        self.ui.btnStart.clicked.connect(lambda: Basics.playvideo(self))
        self.ui.btnStop.clicked.connect(lambda: Basics.stopvideo(self))
        self.ui.btnRew.clicked.connect(lambda: Basics.backvideo(self))
        self.ui.btnFor.clicked.connect(lambda: Basics.forwardvideo(self))
        self.ui.videoSlider.valueChanged.connect(lambda: Basics.move_video(self))
        self.mediaPlayer.positionChanged.connect(lambda: Basics.media_position(self))
        self.ui.progressBar.valueChanged.connect(lambda: Basics.setProgress(self))
        self.ui.btnFourier_Execute.clicked.connect(lambda: self.Fourier_Execute())
        self.ui.btnGeometrical.clicked.connect(lambda: self.Geometrical_Execute())
        self.ui.btnFullImage.clicked.connect(lambda: self.setFullsize())
        self.ui.btnSegment.clicked.connect(lambda: self.setSegment() )
        self.ui.btnSaveAmplitude.clicked.connect(lambda: Basics.ExportImgAmplitudeFourier(self.mf))
        self.ui.btnSaveAmplitudeData.clicked.connect(lambda: Basics.ExportDataAmplitudeFourier(self.mf))
        self.ui.btnSavePhase.clicked.connect(lambda: Basics.ExportImgPhaseFourier(self.mf))
        self.ui.btnSavePhaseData.clicked.connect(lambda: Basics.ExportDataPhaseFourier(self.mf))
        self.ui.btnResetProcessFourier.clicked.connect(lambda estado: self.ResetProcessFourier(estado))



        # Se registra la aplicacion como receptor de eventos para la clase que procesa el metodo de fourier
        self.mf.register(self)
        self.mg.register(self)

    def setSegment(self):
        self.ui.statusbar.showMessage('Segmenting the last frame......')
        black =  self.mf.Thermogram_Phase
        pha = Basics.imgUmbralize(black, 180, 220)
        pha = Basics.imgContours(pha,  self.mf.kernel)

        pha = Gui.QImage(pha.data, pha.shape[1], pha.shape[0], Gui.QImage.Format_Grayscale8)
        # Creamos una imagen en blanco del mismo tamaño que la original
        # imagen_contornos = np.zeros_like(black)
        
        self.ui.imgSegmentacionAmplitud.setPixmap(Gui.QPixmap.fromImage(pha))


    def ResetProcessFourier(self,value: bool):
        self.mf.reset = value
        
        
    #  Execute the Fourier Method
    def Fourier_Execute(self):
        while True:
            ret, img = self.video.read()
            if ret:
                self.mf.Thermogram = img
            else:
                break
    
    #  Execute the Geometrical Method
    def Geometrical_Execute(self):
        while True:    
            ret, img = self.video.read()
            if ret:
                self.mg.Thermogram = img
                z= self.mg.Thermogram
            else:
                break        



    def setInitFrame(self):
        self.video.set(cv2.CAP_PROP_POS_FRAMES ,self.ui.initFrameSpinBox.value() )   # Se establece la posicion del video en el Frame Inicial
        self.ui.statusbar.showMessage(f'Frame Init has been established to frame No.:{int(self.video.get(cv2.CAP_PROP_POS_FRAMES))}')  
        self.mf.Frames = Basics.calculateFrames(self.ui.finalFrameSpinBox , self.ui.initFrameSpinBox, self.ui.framesSpinBox)

    def setFullsize(self):
        self.mf.isImageFull = self.ui.btnFullImage.isChecked()

    def setModulation(self):
        self.mf.Modulation  = self.ui.modulation.value()
        self.ui.digitalFrequency.setValue(self.mf.Modulation)
        self.ui.digitalFrequencyK.setValue(self.mf.K)
        self.ui.framesByLockInPeriod.setValue(self.mf.N)                                            # Updates in setFrameRate too
        self.ui.wNFactor.setText("{:.3f}{:+.3f}j".format(self.mf.W.real, self.mf.W.imag)) # Updates in setFrameRate too
    
    def setFrameRate(self):
        self.mf.FrameRate =self.ui.frameRate.value()
        self.ui.frameRateSpinBox.setValue(self.mf.FrameRate)
        self.mf.Modulation = self.ui.modulation.value()
        self.ui.framesByLockInPeriod.setValue(self.mf.N)                                             # Updates in Set Modulation too
        self.ui.wNFactor.setText("{:.3f}{:+.3f}j".format(self.mf.W.real, self.mf.W.imag)) # Updates in setFrameRate too
       
       
       
        # # Se configura el boton de processar el methodo thermografico elegido
        # self.__ui.btnMethod.clicked.connect(lambda: bf.execute(self))
        
        # # Se ejecuta cada que se selecciona el metodo de proceso geometrico
        # self.__ui.btnGeometry.clicked.connect(lambda: bf.Method_selected(self, 0))
        
        # # Se ejecuta cada que se selecciona el metodo de proceso de cuatro puntos
        # self.__ui.btnFourPoints.clicked.connect(lambda: bf.Method_selected(self, 1))
    
        # # Se ejecuta cada que se selecciona el metodo de proceso de fourier
        # self.__ui.btnFourier.clicked.connect(lambda: bf.Method_selected(self, 2))
        
    # Se ejecuta cada que se actualiza el valor de la barra de progreso
    def Porcentage_Changed(self,event):
        self.ui.wKN_current.setText("{:.3f}{:+.3f}j".format(self.mf.WN.real, self.mf.WN.imag))
        self.ui.progressBar.setValue(event)
        self.ui.n_current.setValue(self.mf.currentPeriod)
        self.ui.statusbar.showMessage(f'Processing frame.:{self.mf.CurrentFrame}')
        self.ui.btnResetProcessFourier.setEnabled(self.mf.CurrentFrame > 1)

    def CurrentImage_Processed(self, event):
        # Normalizar la matriz para que sus valores estén entre 0 y 255
        amp = Basics.imgNormalize(self.mf.Thermogram_Amplitude) 
        pha = Basics.imgNormalize(self.mf.Thermogram_Phase) 

        # Convertir la matriz a una imagen QImage        
        amp = Gui.QImage(amp.data, amp.shape[1], amp.shape[0], Gui.QImage.Format_Grayscale8)
        pha = Gui.QImage(pha.data, pha.shape[1], pha.shape[0], Gui.QImage.Format_Grayscale8)
        self.ui.imgThermogramAmplitud.setPixmap(Gui.QPixmap.fromImage(amp))
        self.ui.imgThermogramPhase.setPixmap(Gui.QPixmap.fromImage(pha))
        
        #if self.mf.CurrentFrame % self.mf.FrameRate == 0:
            
        
        #     ampU = Basics.imgUmbralize(self.mf.Thermogram_Amplitude, 180, 200)
        #     phaU = Basics.imgUmbralize(self.mf.Thermogram_Phase, 180, 220)

        #     
        #     ampU= Gui.QImage(ampU.data, ampU.shape[1],ampU.shape[0],Gui.QImage.Format_Grayscale8)
        #     phaU= Gui.QImage(phaU.data, phaU.shape[1],phaU.shape[0],Gui.QImage.Format_Grayscale8)

            
        #     self.ui.imgContornoPhase.setPixmap(Gui.QPixmap.fromImage(phaU))
        #     self.ui.imgContornoAmplitud.setPixmap(Gui.QPixmap.fromImage(ampU))
        

if __name__ ==  '__main__':
    app = Wigdets.QApplication(sys.argv)
    mi_application = MainWindow()
    mi_application.show()
    sys.exit(app.exec_())