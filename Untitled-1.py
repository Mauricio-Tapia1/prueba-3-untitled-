CantidadPasajes=[]
PrecioAsientoComun=60000
PrecioEspacioPiernas=80000
PrecioNoReclina=50000
CantComun=0
CantPiernas=0
CantNoReclina=0
TipoAsientos=("1)Asiento Comun","2)Espacio para piernas","3)No reclina")
UbicacionesDisponibles=("1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "10")


def CantidadAsientos():
    op=CantidadPasajes=int(input("Selecciona una cantidad de pasajes(maximo:2): "))
    if op==1 or 2:
        print(TipoAsientos)
        SeleccionTipo=TipoAsientos
        SeleccionTipo=int(input("Seleccione Tipo de asientos:  "))
        if SeleccionTipo==1:
            CantComun=+1
        
        elif SeleccionTipo==2:
            CantPiernas=+1
        
        elif SeleccionTipo==3:
            CantNoReclina=+1
        print("Ubicaciones disponibles")
        print(UbicacionesDisponibles)
        SeleccionUbicacion=int(input("Seleccione una ubicacion"))
        print("--------------------------------------------")
        print(f"Cantidad de pasajes")
        print(CantidadPasajes)
        print(f"Tipo De asiento")
        print(SeleccionTipo)
        print("Ubicaciones seleccionadas")
        print(SeleccionUbicacion)




def UbicacionDisponible():
    print(UbicacionesDisponibles)



        
        

    

        
        
def GananciasTotales():
    SeleccionTip=(CantNoReclina*PrecioNoReclina)+(CantComun*PrecioAsientoComun)+(CantPiernas*PrecioEspacioPiernas)
    print(SeleccionTip)


    
















print("""
      Menu linea aerea Flash
      (1)Comprar pasajes
      (2)Mostrar ubicaciones disponibles
      (3)Ver listado de pasajeros
      (4)Buscar pasajero
      (5)Reasignar asiento
      (6)Mostrar ganancias totales
      (7)Salir
      """)

while True:
    opcion = int(input("Seleccione una opcion:" ))
    
    if opcion==1:
        CantidadAsientos()
        
    if opcion==2:
        UbicacionDisponible()
    
    if opcion==3:
        ListadoPasajero()

    if opcion==6:
        GananciasTotales()