from BaciloKoch import calc_functions, plot_functions

# Mostramos número de ORFs para cada clase
for clase in calc_functions.get_classes():
    # Calculamos ORFs de la clase
    n_orfs = calc_functions.get_ORFs_in_class(clase)
    print("ORFs en la clase [{}]: {}".format(clase, len(n_orfs)))

# Lo representamos gráficamente
#plot_functions.plot_ORFs_per_class()

# Mostramos ORFs que pertenecen a la clase con descripción "Respiration"
for clase in calc_functions.get_classes_by_type("Respiration"):
    # Calculamos ORFs de la clase
    n_orfs = calc_functions.get_ORFs_in_class(clase)
    print("ORFs en la clase Respiration [{}]: {}".format(clase, len(n_orfs)))

# Obtenemos clases con algún ORF con "protein" en su desripción
protein = calc_functions.get_classes_by_ORFs_with_pattern("protein")
print("\nEl número de clases con 'protein' en la descripción es de {}".format(len(protein)))

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
