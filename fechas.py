# This is a sample Python script.
import os
import shutil

# Press Shif + F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# años
anos = ['2019', '2020', '2021', '2022', '2023']
meses = ['ENERO', 'FEBRERO', 'MARZO', 'ABRIL', 'MAYO', 'JUNIO', 'JULIO', 'AGOSTO', 'SEPTIEMBRE', 'OCTUBRE',
         'NOVIEMBRE', 'DICIEMBRE']

# La ruta en Windows se coloca con las diagonales normales para que no genere un problema de sintaxis con esta caracter "\".
carpetaArchivos = '/Users/ALEJANDRO/Desktop/remplazarNombre/DocumentosPDF_Pares'

nueva_ruta = os.path.join(carpetaArchivos, "ordenArchivos")


# print(nueva_ruta)


def cambiarNombresArchivos():
    for fileName in os.listdir(carpetaArchivos):
        # la siguiente linea se utiliza para dividir esa ruta en dos partes: el nombre del archivo y su extensión.
        nombre, extencion = os.path.splitext(fileName)

        if extencion in [".pdf"]:
            base_nombre = os.path.basename(nombre)

            mes = ''
            # nuevo_nombre = f"{numero}0.pdf"
            if base_nombre.split('-')[1] == '01':
                mes = 'ENERO'

            if base_nombre.split('-')[1] == '02':
                mes = 'FEBRERO'

            if base_nombre.split('-')[1] == '03':
                mes = 'MARZO'

            if base_nombre.split('-')[1] == '04':
                mes = 'ABRIL'

            if base_nombre.split('-')[1] == '05':
                mes = 'MAYO'

            if base_nombre.split('-')[1] == '06':
                mes = 'JUNIO'

            if base_nombre.split('-')[1] == '07':
                mes = 'JULIO'

            if base_nombre.split('-')[1] == '08':
                mes = 'AGOSTO'

            if base_nombre.split('-')[1] == '09':
                mes = 'SEPTIEMBRE'

            if base_nombre.split('-')[1] == '10':
                mes = 'OCTUBRE'

            if base_nombre.split('-')[1] == '11':
                mes = 'NOVIEMBRE'

            if base_nombre.split('-')[1] == '12':
                mes = 'DICIEMBRE'

            # esta condicion organiza por el año que tenga los filename
            nuevo_nombre = base_nombre.split('-')[0] + "\\" + mes + "\\" + base_nombre + ".pdf"

            ruta_original = os.path.join(carpetaArchivos, fileName)
            ruta_destino = os.path.join(nueva_ruta, nuevo_nombre)

            moverArchivos(ruta_original, ruta_destino)

            print(f"Archivo copiado: {fileName} -> {nuevo_nombre}")


def crearCarpetas():
    for year in anos:
        rutaYear = os.path.join(nueva_ruta, year)
        # print(year)

        # Crea la carpeta 'ordenArchivos' si no existe
        if not os.path.exists(nueva_ruta):
            os.mkdir(nueva_ruta)

        if not os.path.exists(rutaYear):
            os.mkdir(rutaYear)

        for mes in meses:
            rutaMeses = os.path.join(rutaYear, mes)
            if not os.path.exists(rutaMeses):
                os.mkdir(rutaMeses)


def moverArchivos(origen, destino):
    shutil.copy2(origen, destino)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    crearCarpetas()
    cambiarNombresArchivos()
