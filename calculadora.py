while True:
 fechamento=(input("Digite sair, para sair ou digite outra coisa para continuar"))
 if fechamento.lower()=="sair":
  break 
 while True:
    try:
      num1=float(input("Digite um número:"))
      break
    except ValueError:
      print("Digite um número válido")
 operador=(input ("Qual operador você quer?"))
 num2=float(input("Digite um número:"))
 if operador=="+":
    print ("Resultado:",num1+num2)
 elif operador=="-":
    print("Resultado:",num1-num2)
 elif operador=="*":
    print("Resultado:",num1*num2)
 elif operador=="/":
    if num2==0:
       print("Erro") 
    else:
       print("Resultado:",num1/num2)
 else:
    print("Operador inválido") 
