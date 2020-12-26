from BaciloKoch import calc_functions

# Mostramos número de ORFs para cada clase
for clase in calc_functions.get_classes():
    # Calculamos ORFs de la clase
    n_orfs = calc_functions.get_ORFs_in_class(clase)
    print("ORFs en la clase [{}]: {}\n".format(clase, len(n_orfs)))

# Mostramos ORFs que pertenecen a la clase con descripción "Respiration"
for clase in calc_functions.get_classes_by_type("Respiration"):
    # Calculamos ORFs de la clase
    n_orfs = calc_functions.get_ORFs_in_class(clase)
    print("ORFs en la clase Respiration [{}]: {}\n".format(clase, len(n_orfs)))

#