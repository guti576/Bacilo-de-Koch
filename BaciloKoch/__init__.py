from BaciloKoch.load_functions import read_functions, read_classes, read_orfs_info


# Definimos ruta con los datos
data_path = 'data/tb_functions.pl'

# Cargamos funciones y clases
classes_df = read_classes(data_path)
functions_df = read_functions(data_path)

# Definimos rutas de los ficheros orfs
orf_files = ["tb_data_00.txt", "tb_data_01.txt",
             "tb_data_02.txt", "tb_data_03.txt",
             "tb_data_04.txt", "tb_data_05.txt"]

for orf_file in orf_files:
    read_orfs_info("data/orfs/" + orf_file)
