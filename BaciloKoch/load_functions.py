import pandas as pd
import re


def parse_dimensions(dim):
    '''
    Dada una dimensión en texto devuelve las cuatro componentes que la forman

    :param dim: dimensión en formato texto
    :return: lista de enteros con los valores de las 4 dimensiones
    '''

    dim = dim.split(",")

    # Convertimos a lista con tipos entero
    for i in range(0, len(dim)):
        dim[i] = int(dim[i])

    return dim


def read_classes(file):
    '''
    Obtiene la información de las clases funcionales de ORF proporcionadas en el fichero
    file y las inserta en dos dataframe para trabajar con ellas posteriormente. Se ha decidido
    emplear esta metodología ya que permite simplificar las tareas de representación y la librería
    pandas es muy utilizada dentro de la comunidad python.

    :param file: fichero con información de las clases
    :return: dataframe con classes
    '''
    with open(file, 'r') as f:

        # Dataframe para las clases
        orf_classes = pd.DataFrame(columns=['class_id', 'dim0', 'dim1',
                                            'dim2', 'dim3', 'description',
                                            'ORFs_in_class'])

        # Leemos el fichero origen
        for line in f:
            line_type = line.split('(')[0]

            if line_type == 'class':
                # Read class id and description
                class_id = re.findall(r'(?<=\[).+?(?=\])', line)[0]
                class_desc = re.findall(r'(?<=\").+?(?=\")', line)[0]

                # Calculamos dimensiones e insertamos en dataframe
                dims = parse_dimensions(class_id)
                orf_classes = orf_classes.append({'class_id': class_id,
                                                  'dim0': dims[0],
                                                  'dim1': dims[1],
                                                  'dim2': dims[2],
                                                  'dim3': dims[3],
                                                  'description': class_desc.strip(),
                                                  'ORFs_in_class': 0},
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


def read_orfs_info(file):
    '''
    Devuelve un diccionario con el detalle de los ORFs relacionados para cada ORF

    :param file: ruta del fichero con el detalle de las relaciones
    :return: diccionario donde "Key" es un ORF y "Value" una lista con los ORFs relaciones
    '''
    with open(file, 'r') as f:

        # Leemos linea por linea
        line = f.readline()
        typo = line.split("(")[0]

        # Diccionario con información de orfs enlazados
        orfs_related = {}

        while typo == "begin":
            model = re.findall(r'(?<=model\().+?(?=\))', line)[0]
            linked_orfs = []

            # Leemos el bloque para ese orf
            while typo != "end":
                line = f.readline()
                typo = line.split("(")[0]

                # Si es información de un orf enlazado la procesamos
                if typo == "tb_to_tb_evalue":
                    orf = re.findall(r'(?<=tb_to_tb_evalue\().+?(?=\,)', line)[0]
                    linked_orfs.append(orf)

            # Creamos entrada en el diccionario
            orfs_related[model] = linked_orfs
            line = f.readline()
            typo = line.split("(")[0]

    return orfs_related