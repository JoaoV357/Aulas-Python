#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
nota_final = (nota_1 + nota_2) / 2
print('A média das suas notas foi {}.'.format(nota_final))