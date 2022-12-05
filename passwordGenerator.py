#Generador de contraseñas 

import random
import secrets
import string
import time
letras= string.ascii_lowercase
letrasMayus=string.ascii_uppercase
digitos=string.digits
caracteresEspeciales=string.punctuation
alfabeto= letras+ letrasMayus + digitos + caracteresEspeciales
alfabetoSinEsp= letras+ letrasMayus + digitos 
def genera(n):
    tam1=10    
    if(n==1 or n==2):

        while True:
            pwd = ''
            for i in range(tam1):
                pwd += ''.join(secrets.choice(alfabeto))

            if (any(char in caracteresEspeciales for char in pwd) and 
                sum(char in digitos for char in pwd)>=3 and sum(char in letrasMayus for char in pwd)>2 and sum(char in letras for char in pwd)>2):
                    break

        if(n==1):
            return pwd
            
        if(n==2):
            password=random.sample(pwd,tam1)
            password=''.join(password)
            return password

    if(n==3):
        while True:
            pwd = ''
            for i in range(tam1):
                pwd += ''.join(secrets.choice(alfabetoSinEsp))

            if (sum(char in digitos for char in pwd)>=3 and sum(char in letrasMayus for char in pwd)>2 and sum(char in letras for char in pwd)>2):
                    break

        password=random.sample(pwd,tam1)
        password=''.join(password)
        return password
    

def generaTam(n,subTam):
 if(n==4):
    while True:
        tam2=subTam*500
        password1 = ''
        for i in range(tam2):
            password1 += ''.join(secrets.choice(alfabeto))
        if(sum(char in caracteresEspeciales for char in password1)>100 and 
            sum(char in digitos for char in password1 )>100 and sum(char in letrasMayus for char in password1)>100 and sum(char in letras for char in password1)>100):
                 break
    while True: 
        tam2=subTam*500
        password2 = ''
        for i in range(tam2):
            password2 += ''.join(secrets.choice(alfabeto))
        if(sum(char in caracteresEspeciales for char in password2)>90 and 
            sum(char in digitos for char in password2 )>100 and sum(char in letrasMayus for char in password2)>110 and sum(char in letras for char in password2)>100):
                break
               
       # for i in range (tam2):
            
        #    if(sum(char in caracteresEspeciales for char in password2)>90 and 
         #   sum(char in digitos for char in password2 )>100 and sum(char in letrasMayus for char in password2)>100 and sum(char in letras for char in password2)>100):
          #      break


    t2=tam2*2
    phard1=password2+password1     
    passHard1=random.sample(phard1,t2)  
    passdHard=''.join(passHard1)

    
    while True:  
        will=''
        for i in range (subTam):
            will += ''.join(secrets.choice(passdHard))
        if(sum(char in caracteresEspeciales for char in will)>1 and sum(char in digitos for char in will)>1
         and sum(char in letras for char in will)>2 and sum(char in letrasMayus for char in will)>1):           
            break

    willy=''.join(will)
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
     print('Inserte la longitud que desea de la contraseña:')
     tex_number=0
     while True:
        try:   
            tex_number=int(input("Longitud mínima de 10 carácteres\n")) 
            if  tex_number < 10:
                print("El número de carácteres introducido debe ser mayor o igual a 10")
                break
                 
            subTam=int(tex_number)
        except:      
            print('Entrada Incorrecta. por favor inserte un número ...')
     
        print('\nContraseña: ' + generaTam(4,subTam) )
        if(subTam>=30):
            print('¡Te has pasado Willy!\n')
        break

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
            print('Gracias por usar el Generador de Contraseñas')
            time.sleep(2)
            exit()
        else:
            print('\nOpcion invalida. Por favor inserte un numero entre 1 y 4.\n')