from BaciloKoch.read_functions import read_functions, read_classes


# Definimos ruta con los datos
data_path = 'data/tb_functions.pl'

# Cargamos funciones y clases
classes_df = read_classes(data_path)
functions_df = read_functions(data_path)
