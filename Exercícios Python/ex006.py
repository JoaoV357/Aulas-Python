#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e a sua raiz quadrada.
num = int(input('Digite um número: '))
raiz_quad = (num**0.5)
print('O seu número é {}, o dobro dele é {}, o triplo é {}.\na raiz quadrada do número {} é {:.2f}'.format(num, num*2, num*3, num, raiz_quad)) #Obs: Utiliza-se \n para fazer uma quebra de linha.
