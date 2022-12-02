#Generador de contraseñas Fernando Madroñal

import random
import secrets
import string
#Opcion1: dos cadenas aleatorias unidas
#Opcion2: dos cadenas aleatorias unidas que se vuelven a desordenar
#Opcion3: dos cadenas aleatorias unidas que se vuelven a desordenar sin caracteres especiales
#Opcion4: dos cadenas aleatorias unidas de 1000 caracteres en total que se vuelven a desordenar
# se le suman otras dos cadenas aleatorias desordenadas de 1000 caracteres, vuelve a desordenar los 2000 caracteres
# y se selecciona un subconjunto aleatorio con un tamaño de caracteres seleccionado
letras= string.ascii_letters
letrasMayus=string.ascii_uppercase
digitos=string.digits
caracteresEspeciales=string.punctuation
alfabeto= letras+ letrasMayus + digitos + caracteresEspeciales
alfabetoSinEsp= letras+ letrasMayus + digitos 
def genera(n):
    tam1=5
    tam2=500
    subTam=14
    
    if(n==1 or n==2):
      while True:
        password1 = ''
        password2 = ''
        for i in range(tam1):
            password1 += ''.join(secrets.choice(alfabeto))
        if(any(char in caracteresEspeciales for char in password1) and 
            sum(char in digitos for char in password1 )>=3) and sum(char in letrasMayus for char in password1)<1:
             i=0
             
        for i in range (tam1):
            password2 += ''.join(secrets.choice(alfabeto))
        if(any(char in caracteresEspeciales for char in password2) and 
            sum(char in digitos for char in password2 )>=2):
               i=0

        if(n==1):
            p=password2 + password1
            return p

        if(n==2):
            t1=tam1+tam1
            p=password2 + password1
            password=random.sample((p),(t1))
            password=''.join(password)
            return password

    elif(n==3):
     while True:
        password1 = ''
        password2 = ''
        for i in range(tam1):
            password1 += ''.join(secrets.choice(alfabetoSinEsp))
        if(sum(char in digitos for char in password1 )>=3) and sum(char in letrasMayus for char in password1)<1:
             i=0

        for i in range (tam1):
            password2 += ''.join(secrets.choice(alfabetoSinEsp))
        if(sum(char in digitos for char in password2 )>=2):
               i=0
        t1=tam1+tam1
        p=password2 + password1
        password=random.sample((p),(t1))
        password=''.join(password)
        return password

def generaTam(n,subTam):
    if(n==4):
     while True:
        tam2=500
        password1 = ''
        password2 = ''
        password3 = ''
        password4 = ''
        for i in range(tam2):
            password1 += ''.join(secrets.choice(alfabeto))
        if(sum(char in caracteresEspeciales for char in password1)<30 and 
            sum(char in digitos for char in password1 )>=90)and sum(char in letrasMayus for char in password1)<90:
           # break
           i=0
        for i in range (tam2):
            password2 += ''.join(secrets.choice(alfabeto))
        if(any(char in caracteresEspeciales for char in password2) and 
            sum(char in digitos for char in password2 )>=50):
                i=0
        for i in range(tam2):
            password3 += ''.join(secrets.choice(alfabeto))
        if(sum(char in caracteresEspeciales for char in password3)<20 and 
            sum(char in digitos for char in password3 )>=80) and sum(char in letrasMayus for char in password3)<30:
               i=0
        
        for  i in range (tam2):
            password4 += ''.join(secrets.choice(alfabeto))
        if(any(char in caracteresEspeciales for char in password4) and 
                sum(char in digitos for char in password4 )>=50):
               i=0

        t2=tam2*2
        pHard1=password3+password4
        phard2=password2+password1
        passHard1=random.sample(pHard1,t2)
        passHard2=random.sample(phard2,t2)
        union=passHard2+passHard1
        passdHard=''.join(union)
        willy=random.sample(passdHard,subTam)
        willy=''.join(willy)
        return willy

menu_options = {
    1: 'Normal',
    2: 'Hard',
    3: 'Hard sin carácteres especiales',
    4: 'Willy Level',
    5: 'No quiero contraseña',
}
def print_menu():
    for key in menu_options.keys():
        print (key, '-', menu_options[key] )
def option1():
     print('\nOpción Seleccionada \'Normal\'\n')
     print('Contraseña: ' +genera(1))
     
def option2():
     print('\nOpción Seleccionada \'Hard\'\n')
     print('Contraseña: ' +genera(2))
     
def option3():
     print('\nOpción Seleccionada \'Hard sin carácteres especiales\'\n')
     print('Contraseña: ' +genera(3))
def option4():
     print('\nOpción Seleccionada \'Willy Level\'\n')
     print('Inserte el la longitud que desea de la contraseña:\n')
     tex_number=''
     try:   
        tex_number=input("")  
     except:
            print('Entrada Incorrecta. por favor inserte un número ...')
            
     subTam=int(tex_number)
     print('\nContraseña: ' + generaTam(4,subTam) )
     if(subTam>=30):
        print('Te has pasado Willy\n')
if __name__=='__main__':
    while(True):
        print("\nGenerador de Contraseñas\n")
        print_menu()
        option = ''
        try:
            option = int(input('\nSeleccione el tipo de contraseña: '))
        except:
            print('Entrada Incorrecta. por favor inserte un número ...')
        #Elige la entrada
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            option4()
        elif option == 5:
            print('Thanks message before exiting')
            exit()
        else:
            print('\nOpcion invalida. Por favor inserte un numero entre 1 y 4.\n')