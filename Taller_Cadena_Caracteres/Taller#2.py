name = "luis"
age= 27
favouriteFood = "pasta con salsa boloñesa"
texto1 = f"Hola! Mi nombre es {name}. yo tengo {age} años, y mi comida favorita es {favouriteFood}"
print(texto1)

#funcion len()
fullName  = "luis Alfonso vejarano"
texto2 = len (fullName.replace(" ", ""))
print (f"hola,  {fullName} tiene {texto2} letras excluyendo los espacios")

#formatstring()
increaseSalesPercent = 12.93720081
revenueGrowthPercent = 18.33206078
texto3 = f"las ventas de la empresa lactea aumentarom un {increaseSalesPercent:.2f}% y los ingresos crecieron {revenueGrowthPercent:.2f}%"
print(texto3)

# como decodificar un mensaje en python()
secretMessage = "aS!Ir waQm  VL!eDafrcnXi n=gS .P,yytahgoln.!"
texto4 = secretMessage [3::2]
print(texto4)

#lens()
text = 'El nombre "Python" viene dado por la afición de Van Rossum al grupo Monty Python.'
texto5 = len (text.split())
print(f"numero de palabras en la frase: {texto5}")

#()
word = "camila"
texto6 = word.replace("a","e")
print(texto6)

#()
sentence = "La historia del lenguaje de programación Python"
text7 = ' '.join(sentence.split()[::-1])
print(text7)

