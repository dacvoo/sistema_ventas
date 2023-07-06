from persona import Persona
from producto import Producto
from factura import Factura
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from factura_detalle import FacturaDetalle
from cuentas_de_inicio import Cuentas
from tkinter import Tk,Label,Button, Entry
import tkinter as tk

ciro=Cuentas("toshiby","123")
david=Cuentas("naira","111")
valdez=Cuentas("militar","222")
curro=Cuentas("johan","333")
cuentas:Cuentas=[ciro,david,valdez,curro]

"""Crear CRUD de la clase Persona"""

data_personas:list=[{"dni":"61321351",
                    "nombres":"Naira Alture",
                    "apellidos":"Edgar David",
                    "direccion":"jr tupac yupanqui 590 juliaca",
                    "telefono":"997124032"},
                    {"dni":"71849102",
                    "nombres":"Ciro ",
                    "apellidos":"machicado velazques",
                    "direccion":"salida cusco",
                    "telefono":"99999999"},
                    {"dni":"74059496",
                    "nombres":"johan americo",
                    "apellidos":"curro caira",
                    "direccion":"Jr. Jose Galvez",
                    "telefono":"9888888"},
                    {"dni":"75902902",
                    "nombres":"midwar michael",
                    "apellidos":"valdez yujra",
                    "direccion":"Salida Puno",
                    "telefono":"20022145"}]

lista_de_personas:Persona=[]
def cargar_data_personas():
    for data in data_personas:
        lista_de_personas.append(Persona(data["dni"],
                                         data["nombres"],
                                         data["apellidos"],
                                         data["direccion"],
                                         data["telefono"]))
def registrar_persona():
    v_dni:str= input("Ingrese el DNI de la persona: ")
    v_nombres:str= input("Ingrese nombres de la persona: ")
    v_apellidos:str= input("Ingrese apellidos de la persona: ")
    v_direccion:str= input("Ingrese direccion de la persona: ")
    v_telefono:str= input("Ingrese telefono de la persona: ")
    persona:Persona= Persona(v_dni,v_nombres,v_apellidos,v_direccion,v_telefono)
    lista_de_personas.append(persona)
    listar_personas()

def listar_personas():
    for elemento in lista_de_personas:
        print(elemento.convertir_a_string())

def bucar_persona():
    v_dni:str = input("Ingrese el DNI de la persona: ")
    for elemento in lista_de_personas:
        if elemento.dni == v_dni:
            print(elemento.convertir_a_string())
            return elemento
            

def editar_persona():
    listar_personas()  
    v_dni:str =input("Ingrese el DNI de la persona: ")
    for persona in lista_de_personas:
        if persona.dni == v_dni:
            persona.nombres=input("Ingrese nombres de la persona: ")
            persona.apellidos=input("Ingrese apellidos de la persona: ")
            persona.direccion=input("Ingrese direccion de la persona: ")
            persona.telefono=input("Ingrese telefono de la persona: ")
    listar_personas()
    return lista_de_personas

def eliminar_persona():
    dni:str =input("Ingrese el DNI de la persona: ")
    for index, persona in enumerate(lista_de_personas):
        if persona.dni == dni:
            lista_de_personas.pop(index)
    return lista_de_personas


"""Crear CRUD de la clase Producto"""

data_productos:list=[{"codigo":"001",
                    "nombre":"Pancito",
                    "precio":1.50},
                    {"codigo":"002",
                    "nombre":"Agua Cielo",
                    "precio":1.00},
                    {"codigo":"003",
                    "nombre":"Paneton",
                    "precio":20.00}
                    ]

lista_de_productos:Producto=[]
def cargar_data_productos():
    for data in data_productos:
        lista_de_productos.append(Producto(data["codigo"],
                                         data["nombre"],
                                         data["precio"]))
def registrar_producto():
    codigo:str= input("Ingrese el codigo del producto: ")
    nombre:str= input("Ingrese nombre del producto: ")
    precio:float= float(input("Ingrese precio del producto: "))

    producto:Producto= Producto(codigo,nombre,precio)
    lista_de_productos.append(producto)
    listar_productos()

def listar_productos():
    for elemento in lista_de_productos:
        print(elemento.convertir_a_string())

def bucar_producto():
    codigo:str = input("Ingrese el codigo del producto: ")
    for elemento in lista_de_productos:
        if elemento.codigo == codigo:
            print(elemento.convertir_a_string())
            return elemento
            

def editar_producto():
    listar_productos()  
    codigo:str =input("Ingrese el codigo del producto: ")
    for producto in lista_de_productos:
        if producto.codigo == codigo:
            producto.nombre=input("Ingrese nombre del producto: ")
            producto.precio=float(input("Ingrese precio del producto: "))
            break
    listar_productos()
    return lista_de_productos

def eliminar_producto():
    codigo:str =input("Ingrese codigo del producto: ")
    for index, producto in enumerate(lista_de_productos):
        if producto.codigo == codigo:
            lista_de_productos.pop(index)
            break
    return lista_de_productos

facturas:Factura=[]
factura_detalles:FacturaDetalle=[]

def agregar_productos_a_la_factura():
    producto:Producto=bucar_producto()
    cantidad:float=float(input(" Ingrese la cantidad de productos a vender: "))
    factura_detalles.append(FacturaDetalle(len(factura_detalles)+1,producto.codigo,producto.nombre,cantidad,producto.precio))

def generar_pdf_factura(factura):

    total_factura = 0
    for detalle in factura.detalle:
        total_factura += detalle.total

    archivo_pdf = f"factura_{factura.numero}.pdf"
    c = canvas.Canvas(archivo_pdf, pagesize=letter)

    c.drawString(72, 750, "Factura")
    c.drawString(72, 730, f"Cliente: {factura.cliente.nombres} {factura.cliente.apellidos}")
    c.drawString(72, 710, "Detalles:")

    y_position = 690
    for detalle in factura.detalle:
        c.drawString(100, y_position, f"{detalle.cantidad} {detalle.nombre} - {detalle.total:.2f}")
        y_position -= 20

    c.drawString(72, y_position, f"Total: {total_factura:.2f}")

    c.save()


    print(f"Factura generada exitosamente: {archivo_pdf}")

def registrar_factura():
    cliente = bucar_persona()
    continuar_agregando_producto = True
    while continuar_agregando_producto:
        opcion = input("1 para agregar producto, 2 para guardar factura: ")
        if opcion == "1":
            agregar_productos_a_la_factura()
        elif opcion == "2":
            continuar_agregando_producto = False
        else:
            print("Opción inválida. Intente nuevamente.")

    total_factura = 0
    for factura_detalle in factura_detalles:
        total_factura += factura_detalle.total

    factura = Factura(len(facturas) + 1, cliente, total_factura, factura_detalles)
    facturas.append(factura)


    generar_pdf_factura(factura)

    return facturas
def listar_facturas():
    for factura in facturas:
        print(factura.convertir_a_string())
        
def buscar_factura():
    numero:int=int(input("Ingrese el numero de la factura: "))
    for factura in facturas:
        if factura.numero==numero:
            print(factura.convertir_a_string())
            print("==========================================================")
            for detalle in factura.detalle:
                print("--------------------------------------------------------")
                print(detalle.convertir_a_string())
            return factura

def menu_principal():
    print("============= MENU===========")
    print("1: Para registrar persona")
    print("2: Para listar persona")
    print("3: Para bucar persona")
    print("4: Para editar persona")
    print("5: Para eliminar persona")

    print("6: Para registrar producto")
    print("7: Para listar producto")
    print("8: Para bucar producto")
    print("9: Para editar producto")
    print("10: Para eliminar producto")

    print("11: Para registrar factura")
    print("12: Para listar factura")
    print("13: Para buscar factura")


    print("30: Para salir  del sistema")
    return True
def menu():
    continuar_programa:bool=True
    while continuar_programa:
        menu_principal()
        opcion:str=input("Ingrese la opcion: ")
        match opcion:
            case "1":
                registrar_persona()
            case "2":
                listar_personas()
            case "3":
                bucar_persona()
            case "4":
                editar_persona()
            case "5":
                eliminar_persona()
            case "6":
                registrar_producto()
            case "7":
                listar_productos()
            case "8":
                bucar_producto()
            case "9":
                editar_producto()
            case "10":
                eliminar_producto()
            case "11":
                registrar_factura()
            case "12":
                listar_facturas()
            case "13":
                buscar_factura()

            case "30":
                print("Saliendo del programa")
                continuar_programa= False

def iniciar_sesion():
    in_user=str(text1.get())
    in_password=str(text2.get())
    for elemento in cuentas:
        if in_user==elemento.user_name and in_password==elemento.contraseña:
            menu()
            
ventana=Tk()
ventana.title("Tienda tu amigble vecino")
ventana.geometry("600x300")

lbl=Label(ventana,text="Bienvenido Ingrese su cuenta",bg="white")
lbl.place(x=170,y=30,width=220,height=30)

lbl1=Label(ventana, text="Ingrese ususario", bg="grey" ,fg="white")
lbl1.place(x=10,y=80,width=130,height=25)
text1=Entry(ventana,bg="white")
text1.place(x=150,y=80,width=130,height=25)

lbl2=Label(ventana, text="Ingrese contraseña", bg="black" ,fg="white")
lbl2.place(x=10,y=110,width=130,height=25)
text2=Entry(ventana,bg="white")
text2.place(x=150,y=110,width=130,height=25)

butt=Button(ventana, text="Iniciar sesion",command=iniciar_sesion)
butt.place(x=300,y=110,width=130,height=25)

def main():
    cargar_data_personas()
    cargar_data_productos()
    iniciar_sesion()
    return True

if __name__=='__main__':
    main()


ventana.mainloop()