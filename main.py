from PyPDF2 import PdfMerger
import os

# Especifica las rutas de entrada y salida
input_folder = r'~/Downloads/'
output_file = os.path.expanduser(input_folder + 'combined.pdf')

def merge_pdfs(input_path, output_path):
    merger = PdfMerger()

    expanded_input_path = os.path.expanduser(input_path)

    for file in os.listdir(expanded_input_path):
        if file.endswith(".pdf"):
            file_path = os.path.join(expanded_input_path, file)
            merger.append(file_path)

    # Guarda el archivo combinado en la ruta de salida
    merger.write(output_path)

merge_pdfs(input_folder, output_file)
print('Archivos combinados con éxito')