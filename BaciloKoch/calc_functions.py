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
    Devuelve el número de ORFs que pertenecen a la clase "clase_id"

    :param clase_id: clase a la que pertenecen los ORFs
    :return: lista de ORFs que pertenecen a la clase
    '''

    # Devolvemos lista con orfs que pertenecen a la clase
    return functions_df.loc[functions_df.class_id == clase_id, 'orf'].to_list()


def get_ORFs_by_pattern(pattern):
    return functions_df.loc[functions_df.description.str.contains(pattern), 'orf'].to_list()


def get_related_ORFs_in_ORF(orf):
    try:
        related_ORFs = functions_df.loc[functions_df.orf == orf, 'ORFs'].to_list()[0]
    except:
        related_ORFs = []

    return related_ORFs


def get_classes_by_ORFs_with_pattern(pattern):
    return functions_df.loc[functions_df.description.str.contains(pattern), 'class_id'].to_list()

