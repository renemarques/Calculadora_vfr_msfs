from tkinter.ttk import *
from tkinter import *

cor1 = '#9bb9e8'

app = Tk()
app.title('CALCULADORA VFR')
app.geometry('300x550')
app.resizable(width=False, height=False)
app.configure(background=cor1)



#calculos
try:
    def calcular():

        aeronave = lista_cb.get()
        nm = dist_entry.get()
        vel = vel_entry.get()
        fl = fl_entry.get()
       
        target = fltarget_entry.get()
        target = int(target)
        fl = int(fl)
        vel = int(vel)
        nm = int(nm)
        target = (fl - target )* 3/1000
        autonomia = (nm / vel) * 60
        
        
        if aeronave == 'Cessna 152':
            consumo = 30
            gas = consumo / 60 * autonomia
            reserva = consumo / 60 * 30
            combustivel = gas + reserva
        elif aeronave == 'Cessna 172':
            consumo = 35
            gas = consumo / 60 * autonomia
            reserva = consumo / 60 * 30
            combustivel = gas + reserva
        elif aeronave == 'Cessna 208':
            consumo = 243
            gas = consumo / 60 * autonomia
            reserva = consumo / 60 * 30
            combustivel = gas + reserva
        elif aeronave == 'Baron 58':
            consumo = 120
            gas = consumo / 60 * autonomia
            reserva = consumo / 60 * 30
            combustivel = gas + reserva
        else :
            consumo = 35
            gas = consumo / 60 * autonomia
            reserva = consumo / 60 * 30
            combustivel = gas + reserva

        autonomia = int(autonomia)
        gas = int(gas)
        target = str(target)
        return_origem['text'] = 'ORIGEM = ' + dep_entry.get()
        return_destino['text'] = 'DESTINO = ' + arr_entry.get()
        return_cruzeiro['text'] = 'ALTITUDE DE VOO = ' + fl_entry.get()
        return_aeronave['text']= 'AERONAVE = ' + aeronave
        return_tempo['text'] = 'AUTONOMIA ='  + f'{autonomia:.2f}'+ 'MIN'
        return_combustivel['text'] = 'Combustivel Bordo = ' + f'{combustivel:.2f}, LTS'
        return_tod['text']='TOP OF DESCEND = ' + target +'NM'
        
        
       
except:
    print('Informe os valores corretos')       
    
#MENU AERONAVE

aeronave_label= Label(app,text='SELECIONE AERONAVE',bg=cor1)
aeronave_label.place(x=10,y=5)

lista_cb = Combobox(app,values=['Cessna 152','Cessna 172','Cessna 208','Baron 58','Cherokke Pa28'])
lista_cb.place(x=150,y=5)
lista_cb.current(0)

#corpo de informação 

dep_label = Label(app,text='INFORME ORIGEM ',anchor=W,bg=cor1)
dep_label.place(x=10, y=40)
dep_entry = Entry(app,width=5,font='Arial 10 bold')
dep_entry.place(x=230, y=40)

arr_label = Label(app,text='INFORME DESTINO ',anchor=W,bg=cor1)
arr_label.place(x=10, y=80)
arr_entry = Entry(app,width=5,font='Arial 10 bold')
arr_entry.place(x=230, y=80)

alt_label = Label(app,text='INFORME ALTERNADO ',anchor=W,bg=cor1)
alt_label.place(x=10, y=120)
alt_entry = Entry(app,width=5,font='Arial 10 bold')
alt_entry.place(x=230, y=120)

dist_label = Label(app,text='INFORME DISTANCIA NM ',anchor=W,bg=cor1)
dist_label.place(x=10, y=160)
dist_entry = Entry(app,width=5,font='Arial 10 bold')
dist_entry.place(x=230, y=160)

vel_label = Label(app,text='INFORME VEL CRUZEIRO',anchor=W,bg=cor1)
vel_label.place(x=10, y=200)
vel_entry = Entry(app,width=5,font='Arial 10 bold')
vel_entry.place(x=230, y=200)

fl_label = Label(app,text='INFORME ALTITUDE',anchor=W,bg=cor1)
fl_label.place(x=10, y=240)
fl_entry = Entry(app,width=5,font='Arial 10 bold')
fl_entry.place(x=230, y=240)

fltarget_label = Label(app,text='INFORME ALTITUDE Destino',anchor=W,bg=cor1)
fltarget_label.place(x=10, y=280)
fltarget_entry = Entry(app,width=5,font='Arial 10 bold')
fltarget_entry.place(x=230, y=280)

#retorno 


return_label = Label(app,text='PLANEJAMENTO',anchor=CENTER,bg=cor1)
return_label.place(x=100, y=300)

return_origem = Label(app,text='',anchor=W,bg=cor1)
return_origem.place(x=10, y=320)

return_destino = Label(app,text='',anchor=W,bg=cor1)
return_destino.place(x=10, y=340)

return_aeronave = Label(app,text='',anchor=W,bg=cor1)
return_aeronave.place(x=10, y=360)

return_cruzeiro = Label(app,text='',anchor=W,bg=cor1)
return_cruzeiro.place(x=10, y=380)

return_tempo = Label(app,text='',anchor=W,bg=cor1)
return_tempo.place(x=10, y=400)

return_combustivel = Label(app,text='',anchor=W,bg=cor1)
return_combustivel.place(x=10, y=420)

return_tod = Label(app,text='',anchor=W,bg=cor1)
return_tod.place(x=10, y=440)

botao = Button(app, width=8,command=calcular, height=1, text='Calcular', relief='raised')
botao.place(x=10,y=490)

botao = Button(app, width=8, height=1, text='METAR', relief='raised')
botao.place(x=120,y=490)

app.mainloop()


