from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

#variable de operador, calculadora
operador = ''
#precios en dolares
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


# funciones:

def click_boton_cal(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)
    
def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''

def revisar_check():
    # revisar si el check ha sido activado.
    x = 0 #contar indices
    for c in cuadros_comidas:
        if variables_comidas[x].get() == 1:
            cuadros_comidas[x].config(state = NORMAL)
            if cuadros_comidas[x].get() == '0':
                cuadros_comidas[x].delete(0, END)
            cuadros_comidas[x].focus()
        else:
            cuadros_comidas[x].config(state = DISABLED)
            texto_comida[x].set('0')
        x += 1
        
    x = 0 #contar indices
    for b in cuadros_bebidas:
        if variables_bebidas[x].get() == 1:
            cuadros_bebidas[x].config(state = NORMAL)
            if cuadros_bebidas[x].get() == '0':
                cuadros_bebidas[x].delete(0, END)
            cuadros_bebidas[x].focus()
        else:
            cuadros_bebidas[x].config(state = DISABLED)
            texto_bebida[x].set('0')
        x += 1
        
    x = 0 #contar indices
    for p in cuadros_postres:
        if variables_postres[x].get() == 1:
            cuadros_postres[x].config(state = NORMAL)
            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0, END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state = DISABLED)
            texto_postre[x].set('0')
        x += 1

def total():
    #calcula total, impuestos y sub-total
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1
    

    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1
    
    
    sub_total_postre = 0
    p = 0
    for cantidad in texto_postre:
        sub_total_postre = sub_total_postre + (float(cantidad.get()) * precios_postres[p])
        p += 1
    
    # calculo de sub-total, impuestos y el total
    sub_total = sub_total_comida + sub_total_bebida + sub_total_postre
    impuestos = sub_total * 0.1 # porcentaje de impuestos supuestos a cambios
    total = sub_total + impuestos
    
    # muestra el resultado, dando un redondeo con 2 numeros decimales
    var_costo_comida.set(f'$ {round(sub_total_comida, 2)}')
    var_costo_bebida.set(f'$ {round(sub_total_bebida, 2)}')
    var_costo_postre.set(f'$ {round(sub_total_postre, 2)}')
    var_subtotal.set(f'$ {round(sub_total, 2)}')
    var_impuesto.set(f'$ {round(impuestos, 2)}')
    var_total.set(f'$ {round(total, 2)}')

def recibo():
    # generamos el recibo, considerando que el numero legal de ticket esta siendo generado aleatoriamente por conveniencia
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    fecha = datetime.datetime.now() # fecha y hora actual a generar
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}' #imprimiendo en el formato deseado
    texto_recibo.insert(END, f'Datos:\t{num_recibo}\t  {fecha_recibo}\n')
    texto_recibo.insert(END, f'*'*40 + '\n')
    texto_recibo.insert(END, f'Items\t\tCant.\tCosto Items\n')
    texto_recibo.insert(END, f'-'*50 + '\n')
    
    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t$ {int(comida.get()) * precios_comida[x]}\n')
        x += 1
        
    x = 0
    for bebida in texto_bebida:
        if bebida.get() != '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t$ {int(bebida.get()) * precios_bebida[x]}\n')
        x += 1
        
    x = 0
    for postre in texto_postre:
        if postre.get() != '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postre.get()}\t$ {int(postre.get()) * precios_postres[x]}\n')
        x += 1
        
    texto_recibo.insert(END, f'-'*40 + '\n')
    texto_recibo.insert(END, f'Costo de COMIDA: \t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'Costo de BEBIDA: \t\t\t{var_costo_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo de POSTRES: \t\t\t{var_costo_postre.get()}\n')
    
    texto_recibo.insert(END, f'-'*40 + '\n')
    texto_recibo.insert(END, f'SUB-TOTAL: \t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'IMPUESTOS: \t\t\t{var_impuesto.get()}\n')
    texto_recibo.insert(END, f'TOTAL: \t\t\t{var_total.get()}\n')
    texto_recibo.insert(END, f'*'*40 + '\n')
    texto_recibo.insert(END, 'LO ESPERAMOS PRONTO!')


def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion', 'Su recibo ha sido guardado')
    
def resetear():
    texto_recibo.delete(0.1, END)

    for texto in texto_comida:
        texto.set('0')
    
    for texto in texto_bebida:
        texto.set('0')
        
    for texto in texto_postre:
        texto.set('0')
        
        
    for cuadro in cuadros_comidas:
        cuadro.config(state = DISABLED)
    
    for cuadro in cuadros_bebidas:
        cuadro.config(state = DISABLED)
        
    for cuadro in cuadros_postres:
        cuadro.config(state = DISABLED)
    
    
    for v in variables_comidas:
        v.set('0')
    
    for v in variables_bebidas:
        v.set('0')
        
    for v in variables_postres:
        v.set('0')
    
    var_costo_comida.set('')
    var_costo_bebida.set('')
    var_costo_postre.set('')
    var_subtotal.set('')
    var_impuesto.set('')
    var_total.set('')
    
#iniciar tkinter
aplicacion = Tk()


#size de la ventana
aplicacion.geometry('1020x650+0+0')

#evitar maximizar
aplicacion.resizable(0,0)

#titulo de la ventana
aplicacion.title('MI RESTAURANTE - SISTEMA DE FACTURACION')

#color de fondo
aplicacion.config(bg='#FFE3A8')


#panel superior
panel_superior = Frame(aplicacion, bd = 2, relief = FLAT)
panel_superior.pack(side = TOP)

#etiqueta titulo
etiqueta_titulo = Label(panel_superior, text = 'SISTEMA DE FACTURACION', fg = '#703116',
                        font = ('Times New Roman', 48), bg = '#FFE3A8', width = 27)
etiqueta_titulo.grid(row = 0, column = 0)

#panel izquierdo
panel_izq = Frame(aplicacion, bd = 2, relief = FLAT, bg = '#FFF0CA')
panel_izq.pack(side = LEFT)

#panel costos
panel_costos = Frame(panel_izq, bd = 2, relief= FLAT, bg = 'white')
panel_costos.pack(side = BOTTOM)

#panel comidas
panel_comidas = LabelFrame(panel_izq, text = 'COMIDA', font = ('Times New Roman', 15, 'bold'),
                           bd = 2, relief= FLAT, fg= '#703116', bg= '#FFF0CA')
panel_comidas.pack(side = LEFT)

#panel de bebidas
panel_bebidas = LabelFrame(panel_izq, text = 'BEBIDAS', font = ('Times New Roman', 15, 'bold'),
                           bd = 2, relief= FLAT, fg= '#703116', bg= '#FFF0CA')
panel_bebidas.pack(side = LEFT)

#panel de postres
panel_postres = LabelFrame(panel_izq, text = 'POSTRES', font = ('Times New Roman', 15, 'bold'),
                           bd = 2, relief= FLAT, fg= '#703116', bg= '#FFF0CA')
panel_postres.pack(side = LEFT)


#panel derecho
panel_der = Frame(aplicacion, bd = 2, relief= FLAT)
panel_der.pack(side = RIGHT)

#panel calculadora
panel_calculadora = Frame(panel_der, bd = 2, relief= FLAT, bg = '#FFF0CA')
panel_calculadora.pack()

#panel recibo
panel_recibo = Frame(panel_der, bd = 2, relief= FLAT, bg = '#FFF0CA')
panel_recibo.pack()

#panel botones
panel_botones = Frame(panel_der, bd = 2, relief= FLAT, bg = '#FFF0CA')
panel_botones.pack()


#lista de productos
lista_comidas = ['pizza margarita', 'ensalada', 'sandwich', 'huevos revueltos', 'pollo con arroz', 'pasta', 'tacos', 'sopa']
lista_bebidas = ['agua', 'jugo', 'gaseosa', 'cerveza malta', 'cerveza negra', 'vino espumante', 'vino', 'trago']
lista_postres = ['helado', 'fruta', 'milkshake', 'torta', 'chocolate', 'budin', 'alfajor', 'crema']

# generar items comidas

cuadros_comidas = []
texto_comida = []
variables_comidas = []
contador = 0

for comida in lista_comidas:
    
    #crear checkbuttons
    variables_comidas.append('')
    variables_comidas[contador] = IntVar()
    comida = Checkbutton(panel_comidas, text= comida.title(),
                         font = ('Times New Roman', 15, 'bold'),
                         onvalue= 1, offvalue= 0, fg= '#000000', bg= '#FFF0CA',
                         variable= variables_comidas[contador],
                         command= revisar_check)
    
    comida.grid(row = contador, column = 0, sticky= W)
    
    #crear cuadros de entrada
    cuadros_comidas.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comidas[contador] = Entry(panel_comidas,
                                      font = ('Times New Roman', 16, 'bold'),
                                      bd = 2,
                                      width= 6,
                                      state = DISABLED,
                                      textvariable= texto_comida[contador])
    cuadros_comidas[contador].grid(row = contador, column = 1)
    
    contador += 1
    
# generar items bebidas
cuadros_bebidas = []
texto_bebida = []
variables_bebidas = []

contador = 0

for bebida in lista_bebidas:
    #crear checkbuttons
    variables_bebidas.append('')
    variables_bebidas[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas, text= bebida.title(),
                         font = ('Times New Roman', 15, 'bold'),
                         onvalue= 1, offvalue= 0, fg= '#000000', bg= '#FFF0CA',
                         variable= variables_bebidas[contador],
                         command= revisar_check)
    
    bebida.grid(row = contador, column = 1, sticky= W)
    
    #crear cuadros de entrada
    cuadros_bebidas.append('')
    texto_bebida.append('')
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebidas[contador] = Entry(panel_bebidas,
                                      font = ('Times New Roman', 16, 'bold'),
                                      bd = 2,
                                      width= 6,
                                      state = DISABLED,
                                      textvariable= texto_bebida[contador])
    cuadros_bebidas[contador].grid(row = contador, column = 2)
    
    contador += 1
    
# generar items postres

cuadros_postres = []
texto_postre = []
variables_postres = []
contador = 0

for postre in lista_postres:
    #crear checkbuttons
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postre = Checkbutton(panel_postres, text= postre.title(),
                         font = ('Times New Roman', 15, 'bold'),
                         onvalue= 1, offvalue= 0, fg= '#000000', bg= '#FFF0CA',
                         variable= variables_postres[contador],
                         command = revisar_check)

    postre.grid(row = contador, column = 3, sticky= W)
    
    cuadros_postres.append('')
    texto_postre.append('')
    texto_postre[contador] = StringVar()
    texto_postre[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres,
                                      font = ('Times New Roman', 16, 'bold'),
                                      bd = 2,
                                      width= 6,
                                      state = DISABLED,
                                      textvariable= texto_postre[contador])
    cuadros_postres[contador].grid(row = contador, column = 4)
    
    contador += 1

# variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# etiquetas de costo y campos de entrada
#comida
etiqueta_costo_comida = Label(panel_costos,
                              text = 'COSTO COMIDA',
                              font = ('Times New Roman', 10, 'bold'),
                              bg = 'white',
                              fg = '#703116')
etiqueta_costo_comida.grid(row = 0, column = 0)

texto_costo_comida = Entry(panel_costos,
                           font = ('Times New Roman', 10, 'bold'),
                           bd = 2,
                           width = 10,
                           state = 'readonly',
                           textvariable = var_costo_comida)

texto_costo_comida.grid(row = 0, column = 1, padx = 50)

#bebida
etiqueta_costo_bebida = Label(panel_costos,
                              text = 'COSTO BEBIDA',
                              font = ('Times New Roman', 10, 'bold'),
                              bg = 'white',
                              fg = '#703116')
etiqueta_costo_bebida.grid(row = 1, column = 0)

texto_costo_bebida = Entry(panel_costos,
                           font = ('Times New Roman', 10, 'bold'),
                           bd = 2,
                           width = 10,
                           state = 'readonly',
                           textvariable = var_costo_bebida)

texto_costo_bebida.grid(row = 1, column = 1, padx = 50)

#postre
etiqueta_costo_postre = Label(panel_costos,
                              text = 'COSTO POSTRES',
                              font = ('Times New Roman', 10, 'bold'),
                              bg = 'white',
                              fg = '#703116')
etiqueta_costo_postre.grid(row = 2, column = 0)

texto_costo_postre = Entry(panel_costos,
                           font = ('Times New Roman', 10, 'bold'),
                           bd = 2,
                           width = 10,
                           state = 'readonly',
                           textvariable = var_costo_postre)

texto_costo_postre.grid(row = 2, column = 1, padx = 50)

#subtotal
etiqueta_subtotal = Label(panel_costos,
                              text = 'SUBTOTAL',
                              font = ('Times New Roman', 10, 'bold'),
                              bg = 'white',
                              fg = '#703116')
etiqueta_subtotal.grid(row = 0, column = 2)

texto_subtotal = Entry(panel_costos,
                           font = ('Times New Roman', 10, 'bold'),
                           bd = 2,
                           width = 10,
                           state = 'readonly',
                           textvariable = var_subtotal)

texto_subtotal.grid(row = 0, column = 3, padx = 50)

#impuestos
etiqueta_impuestos = Label(panel_costos,
                              text = 'IMPUESTOS',
                              font = ('Times New Roman', 10, 'bold'),
                              bg = 'white',
                              fg = '#703116')
etiqueta_impuestos.grid(row = 1, column = 2)

texto_impuestos = Entry(panel_costos,
                           font = ('Times New Roman', 10, 'bold'),
                           bd = 2,
                           width = 10,
                           state = 'readonly',
                           textvariable = var_impuesto)

texto_impuestos.grid(row = 1, column = 3, padx = 50)

#total
etiqueta_total = Label(panel_costos,
                              text = 'TOTAL',
                              font = ('Times New Roman', 10, 'bold'),
                              bg = 'white',
                              fg = '#703116')
etiqueta_total.grid(row = 2, column = 2)

texto_total = Entry(panel_costos,
                           font = ('Times New Roman', 10, 'bold'),
                           bd = 2,
                           width = 10,
                           state = 'readonly',
                           textvariable = var_total)

texto_total.grid(row = 2, column = 3, padx = 50)


#botones
botones = ['TOTAL', 'RECIBO', 'GUARDAR', 'RESETEAR']
botones_creados = []

cont_columnas = 0

for boton in botones:
    boton = Button(panel_botones,
                   text = boton.title(),
                   font = ('Times New Roman', 12, 'bold'),
                   fg = '#703116',
                   bg = 'white',
                   bd = 2,
                   width = 7)
    
    botones_creados.append(boton)
    
    boton.grid(row = 0,
               column = cont_columnas)
    
    cont_columnas += 1


botones_creados[0].config(command = total)
botones_creados[1].config(command = recibo)
botones_creados[2].config(command = guardar)
botones_creados[3].config(command = resetear)

# area de recibo
texto_recibo = Text(panel_recibo,
                    font = ('Times New Roman', 12, 'bold'),
                    bd = 2,
                    width = 42,
                    height = 10)
texto_recibo.grid(row = 0,
                  column = 0)


#calculadora
visor_calculadora = Entry(panel_calculadora,
                          font = ('Times New Roman', 14, 'bold'),
                          width = 30,
                          bd = 2)
visor_calculadora.grid(row = 0,
                       column = 0,
                       columnspan = 4)

#botones calculadora
boton_calculadora = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', 'x', 'CE', 'BORRAR', '0', '/']

botones_guardados = []

fila = 1
columna = 0
for boton in boton_calculadora:
    boton = Button(panel_calculadora,
                   text = boton.title(),
                   font = ('Times New Roman', 14, 'bold'),
                   fg = '#703116',
                   bg = 'white',
                   bd = 2,
                   width = 6)
    
    botones_guardados.append(boton)
    
    boton.grid(row = fila,
            column = columna)
    
    if columna == 3:
        fila += 1
    columna += 1
    if columna == 4:
        columna = 0


botones_guardados[0].config(command = lambda : click_boton_cal('7'))
botones_guardados[1].config(command = lambda : click_boton_cal('8'))
botones_guardados[2].config(command = lambda : click_boton_cal('9'))
botones_guardados[3].config(command = lambda : click_boton_cal('+'))
botones_guardados[4].config(command = lambda : click_boton_cal('4'))
botones_guardados[5].config(command = lambda : click_boton_cal('5'))
botones_guardados[6].config(command = lambda : click_boton_cal('6'))
botones_guardados[7].config(command = lambda : click_boton_cal('-'))
botones_guardados[8].config(command = lambda : click_boton_cal('1'))
botones_guardados[9].config(command = lambda : click_boton_cal('2'))
botones_guardados[10].config(command = lambda : click_boton_cal('3'))
botones_guardados[11].config(command = lambda : click_boton_cal('*'))
botones_guardados[12].config(command = obtener_resultado)
botones_guardados[13].config(command = borrar)
botones_guardados[14].config(command = lambda : click_boton_cal('0'))
botones_guardados[15].config(command = lambda : click_boton_cal('/'))

#evitar que la pantalla se cierre
aplicacion.mainloop()