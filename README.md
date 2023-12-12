# Raising-errors
types of errors and treatments

# finally
  - Se finally estiver presente, ele especifica um manipulador de ‘limpeza’.
- O try cláusula é executada, incluindo qualquer except e else cláusulas.
 - Se ocorrer uma exceção em qualquer uma das cláusulas e for não tratada, a exceção é salva temporariamente.
  - A cláusula finally É executado. Se houver uma exceção salva, ela será levantada novamente no final do finally cláusula.
  - Se a cláusula finally gerar outra exceção, a exceção salva é definida como o contexto da nova exceção. 
  - Se a cláusula finally executar um return, break ou continue, a exceção salva é descartada:

# Se uma cláusula finally estiver presente, a cláusula finally será executada como a última tarefa antes da conclusão da instrução try. A cláusula finally executa se a instrução try produz uma exceção.

```Py
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    print(f"O resultado é: {resultado}")
except ValueError:
    print("Você deve digitar um número.")
except ZeroDivisionError:
    print("Não é possível dividir por zero.")
finally:
    print("Este bloco é sempre executado.")
```
# Raise

A instrução raise permite ao programador forçar a ocorrência de um determinado tipo de exceção. Por exemplo:

```Py
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
```
- Caso você precise determinar se uma exceção foi levantada ou não, mas não quer manipular o erro, uma forma simples de instrução raise permite que você levante-a novamente

```Py
raise NameError('Oieee')
```
