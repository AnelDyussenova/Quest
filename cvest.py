from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random




class Person:
    def __init__(self):
        self.name = 'Main Hero'
        self.xp = 100
        self.luk= 10
        self.mech= TRUE
        self.luk_arr=[TRUE,FALSE]
        self.mech_arr=[TRUE, TRUE, TRUE, FALSE]
        self.arr=[TRUE, TRUE, FALSE]
    def ataka_luk(self, ev_xp, popal):
        n= random.randint(1,2)
        self.luk=self.luk-1
        if self.luk==0:
            return ev_xp, popal, TRUE
        if(self.luk_arr[n-1]== TRUE):
            ev_xp=ev_xp-20
            popal=TRUE
            return ev_xp, popal,FALSE
        if(self.luk_arr[n-1]== FALSE):
            popal=FALSE
            return ev_xp, popal,FALSE
    def ataka_mech(self, ev_xp,popal):
        n= random.randint(1,4)
        m= random.randint(1,3)
        if(self.mech_arr[n-1]== TRUE):
            ev_xp=ev_xp-30
            popal=TRUE
            return ev_xp, popal,self.arr[m-1]
        if(self.mech_arr[n-1]== FALSE):
            popal=FALSE
            return ev_xp, popal,self.arr[m-1]
    def ataka(self, ev_xp,popal):
        n= random.randint(1,3)
        if(self.arr[n-1]== TRUE):
            ev_xp=ev_xp-30
            popal=TRUE
            return ev_xp, popal
        if(self.arr[n-1]== FALSE):
            popal=FALSE
            return ev_xp, popal
    def zashita(self,udar):
        udar= FALSE
    

class Evil:
    def __init__(self):
        self.name = 'Golem'
        self.xp = 100
        self.arr=[TRUE,FALSE]
    def a(self, pr_xp, udar):
        n= random.randint(1,2)
        if(self.arr[n-1]== TRUE):
            pr_xp=pr_xp-20
            udar=TRUE
            return pr_xp, udar
        if(self.arr[n-1]== FALSE):
            udar=FALSE
            return pr_xp, udar
    def ataka(self,  pr_xp):
        pr_xp=pr_xp-25
        return pr_xp


person = Person()
golem = Evil()
popal=FALSE
poteryl=FALSE
poteryl_luk=FALSE
print('')
while(person.xp>0 and golem.xp>0):
    print('HI')
    otv = input()
    if otv == '1':
        if poteryl!=TRUE:
            golem.xp, popal, poteryl_luk= person.ataka_luk(golem.xp, popal)
            if popal==FALSE:
                person.xp= golem.ataka(person.xp)
            if poteryl==TRUE:
                print('poteryl')
        else:
            person.xp= golem.ataka(person.xp)
    elif otv == '2':
        if poteryl!=TRUE:
            golem.xp, popal, poteryl= person.ataka_mech(golem.xp, popal)
            if popal==FALSE:
                person.xp= golem.ataka(person.xp)
            if poteryl==TRUE:
                print('poteryl')
        else:
            person.xp= golem.ataka(person.xp)
    elif otv == '3':
        golem.xp, popal= person.ataka(golem.xp, popal)
        if popal==FALSE:
            person.xp= golem.ataka(person.xp)
    elif otv == '4':
        person.zashita(popal)

    if popal==TRUE:
        print("golem",golem.xp)
    elif popal==FALSE:
        print("person",person.xp)

        
if(person.xp>golem.xp):
    print('Win')
elif(person.xp<golem.xp):
    print('Game over')
else:
    print('Hmm..')


    
print('Добро пожаловать в Квест.')
print('Вы очнулись в незнакомом помещение')
print('Перед вами 3 двери с номерами: 1, 2 или 3.')
print('Дверь из которой можно выбраться - не крайняя, в какую пройдете?')
otv1 = input()
if otv1 == '3':
    print('Пройдя в эту дверь, она захлопнулась. Выхода нет. Game over.')
elif otv1 == '1':
    print('Вы прошли в пропасть')
if otv1 == '2':
    print('Вы в следующей комнате')
    print('Выход отсюда возможен через 2 двери.')
    print('Дверь справа под номером 1, дверь слева под номером 2,')
    print('над дверью слева написано: выход в двери под номером 2.')
    print('Выход справа или слева?')
    otv2 = input()
    if otv2 == 'справа':
        print('Вы смело открыли правую дверь. Но за ней вас подстерегала ')
        print('гигантская подземная жаба, которая проглотила вас целиком!')
    elif otv2 == 'слева':
        print('Вы на улице!')




        
    






