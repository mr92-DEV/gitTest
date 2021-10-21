import sqlite3

class Gases:
    id=0
    temperature=0
    pressure=0
    volume=0

conn = sqlite3.connect('/home/pi/Documents/Programacion/MyDatabase.db')
cur = conn.cursor()

#print headers and attributes class description
cur.execute("PRAGMA table_info(Gases)")
head = cur.fetchall() 
print (head)

#execute table query
table = cur.execute('SELECT * from Gases')

#create a list
gasesList = []

#instance of a class and add values and make a list of Gases class object
for row in table:
    gases = Gases()
    gases.id = row[0]
    gases.temperature = row[1]
    gases.pressure = row[2]
    gases.volume = row[3]
    gasesList.append(gases)


#Para una misma masa gaseosa (por tanto, el número de moles «n» es constante), podemos afirmar que existe una constante directamente proporcional a la presión y volumen del gas, e inversamente proporcional a su temperatura.
#calcula la temperatura de una misma masa gaseosa sometida a un cambio de presion y volumen ingresado por el usuario

print("Para una misma masa gaseosa (por tanto, el número de moles «n» es constante), podemos afirmar que existe una constante directamente proporcional a la presión y volumen del gas, e inversamente proporcional a su temperatura.")
print("calcula la temperatura de una misma masa gaseosa sometida a un cambio de presion y volumen ingresado por el usuario")

for gas in gasesList:

    text = "Introduce a value for the {} state where temperature(K) {} , volume(dm3) {} and pressure(atm){}:".format(str(gas.id),str(gas.temperature),str(gas.volume),str(gas.pressure))
    print(text)
    v2 = float(input("Introduce a value for the second state volume(dm3):"))
    p2 = float(input("Introduce a value for the second state pressure(atm):"))
    T2 = ((gas.temperature * p2 *v2)/(gas.volume * gas.pressure))
    responseText = "The temperature for the {} state is {} Kelvin".format(str(gas.id),str(T2))
    print(responseText) 