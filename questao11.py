def eh_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def imprimir_primos_entre_1_e_50():
    print("Números primos entre 1 e 50:")
    for numero in range(1, 51):
        if eh_primo(numero):
            print(numero)

def main():
    imprimir_primos_entre_1_e_50()

if __name__ == "__main__":
    main()
