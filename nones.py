import os
import shutil

carpetaArchivos = '/Users/ALEJANDRO/Desktop/remplazarNombre/DocumentosPDF_Pares'
# print(carpetaArchivos)
# carpeta = os.listdir(carpetaArchivos)

nueva_ruta = os.path.join(carpetaArchivos, "ordenArchivos")
# print(nueva_ruta)

ruta_par = os.path.join(nueva_ruta, "pares")
# print(ruta_par)

ruta_impar = os.path.join(nueva_ruta, "impares")
# print(ruta_impar)

# Crea la carpeta 'ordenArchivos' si no existe
if not os.path.exists(nueva_ruta) and not os.path.exists(ruta_par) and not os.path.exists(ruta_impar):
    os.mkdir(nueva_ruta)
    os.mkdir(ruta_par)
    os.mkdir(ruta_impar)

if __name__ == '__main__':
    for fileName in os.listdir(carpetaArchivos):
        # la siguiente linea se utiliza para dividir esa ruta en dos partes: el nombre del archivo y su extensión.
        nombre, extension = os.path.splitext(fileName)

        if extension == ".pdf":
            base_nombre = os.path.basename(nombre)
            if base_nombre.isdigit():
                numero = int(base_nombre) * 11

                # nuevo_nombre = f"{numero}.pdf"
                # nuevo_nombre = str(numero) + ".pdf"
                nuevo_nombre = f"{numero}.pdf"
                # print(nuevo_nombre)

                ruta_original = os.path.join(carpetaArchivos, fileName)
                ruta_destino = os.path.join(nueva_ruta, nuevo_nombre)
                ruta_destino_par = os.path.join(ruta_par, nuevo_nombre)
                ruta_destino_impar = os.path.join(ruta_impar, nuevo_nombre)

                if numero % 2 == 0:
                    shutil.copy2(ruta_original, ruta_destino_par)

                elif numero % 2 != 0:
                    shutil.copy2(ruta_original, ruta_destino_impar)

                print(f"Archivo copiado: {fileName} -> {nuevo_nombre}")

                # Para renombrar un archivo hay que colocar la ruta completa del archivo / carpeta ejemplo asi: '/Users/ALEJANDRO/Desktop/DocumentosPDF1.pdf' y no solo especificar el archivo '1.pdf'  # os.rename(vieja_ruta, nueva_ruta)
