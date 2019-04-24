userInput = input("Votre date de naissance :")
age = 2019 - int(userInput)
print("Vous avez " + str(age) + " ans.")

#----------------------------------------------------------------------------#

userNumber = "rien"
userNumber = input("Entrez un nombre :")
if int(userNumber) != 0 :
	print("Ce nombre est différent de 0.")
else:
	print("Votre nombre est égal à 0.")