

    
print( "KONVERSI SUHU FARENHEIT KE KELVIN" )

F = float(input("Masukkan suhu fahrenheit : "))
print ( "suhu fahrenheit", F ) 

R = 4/9 * (F - 32)
print  ( "Farenheit ke reamur adalah ", R, "reamur" )

C = 5/9 * (F - 32)
print  ( "Farenheit ke celcius adalah ", C, " cel cius" )

K1 = (5/4 * R) + 273
print  ( "Reamur ke kelvin adalah ", K1 , "kelvin" )

K2 = C + 273
print ( "celcius ke kelvin adalah ", K2, " kelvin")
print ("jadi konversi farenheit ke kelvin adalah", K2,"/", K1, "dengan cara di konversikan ke celcius / reamur terlebih dahulu")

