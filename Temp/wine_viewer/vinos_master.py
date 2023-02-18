from vino_conexion import DataConexion
import vino_conexion 
import vino_funciones
import argparse

""" Function to coordinate all the options and functions with DB """
parser = argparse.ArgumentParser(description='Give the database information.')
parser.add_argument('hostname', help='the hostname of the database.')
parser.add_argument('port', type=int, help='the port of the database.')
parser.add_argument('db_username', help='the username of the database.')
parser.add_argument('db_password', help='the database password.')
parser.add_argument('db_name', help='the database name.')

args = parser.parse_args()


def menuPrincipal():
    """ Main coordinate function """
    conectar= DataConexion(args.hostname, args.port, args.db_username,
                            args.db_password, args.db_name)
    bandera=True
    while bandera==True:
        print("#### MENU PRINCIPAL#####")
        print("1.-Listar Productos")
        print("2.-Registrar Productos")
        print("3.-Actualizar Productos")
        print("4.-Borrar Productos")
        print("5.-Salir")
        try:
            opc = int(input("Selecciona una Opción:"))
        except:
            continue
        if opc > 0 and opc < 6:
            if opc == 1:
                try:
                    productos = conectar.listaProductos()
                    if len(productos) > 0:
                        vino_funciones.listar(productos)
                    else:
                        print("No hay productos todavía.")
                except:
                    print("No se pudo ejecutar la consulta.")
            elif opc == 2:
                datos_producto = vino_funciones.datosProductos()
                print(f"Estos son los productos a insertar {datos_producto}.")
                for pro in datos_producto:
                    try:
                        conectar.registrarProductos(pro)
                    except:
                        print("No se pudo insertar productos.")
            elif opc == 3:
                    productos = conectar.listaProductos()
                    try:
                        if len(productos) > 0:
                            productAct = vino_funciones.datosProductosActualizar(productos)
                            print(f"Productos a actualizar: {productAct}.")
                            for prod in productAct:
                                conectar.actualizarProductos(prod)
                        else:
                            print("No hay productos.")                        
                    except:
                        print("Error en master actualizar.")                    
            elif opc == 4:
                try:
                    productos = conectar.listaProductos()
                    if len(productos) > 0:
                        dato_eliminar = vino_funciones.registroEliminar(productos)
                        print(f"Dato a Eliminar {dato_eliminar}")
                        if not(dato_eliminar == ""): 
                            conectar.eliminarProducto(dato_eliminar)
                        else:
                            print("Codigo del producto no encontrado o vacio ....")
                    else:
                        print("No hay Registros Para Eliminar.")                   
                except:
                    print("No se ha podido ejecutar la orden.")                                
            elif opc==5:
                print("Hasta luego.")
                bandera=False
        else:
            print("Opción no valida selecciona una opcion del 1-6")
        
if __name__=='__main__':
    menuPrincipal()
                 