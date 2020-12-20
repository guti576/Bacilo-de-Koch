import pandas as pd

def get_class_and_functions(file):
    '''
    Obtiene la información de las clases funcionales de ORF proporcionadas en el fichero
    file y las inserta en dos dataframe para trabajar con ellas.

    :param file: fichero con información de las clases
    :return:
    '''

    with open(file, 'r') as f:

        # Dataframe para las clases
        orf_classes = pd.DataFrame(columns=['class_id', 'description'])

        # Dataframe para las funciones
        orf_functions = pd.DataFrame(columns=['orf', 'class_id', 'gen_name', 'description'])

        # Leemos el fichero origen
        for line in f:
            line = line.split('(')

            if line[0] == 'class':
                # Read id
                pass

                # Read description
                pass
