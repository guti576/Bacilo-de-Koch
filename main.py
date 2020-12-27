from BaciloKoch import calc_functions, plot_functions

# 1.1 Mostramos número de ORFs para cada clase
for clase in calc_functions.get_classes():
    # Calculamos ORFs de la clase
    n_orfs = calc_functions.get_ORFs_in_class(clase)
    print("ORFs en la clase [{}]: {}".format(clase, len(n_orfs)))

# Lo representamos gráficamente
#plot_functions.plot_ORFs_per_class()

# 1.2 Mostramos ORFs que pertenecen a la clase con descripción "Respiration"
for clase in calc_functions.get_classes_by_type("Respiration"):
    # Calculamos ORFs de la clase
    n_orfs = calc_functions.get_ORFs_in_class(clase)
    print("ORFs en la clase Respiration [{}]: {}".format(clase, len(n_orfs)))

# 2.1 Obtenemos número de clases para los patrones indicados
patrones = {'protein': "protein",
            '( |^)[\w*hydro*\w]{13}( |$)': "hydro de 13 caracteres"}

for k,v in patrones.items():
    res = calc_functions.get_classes_by_ORFs_regex(k)
    print("\nEl número de clases con {} en la descripción es de {}".format(v, len(res)))

# 2.2 Calculamos el número promedio de ORFs con los cuales se relacionan
# los ORFs con el patrón indicado en su descripción.
ORFs_relacionados_medio = 0
protein = calc_functions.get_ORFs_by_pattern("protein")
for orf in protein:
    ORFs_relacionados_medio += len(calc_functions.get_related_ORFs_in_ORF(orf))

ORFs_relacionados_medio = ORFs_relacionados_medio/len(protein)
print("\nEl número promedio de ORFs con los cuales se relacionan los ORFs con el patrón 'protein'"
      "es de {}".format(round(ORFs_relacionados_medio, 2)))

##########################################################
# FALTA LA OTRA CONDICION palabra de 13 letras con hydro
##########################################################
# Regex ( |^)[\w*hydro*\w]{13}( |$)

for i in range(2,10):
    clases = calc_functions.dims_greater_than_zero_and_divisible(i)
    print("M={}: {} clases".format(i, len(clases)))