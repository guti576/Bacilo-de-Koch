import pandas as pd
import re


def get_class_and_functions(file):
    '''
    Obtiene la información de las clases funcionales de ORF proporcionadas en el fichero
    file y las inserta en dos dataframe para trabajar con ellas.

    :param file: fichero con información de las clases
    :return: one dataframe with classes and other with functions
    '''

    with open(file, 'r') as f:

        # Dataframe para las clases
        orf_classes = pd.DataFrame(columns=['class_id', 'description'])

        # Dataframe para las funciones
        orf_functions = pd.DataFrame(columns=['orf', 'class_id', 'gen_name', 'description'])

        # Leemos el fichero origen
        for line in f:
            line_type = line.split('(')[0]

            if line_type == 'class':
                # Read class id and description
                class_id = re.findall(r'(?<=\[).+?(?=\])', line)[0]
                class_desc = re.findall(r'(?<=\").+?(?=\")', line)[0]

                # Insertamos en dataframe
                orf_classes = orf_classes.append({'class_id': class_id,
                                                  'description': class_desc.strip()},
                                                 ignore_index=True)
            elif line_type == 'function':
                orf = line.split("(")[1].split(",")[0]
                class_id = re.findall(r'(?<=\[).+?(?=\])', line)[0]
                gen_name = re.findall(r'(?<=\').+?(?=\')', line)[0]
                description = re.findall(r'(?<=\").+?(?=\")', line)[0]

                # Insertamos en dataframe
                orf_functions = orf_functions.append({'orf': orf,
                                                      'class_id': class_id,
                                                      'gen_name': gen_name,
                                                      'description': description.strip()},
                                                     ignore_index=True)
            else:
                pass  # Tipo no identificado

    return orf_classes, orf_functions
