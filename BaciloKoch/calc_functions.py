from BaciloKoch import functions_df, classes_df


def get_classes():
    '''
    Devuelve todas las clase funcionales de ORFs

    :return: lista con todas las clases existentes
    '''

    return classes_df.class_id.unique()


def get_classes_by_type(description):
    '''
    Obtiene todas las clases funcionales de ORFs con una descripción concreta
    :return: lista con las clases coincidientes
    '''

    return classes_df.loc[classes_df.description==description, 'class_id'].unique()


def get_ORFs_in_class(clase_id):
    '''
    Devuelve el número de ORFs que pertenecen a la clase "clase"

    :param clase_id: clase a la que pertenecen los ORFs
    :return:
    '''

    # Devolvemos lista con orfs que pertenecen a la clase
    return functions_df.loc[functions_df.class_id == clase_id, 'orf'].to_list()
