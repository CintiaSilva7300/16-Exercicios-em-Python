#para saber qual sera o tratamento de atendimento de um mercado hospital
# ou ate msm uma loterica para saber 
# qual sera a melhor forma de atenmder esse paciente ou cliente
idade = int(input('Digite uma idade: '))
if idade > 65:
  print('Acesso prioritario')
elif idade > 45:
  print('Acesso preferencial')  
elif idade > 18:
   print('Acesso liberado')
else:
  print('Acesso bloqueado')
print('Final do programa')