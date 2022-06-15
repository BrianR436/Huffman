from PySide6.QtWidgets import QApplication,QMainWindow,QMessageBox, QTableWidgetItem
from interfaz.ui_InterfazHufman import Ui_Form
import six
import io
import re
import sys
import os
class Node:#Clase nodo
    def __init__(self,freq):
        self.left = None
        self.right = None
        self.father = None
        self.freq = freq
 
    def is_left(self):
        return self.father.left == self
class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ejecutar.clicked.connect(self.extraer_ruta)
        self.ruta.returnPressed.connect(self.extraer_ruta)#para dar enter y que el programa corra

    def extraer_ruta(self):
        try:
            RUTA = self.ruta.text() 
            archivo = io.open(RUTA,mode='r',encoding="utf-8")
        except Exception as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No se encontro ningun archivo de texto .TXT")
            msg.setWindowTitle("ERROR")
            msg.setStandardButtons(QMessageBox.Close)
            msg.exec()    
        self.correr_programa(RUTA)
    def crear_nodos(self,frequencies):
        return [Node(freq) for freq in frequencies]
    #huffmanFunción de generación de árboles
    def crear_raiz_huffman(self,nodes):
        queue = nodes[:]
        while len(queue) > 1:
            queue.sort(key=lambda item: item.freq)
            node_left = queue.pop(0)
            node_right = queue.pop(0)
            node_father = Node(node_left.freq + node_right.freq)
            node_father.left = node_left
            node_father.right = node_right
            node_left.father = node_father
            node_right.father = node_father
            queue.append(node_father)
        queue[0].father = None
        return queue[0]
    #Generar código huffman según árbol huffman
    def generar_arbol(self,nodes, root):
        codes = [''] * len(nodes)
        for i in range(len(nodes)):
            node_tmp = nodes[i]
            while node_tmp != root:
                if node_tmp.is_left():
                    codes[i] = '0' + codes[i]
                else:
                    codes[i] = '1' + codes[i]
                node_tmp = node_tmp.father
        return codes
    # Obtener la frecuencia de los caractere
    def frecuencia_caracteres(self,input_string):
        # Se usa para almacenar caracteres
        char_store = []
        # Se usa para almacenar frecuencia
        freq_store = []
    
        # Analizar cadena
        for index in range(len(input_string)):
            if char_store.count(input_string[index]) > 0:
                temp = int(freq_store[char_store.index(input_string[index])])
                temp = temp + 1
                freq_store[char_store.index(input_string[index])] = temp
            else:
                char_store.append(input_string[index])
                freq_store.append(1)

        return char_store, freq_store
    # Obtener una lista de caracteres y frecuencias
    def probabilidad(self,char_store=[], freq_store=[]):
        # Se usa para almacenar char_frequency
        char_frequency = []
        for item in zip(char_store, freq_store):
            temp = (item[0], item[1])
            char_frequency.append(temp)        
        return char_frequency
    #Conversión de #Coding
    def generar_archivo(self,code):
        f=open("Comprimido.txt","wb")
        out=0
        while len(code)>8:
            for x in range(8):
                out=out<<1
                if code[x]=="1":
                    out=out|1
            code=code[8:]
            f.write(six.int2byte(out))
            out=0

        f.write(six.int2byte(len(code)))
        out=0
        for i in range(len(code)):
            out=out<<1
            if code[i]=="1":
                out=out|1
        
        for i in range(8-len(code)):
            out=out<<1
        f.write(six.int2byte(out)) 
        f.close()
        return True
    # Convertir caracteres a codificación huffman
    def genera_codigo(self,input_string, char_frequency, codes,char_store,char_freq_store,numero_caracteres):
        # Reemplazar carácter por carácter
        file_content = ''
        n=int(0)
        for index in range(len(input_string)):
            for item in zip(char_frequency, codes):
                if input_string[index] == item[0][0]:
                    file_content = file_content + item[1]
                    #print(input_string[index],"Codigo huffman "+item[1])
                    self.tabla.insertRow(n)
                    e= str(item[1])
                    texto4 = QTableWidgetItem(input_string[index])
                    self.tabla.setItem(n,0,texto4)
                    texto5 = QTableWidgetItem(e)
                    self.tabla.setItem(n,1,texto5)
                    n=n+1
        c=''
        f=-1
        longitud_codigo= 0
        for item in zip(char_store, char_freq_store):
            temp = (item[0], item[1]) 
            f=f+1
            codigo=codes[f]
            veces=int(item[1])
            c=str(codigo)
            longitud_codigo=longitud_codigo+len(c)*((veces)/numero_caracteres) 
        longitud_codigo = round(longitud_codigo,2)
        media = str(longitud_codigo)
        texto2 = QTableWidgetItem(media)
        self.tableWidget.setItem(3,0,texto2)
        return file_content
    def mostrar_ruta(self):
    
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Su archivo se ha guardado con el nombre: Comprimido.txt")
        msg.setInformativeText("Se encuentra en la misma carpeta del programa")
        msg.setWindowTitle("EXITOSO")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec()   
    def correr_programa(self,RUTA):
        fo=io.open(RUTA, mode='r', encoding="utf-8")# Lee el archivo a comprimir
        input_string=fo.read()
        t = input_string.splitlines()
        t1 = len(t)-1
        sinsaltos = len(input_string)
        numero_caracteres = sinsaltos
        numero = str(numero_caracteres)
        texto1 =QTableWidgetItem(numero)
        self.tableWidget.setItem(1,0,texto1)
        t=re.sub(r"\s+","",input_string)#Quito los espacios
        t1=t.strip("\n")#Quito saltos de linea
        fo.close()
        char_store, freq_store=self.frecuencia_caracteres(t1)# Estadísticas de aparicioned de caracteres
        char_frequency=self.probabilidad(char_store,freq_store)# Estadísticas de banda
        nodes=self.crear_nodos([i[1] for i in char_frequency])# Generación de nodos
        root= self.crear_raiz_huffman(nodes)# Marcar el nodo raíz
        codes=self.generar_arbol(nodes,root)#Generar árbol huffman
        save_file=self.genera_codigo(t1,char_frequency,codes,char_store,freq_store,numero_caracteres)# De acuerdo con el árbol de huffman generado, genera código de huffman
        self.generar_archivo(save_file)#Escribe la cadena de 01 bit en el archivo bit a bit    
        archivo_codificado = os.stat('Comprimido.txt').st_size
        peso_codificado = str(archivo_codificado)
        texto3 = QTableWidgetItem(peso_codificado)
        self.tableWidget.setItem(0,0,texto3)
        porcentaje = round((archivo_codificado/numero_caracteres),2)
        porcentaje_arc = str(porcentaje)
        texto4 = QTableWidgetItem(porcentaje_arc)
        self.tableWidget.setItem(2,0,texto4)
        self.mostrar_ruta()        

if __name__ =='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
