while True:
    try:
        x = int(input("Digite um valor int: "))
        break
    except ValueError:
        pass


import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError:
    print("Oie")
except ValueError:
    print("Could not convert data to an integer.")
except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
    raise

/////////////////////////////////////////////////////////////

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

/////////////////////////////////////////////////////////////

try:
    raise KeyboardInterrupt
except:
    print('Goodbye, world!')

/////////////////////////////////////////////////////////////

try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise
