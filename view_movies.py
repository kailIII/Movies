import sys
from PySide import QtGui,QtCore
from movies import Ui_MainWindow
import controller
import os

class Movies(QtGui.QMainWindow):
    """Clase principal del programa"""
    table_columns =(
        (u"Titulo",100),
        (u"Director",150),
        (u"Pais",100),
        (u"Ranking",75))

    def __init__(self):
        """Cosntructor del programa"""
        super(Movies, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.load_movies()
        #self.connect(self.ui.tableView,QtCore.SIGNAL("clicked()"),self.infoMovies)
        self.ui.tableView.clicked.connect(self.infoMovies)
        #self.infoMovies()
        self.ui.subir.clicked.connect(self.subir)
        self.ui.bajar.clicked.connect(self.bajar)
        self.show()

    def load_movies(self):
        """Funcion que carga la base de datos en la interfaz"""
        movies = controller.obtener_movies()
        row = len(movies)
        model =QtGui.QStandardItemModel(
            row,len(self.table_columns))
        self.ui.tableView.setModel(model)
        self.ui.tableView.horizontalHeader().setResizeMode(0,self.ui.tableView.horizontalHeader().Stretch)

        for col,h in enumerate(self.table_columns):
            model.setHeaderData(col,QtCore.Qt.Horizontal,h[0])
            self.ui.tableView.setColumnWidth(col,h[1])

        for i,data in enumerate(movies):
            row = [data[1],data[4],data[5],data[8]]
            for j,field in enumerate(row):
                index = model.index(i,j,QtCore.QModelIndex())
                model.setData(index,field)

    def infoMovies(self):
        model = self.ui.tableView.model()
        index = self.ui.tableView.currentIndex()
        codigo = model.index(index.row(), 3, QtCore.QModelIndex()).data()
        valores = controller.infoFila2(codigo)
        self.ui.titulo.setText(valores[1])
        self.ui.descripcion.setText(valores[7])
        ficheros = os.listdir('Img/')
        fichero = valores[2] in ficheros
        if fichero is True:
            direccion = 'Img/{0}'.format(valores[2])
            self.ui.setImageLabel(direccion)
        else:
            fichero = valores[2] + ".png" in ficheros
            if fichero is True:
                direccion = 'Img/{0}'.format(valores[2])
                self.ui.setImageLabel(direccion)


    def subir(self):
        index = self.ui.tableView.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.setWindowTitle("ERROR!")
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
        else:
            model = self.ui.tableView.model()
            index = self.ui.tableView.currentIndex()
            codigo = model.index(index.row(), 3, QtCore.QModelIndex()).data()
            if(codigo!=1):
                codigo2 = model.index(index.row()-1, 3, QtCore.QModelIndex()).data()
                valores = controller.infoFila(codigo)
                valores2 = controller.infoFila(codigo2)
                controller.subir(codigo,valores2)
                controller.subir(codigo2,valores)
            else:
                self.errorMessageDialog = QtGui.QErrorMessage(self)
                self.errorMessageDialog.setWindowTitle("ERROR!")
                self.errorMessageDialog.showMessage("No puede subir mas el ranking")
        self.load_movies()

    def bajar(self):
        index = self.ui.tableView.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.setWindowTitle("ERROR!")
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
        else:
            model = self.ui.tableView.model()
            index = self.ui.tableView.currentIndex()
            codigo = model.index(index.row(), 3, QtCore.QModelIndex()).data()
            if(codigo!=7):
                codigo2 = model.index(index.row()+1, 3, QtCore.QModelIndex()).data()
                valores = controller.infoFila(codigo)
                valores2 = controller.infoFila(codigo2)
                controller.subir(codigo,valores2)
                controller.subir(codigo2,valores)
            else:
                self.errorMessageDialog = QtGui.QErrorMessage(self)
                self.errorMessageDialog.setWindowTitle("ERROR!")
                self.errorMessageDialog.showMessage("No puede bajar mas el ranking")
        self.load_movies()


if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    main = Movies()
    sys.exit(app.exec_())