from BaciloKoch import calc_functions, plot_functions

# 1.1 Mostramos número de ORFs para cada clase
plot_functions.plot_exercise_separator("1.1")

for clase in calc_functions.get_classes():
    # Calculamos ORFs de la clase
    n_orfs = calc_functions.get_ORFs_in_class(clase)
    print("ORFs en la clase [{}]: {}".format(clase, len(n_orfs)))

plot_functions.plot_ORFs_per_class()  # Representamos el resultado

# 1.2 Mostramos ORFs que pertenecen a la clase con descripción "Respiration"
plot_functions.plot_exercise_separator("1.2")

for clase in calc_functions.get_classes_by_type("Respiration"):
    # Calculamos ORFs de la clase
    n_orfs = calc_functions.get_ORFs_in_class(clase)
    print("ORFs en la clase Respiration [{}]: {}".format(clase, len(n_orfs)))

# 2.1 Obtenemos número de clases para los patrones indicados
plot_functions.plot_exercise_separator("2.1")

patrones = {'protein': "protein",
            '( |^)[\w*hydro*\w]{13}( |$)': "hydro de 13 caracteres"}

res_dict = {"Número de clases": [], "Promedio ORFs": []}  # Diccionario para almacenar resultados

for k,v in patrones.items():
    res = calc_functions.get_classes_by_ORFs_regex(k)
    res_dict["Número de clases"].append(len(res))
    print("El número de clases con '{}' en la descripción es de {}".format(v, len(res)))


# 2.2 Calculamos el número promedio de ORFs con los cuales se
# relacionan los ORFs con el patrón indicado en su descripción.
plot_functions.plot_exercise_separator("2.2")

for k,v in patrones.items():
    ORFs_relacionados_medio = 0
    related = calc_functions.get_ORFs_by_regex(k)
    for orf in related:
        ORFs_relacionados_medio += len(calc_functions.get_related_ORFs_in_ORF(orf))

    ORFs_relacionados_medio = round(ORFs_relacionados_medio/len(related), 2)
    res_dict["Promedio ORFs"].append(ORFs_relacionados_medio)

    print("El número promedio de ORFs relacionanados con los ORFs con patrón '{}' "
          "es de {}".format(v, ORFs_relacionados_medio))

plot_functions.bar_two_axis(res_dict, list(patrones.values()))

# 3.1 Para cada entero M entre 2 y 9, calculamos el número de clases que tienen
# como mínimo una dimensión mayor estricta (>) que 0 y a la vez múltiple de M.
plot_functions.plot_exercise_separator("3.1")

res_dict = {"M": [], "Num. de clases": []}

for i in range(2,10):
    clases = calc_functions.dims_greater_than_zero_and_divisible(i)
    res_dict["M"].append(i)
    res_dict["Num. de clases"].append(len(clases))
    print("M={}: {} clases".format(i, len(clases)))

plot_functions.plot_bar_chart(res_dict)