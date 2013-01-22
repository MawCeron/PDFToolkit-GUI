#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
#   "LICENCIA DEL CAFÉ"
#
#   Haz lo que quieras con este código: Míralo, compártelo, modifícalo,
#   estúdialo... y si algún día nos encontramos y crees que te ha sido
#   útil, invítame a un café, a una cerveza o a algo equivalente.
#   Y si en tu código adaptado del mío quieres poner "Basado en el código
#   original de Mauricio 'Maw' Cerón - <ceron.maw@gmail.com>",
#   te lo agradeceré un montón, aunque si no quieres, pues no lo hagas...
#

import sys, os
from PyQt4 import QtCore, QtGui
from gui import Ui_MainWindow

class principal(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        # Importo la clase MainWindow de de la GUI
        self.ventana = Ui_MainWindow()
        self.ventana.setupUi(self)
        
        # Se determina la acción que realizará cada botón al darle clic
        # Botones del área de Archivos de Entrada
        self.connect(self.ventana.btAdd, QtCore.SIGNAL('clicked()'), self.agregar)
        self.connect(self.ventana.btQuit, QtCore.SIGNAL('clicked()'), self.quitar)
        self.connect(self.ventana.btQuitAll, QtCore.SIGNAL('clicked()'), self.quitarTodo)
        self.connect(self.ventana.btUp, QtCore.SIGNAL('clicked()'), self.subir)
        self.connect(self.ventana.btDown, QtCore.SIGNAL('clicked()'), self.bajar)
        
        # Botón del área de Archivo de Salida
        self.connect(self.ventana.btSearch, QtCore.SIGNAL('clicked()'), self.buscar)
        
        # Botones independientes
        self.connect(self.ventana.btExit, QtCore.SIGNAL('clicked()'), QtCore.SLOT('close()'))
        self.connect(self.ventana.btMerge, QtCore.SIGNAL('clicked()'), self.unir)

    def agregar(self):
        dialog = QtGui.QFileDialog # Llamo un dialogo 
        home = os.getenv('HOME') # Obtengo la ruta de HOME dependiendo del SO en que se ejecute
        nombresArchivos = dialog.getOpenFileNames(self, "Seleccionar Archivos", home, "Documentos PDF (*.pdf)") # Llamo al dialogo que obtenga los archivos del tipo PDF
        self.ventana.listWidget.addItems(nombresArchivos) # Agrego los 'paths' a la lista
    
    def quitar(self):
        # Toma la fila seleccionada de la lista y borra su contenido
        item = self.ventana.listWidget.takeItem(self.ventana.listWidget.currentRow())
        item = None
    
    def quitarTodo(self):
        self.ventana.listWidget.clear()
        
    def subir(self):
        # Mueve la fila seleccionada una posición hacia arriba dentro de los elementos de la lista
        currentRow = self.ventana.listWidget.currentRow()
        currentItem = self.ventana.listWidget.takeItem(currentRow)
        self.ventana.listWidget.insertItem(currentRow - 1, currentItem)
       
       # Mantiene resaltada la selección del usuario mientras se mueve.
        if currentRow > 0:
            self.ventana.listWidget.setCurrentRow(currentRow - 1)
        elif currentRow == 0:
            self.ventana.listWidget.setCurrentRow(0)
    
    def bajar(self):
        currentRow = self.ventana.listWidget.currentRow()
        currentItem = self.ventana.listWidget.takeItem(currentRow)
        self.ventana.listWidget.insertItem(currentRow + 1, currentItem)
        
        maximum = self.ventana.listWidget.count() - 1
        if currentRow < maximum:
            self.ventana.listWidget.setCurrentRow(currentRow + 1)
        elif currentRow == maximum:
            self.ventana.listWidget.setCurrentRow(maximum)
            
    def buscar(self):
        dialog = QtGui.QFileDialog
        home = os.getenv('HOME')
        textBox = self.ventana.tbOutput
        salida = dialog.getSaveFileName(self, "Seleccione ruta de salida", home + "/output.pdf", "Documento PDF (*.pdf)")
        textBox.setText(salida)
    
    def unir(self):
        
        # Función que muestra mensaje al finalizar el proceso        
        def mensaje(self):
            QtGui.QMessageBox.about(self, "PDF Tool Kit GUI", u"La unión de los archivos se ha realizado con éxito.")
            
        # Obtengo la ruta de salida
        output = self.ventana.tbOutput.text()
        # Creo la QStringList para los archivos a unir        
        self.file = QtCore.QStringList()
        arguments = self.file
        lista = self.ventana.listWidget
        
        # Convierto el QListWidget con los archivos a unir en una QStringList
        cuenta = lista.count()
        for index in range(cuenta):
            arguments.append(lista.item(index).text())
        
        # Agrego el resto de los argumentos al QStringList       
        arguments.append("cat output")
        arguments.append(output)
        
        # Convierto la lista en un solo String para solicitar el comando
        command = "pdftk"
        for i in range(arguments.count()):
            command = command + " " + arguments[i]
        # Agrego todos los datos para el proceso
        comand = unicode(command, "utf-8")
        orden = comand.encode( "utf-8" )
        os.system(str(orden))
        
        # Muestro el mensaje
        mensaje(self)
        
        # Limpio la lista y el textbox por si hay que crear más archivos
        self.ventana.listWidget.clear()
        self.ventana.tbOutput.clear()

def main():
    app = QtGui.QApplication(sys.argv)
    ventana = principal()
    ventana.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
    
    
