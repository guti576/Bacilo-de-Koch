from BaciloKoch.load_functions import read_functions, read_classes, read_orfs_info
import numpy as np

# Definimos ruta con los datos
data_path = 'data/tb_functions.pl'

# Cargamos funciones y clases
print("Cargando información de clases...")
classes_df = read_classes(data_path)
print("Cargando información de funciones...")
functions_df = read_functions(data_path)

# Definimos rutas de los ficheros orfs
orf_files = ["tb_data_00.txt", "tb_data_01.txt",
             "tb_data_02.txt", "tb_data_03.txt",
             "tb_data_04.txt", "tb_data_05.txt"]

# Creamos columna donde guardamos las listas de los ORFs de la clase
functions_df["ORFs"] = np.empty((len(functions_df), 0)).tolist()

# Enriquecemos las clases con información de los ORFs asociados vinculados
print("Cargando información adicional de ORFs asociados...")
for orf_file in orf_files:
    dict = read_orfs_info("data/orfs/" + orf_file)
    for k,v in dict.items():
        functions_df.loc[functions_df.orf == k, 'ORFs'] = [v]
