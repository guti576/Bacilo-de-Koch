from BaciloKoch import functions_df, classes_df
import warnings
warnings.simplefilter("ignore", UserWarning)


def get_classes():
    '''
    Devuelve todas las clase funcionales de ORFs

    :return: lista con todas las clases existentes
    '''

    return classes_df.class_id.unique()


def get_classes_by_type(description):
    '''
    Obtiene todas las clases funcionales de ORFs con una descripción concreta

    :param: descripción que tiene que cumplir la clase
    :return: lista con las clases coincidientes
    '''

    return classes_df.loc[classes_df.description==description, 'class_id'].unique()


def get_ORFs_in_class(clase_id):
    '''
    Devuelve el número de ORFs que pertenecen a la clase "clase_id"

    :param clase_id: clase a la que pertenecen los ORFs
    :return: lista de ORFs que pertenecen a la clase
    '''

    # Calculamos ORFs en la clase
    orfs_in_class = functions_df.loc[functions_df.class_id == clase_id, 'orf'].to_list()

    # Guardamos valor en Dataframe para poder representarlo
    classes_df.loc[classes_df.class_id == clase_id,
                   'ORFs_in_class'] = len(orfs_in_class)

    # Devolvemos lista con orfs que pertenecen a la clase
    return orfs_in_class


def get_related_ORFs_in_ORF(orf):
    '''
    Obtiene el listad de ORFs relacionados con un ORF dado

    :param orf: ORF del que queremos obtener los relacinados
    :return: lista con ORFs relacionados
    '''
    try:
        related_ORFs = functions_df.loc[functions_df.orf == orf, 'ORFs'].to_list()[0]
    except:
        related_ORFs = []

    return related_ORFs


def get_classes_by_ORFs_regex(pattern):
    '''
    Obtiene las clases que cumplen el patrón 'pattern' en su descripción.

    :param pattern: patrón que tienen que cumplir las clases
    :return: listado de clases que cumplen el patrón dado
    '''
    return functions_df.loc[functions_df.description.str.contains(pattern), 'class_id'].to_list()


def get_ORFs_by_regex(pattern):
    '''
    Obtiene los ORFs que cumplen el patrón 'pattern' en su descripción.

    :param pattern: patrón que tienen que cumplir el ORF
    :return: listado de ORFs que cumplen el patrón dado
    '''
    return functions_df.loc[functions_df.description.str.contains(pattern), 'orf'].to_list()


def dims_greater_than_zero_and_divisible(m):
    '''
    Obtiene las clases con alguna dimensión mayor que cero y que además
    es divisible por el valor m indicado como parámetro de la función.

    :param m: valor por el que tiene que ser divisible la dimensión
    :return: listado de clases que cumplen los criterios definidos
    '''

    res = classes_df.loc[((classes_df.dim0 > 0) & (classes_df.dim0 % m == 0)) |
                         ((classes_df.dim1 > 0) & (classes_df.dim1 % m == 0)) |
                         ((classes_df.dim2 > 0) & (classes_df.dim2 % m == 0)) |
                         ((classes_df.dim3 > 0) & (classes_df.dim3 % m == 0)), 'class_id'].to_list()
    return res