import random
import os
A1="Cette réponse nécessite un abonnement payant pour voir"
A2="Vous verrez"
A3="Ne voudrais-tu savais"
A4="Les choses arrivent, les choses ne se passent pas"
A5="Pourquoi me demandez-vous, je ne sais rien"
A6="Sen aller"
A7="Je suis en pause, demandez dans le siècle prochain"
A8="Ce nest pas parce que je le sais que je veux vous répondre"
x= 0
list=[A1,A2,A3,A4,A5,A6,A7,A8]
answer=""
print("Cette balle de huit répondra à la question oui ou non, et note latérale si tu veux le aretter ecris arret.")
os.system("say Cette balle de huit répondra à la question oui ou non, et note latérale si tu veux le aretter ecris arret.")
answer = input("Poser une question ")
while answer!= "arret":


    num = random.randint (0, len(list)-1)
    wisdom= list[num]
    print(wisdom)
    os.system("say "+ wisdom)
    answer = input("Poser une question ")
