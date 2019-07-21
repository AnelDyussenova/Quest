from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random



class Person:
    def __init__(self):
        self.name = 'Main Hero'
        self.xp = 100
        self.luk= 7
        self.mech= TRUE
        self.luk_arr=[TRUE,TRUE, TRUE, TRUE,TRUE, TRUE, FALSE]
        self.mech_arr=[TRUE, TRUE, TRUE, FALSE]
        self.arr=[TRUE, TRUE, FALSE]
    def ataka_luk(self, ev_xp, popal):
        n= random.randint(1,7)
        self.luk=self.luk-1
        if self.luk==0:
            return ev_xp, popal, TRUE
        if(self.luk_arr[n-1]== TRUE):
            ev_xp=ev_xp-10
            popal=TRUE
            return ev_xp, popal,FALSE
        if(self.luk_arr[n-1]== FALSE):
            popal=FALSE
            return ev_xp, popal,FALSE
    def ataka_mech(self, ev_xp,popal):
        n= random.randint(1,4)
        m= random.randint(1,3)
        if(self.mech_arr[n-1]== TRUE):
            ev_xp=ev_xp-25
            popal=TRUE
            return ev_xp, popal,self.arr[m-1]
        if(self.mech_arr[n-1]== FALSE):
            popal=FALSE
            return ev_xp, popal,self.arr[m-1]
    def ataka(self, ev_xp,popal):
        n= random.randint(1,3)
        if(self.arr[n-1]== TRUE):
            ev_xp=ev_xp-10
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

def mmain():
    person = Person()
    golem = Evil()
    popal=FALSE
    poteryl=FALSE
    poteryl_luk=FALSE
    print("Your task is to kill the golem.\nGolem's life:  100\nYour life: 100")
    print('Bow damage: 10; probability of hitting: 86%\nSword damage: 25; probability of hitting: 75%\nMelee strike damage: 10; probability of hitting: 67%')
    while(person.xp>0 and golem.xp>0):
        print('Attack')
        if poteryl_luk== TRUE:
            print("You run out of arrows\nPress 2 to use sword\nPress 3 to melee strike")
        if poteryl==TRUE:
            print("Press 1 to use bow\nYou lost your sword\nPress 3 to melee strike")
        if poteryl== FALSE and poteryl_luk==FALSE:
            print("Press 1 to use bow\nPress 2 to use sword\nPress 3 to melee strike")
        otv = input()
        if otv == '1':
            if poteryl_luk!=TRUE:
                golem.xp, popal, poteryl_luk= person.ataka_luk(golem.xp, popal)
                if popal==FALSE:
                    person.xp= golem.ataka(person.xp)
                if poteryl_luk==TRUE:
                    print('You run out of arrows')
            else:
                print("You run out of arrows")
                person.xp= golem.ataka(person.xp)
            if popal==TRUE:
                print("You hit. Golem's life: ",golem.xp)
            elif popal==FALSE:
                print("Your blow failed. You are attacked by a golem. Your life: ",person.xp)
        elif otv == '2':
            if poteryl!=TRUE:
                golem.xp, popal, poteryl= person.ataka_mech(golem.xp, popal)
                if popal==FALSE:
                    person.xp= golem.ataka(person.xp)
                if poteryl==TRUE:
                    print('You lost your sword')
            else:
                person.xp= golem.ataka(person.xp)
            if popal==TRUE:
                print("You hit. Golem's life: ",golem.xp)
            elif popal==FALSE:
                print("Your blow failed. You are attacked by a golem. Your life: ",person.xp)
        elif otv == '3':
            golem.xp, popal= person.ataka(golem.xp, popal)
            if popal==FALSE:
                person.xp= golem.ataka(person.xp)
            if popal==TRUE:
                print("You hit. Golem's life: ",golem.xp)
            elif popal==FALSE:
                print("Your blow failed. You are attacked by a golem. Your life: ",person.xp)
        elif otv == '4':
            person.zashita(popal)
            print("Protection. Your life: ",person.xp,"Golem's life: ",golem.xp)
        popal=FALSE
            
    if(person.xp>golem.xp):
        print('Congratulations, you won!!!!')
    elif(person.xp<golem.xp):
        print('Game over')
    else:
        print('Hmm... both of you died')
    again()
def again():
    print("Do you want to play again?")
    otv = input()
    if otv.lower()=='yes':
        mmain()
    elif otv.lower()=='no': 
        print("Okey, bye))")

mmain()

        
    






