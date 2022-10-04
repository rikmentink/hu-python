### 5.1 ###
# def som(getal1, getal2, getal3):
#     return sum([getal1, getal2, getal3])

# print(som(1,2,3))

### 5.2 ###
# def som(getallenLijst):
#     return sum(getallenLijst)

# print(som([1, 3, 5]))

### 5.3 ###
# def lang_genoeg(lengte):
#     if lengte >= 120:
#         return "Je bent lang genoeg voor de attractie!"
#     else:
#         return "Sorry, je bent te klein."
#
# lengte = int(input("Wat is jouw lengte in centimeters?\n"))
# print(lang_genoeg(lengte))

### 5.4 ###
# def new_password(oldpassword, newpassword):
#     return newpassword != oldpassword and len(newpassword) >= 6

# oldpassword = input("Voer uw oude wachtwoord in: ")
# newpassword = input("Voer uw nieuwe wachtwoord in: ")

# if len(newpassword) != 0:
#     print(new_password(oldpassword, newpassword))
# else:
#     print("Voer een nieuw wachtwoord in.")

# TODO: 5.5

### 5.6 ###
def wijzig(letterlijst):
    letterlijst.clear()
    letterlijst.append('d')
    letterlijst.append('e')
    letterlijst.append('f')

lijst = ['a', 'b', 'c']
print(lijst)
wijzig(lijst)
print(lijst)