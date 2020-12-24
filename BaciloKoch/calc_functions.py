from BaciloKoch.read_functions import read_functions


def get_ORFs_in_class(clase_id):
    '''
    Devuelve el número de ORFs que pertenecen a la clase "clase"

    :param clase_id: clase a la que pertenecen los ORFs
    :return:
    '''

    # Cargamos el dataframe creado al cargar el paquete
    from BaciloKoch import functions_df

    # Devolvemos lista con orfs que pertenecen a la clase
    return functions_df.loc[functions_df.class_id == clase_id, 'orf'].to_list()


def get_ORFs_in_respiration_class():
    return None

