from read_functions import read_classes, read_functions


def get_ORFs_in_class(clase_id, file):
    '''
    Devuelve el número de ORFs que pertenecen a la clase "clase"

    :param clase_id: clase a la que pertenecen los ORFs
    :return:
    '''

    orf_functions = read_functions(file)
    return orf_functions.loc[orf_functions.class_id == clase_id, 'orf'].to_list()


def get_ORFs_in_respiration_class():
    return None

