from BaciloKoch import calc_functions, plot_functions

# 1.1 Mostramos número de ORFs para cada clase
for clase in calc_functions.get_classes():
    # Calculamos ORFs de la clase
    n_orfs = calc_functions.get_ORFs_in_class(clase)
    print("ORFs en la clase [{}]: {}".format(clase, len(n_orfs)))

plot_functions.plot_ORFs_per_class("show")  # Representamos el resultado

# 1.2 Mostramos ORFs que pertenecen a la clase con descripción "Respiration"
for clase in calc_functions.get_classes_by_type("Respiration"):
    # Calculamos ORFs de la clase
    n_orfs = calc_functions.get_ORFs_in_class(clase)
    print("ORFs en la clase Respiration [{}]: {}".format(clase, len(n_orfs)))

# 2.1 Obtenemos número de clases para los patrones indicados
patrones = {'protein': "protein",
            '( |^)[\w*hydro*\w]{13}( |$)': "hydro de 13 caracteres"}

res_dict_class = {}  # Diccionario para almacenar valores a representar

for k,v in patrones.items():
    res = calc_functions.get_classes_by_ORFs_regex(k)
    res_dict_class[v] = len(res)
    print("\nEl número de clases con {} en la descripción es de {}".format(v, len(res)))

#plot_functions.plot_pie_from_dict(res_dict)  # Representamos el resultado

# 2.2 Calculamos el número promedio de ORFs con los cuales se relacionan
# los ORFs con el patrón indicado en su descripción.

res_dict_orf = {}  # Diccionario para almacenar valores a representar

for k,v in patrones.items():
    ORFs_relacionados_medio = 0
    related = calc_functions.get_ORFs_by_regex(k)
    for orf in related:
        ORFs_relacionados_medio += len(calc_functions.get_related_ORFs_in_ORF(orf))

    ORFs_relacionados_medio = round(ORFs_relacionados_medio/len(related), 2)
    res_dict_orf[v] = ORFs_relacionados_medio
    print("\nEl número promedio de ORFs relacionanados con los ORFs con patrón v"
          "es de {}".format(ORFs_relacionados_medio))

plot_functions.bar_two_axis(res_dict_class, res_dict_orf)
# 3.1 Para cada entero M entre 2 y 9, calculamos el número de clases que tienen
# como mínimo una dimensión mayor estricta (>) que 0 y a la vez múltiple de M.
for i in range(2,10):
    clases = calc_functions.dims_greater_than_zero_and_divisible(i)
    print("M={}: {} clases".format(i, len(clases)))