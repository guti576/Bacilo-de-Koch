import pandas as pd
import re


def read_classes(file):
    '''
    Obtiene la información de las clases funcionales de ORF proporcionadas en el fichero
    file y las inserta en dos dataframe para trabajar con ellas posteriormente. Se ha decidido
    emplear esta metodología, pese a que es más costosa en tiempo, ya que permite simplificar las
    tareas de representación y la librería pandas es muy utilizada dentro de la comunidad python.

    :param file: fichero con información de las clases
    :return: dataframe con classes
    '''
    with open(file, 'r') as f:

        # Dataframe para las clases
        orf_classes = pd.DataFrame(columns=['class_id', 'description'])

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
    return orf_classes


def read_functions(file):
    '''
    Obtiene la información de las clases funcionales de ORF proporcionadas en el fichero
    file y las inserta en dos dataframe para trabajar con ellas posteriormente. Se ha decidido
    emplear esta metodología, pese a que es más costosa en tiempo, ya que permite simplificar las
    tareas de representación y la librería pandas es muy utilizada dentro de la comunidad python.

    :param file: fichero con información de las clases
    :return: dataframe con funciones orf
    '''
    with open(file, 'r') as f:

        # Dataframe para las funciones
        orf_functions = pd.DataFrame(columns=['orf', 'class_id', 'gen_name', 'description'])

        # Leemos el fichero origen
        for line in f:
            line_type = line.split('(')[0]

            if line_type == 'function':
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

    return orf_functions
