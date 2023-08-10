def main():
    idades = []
    
    for i in range(10):
        idade = int(input(f"Digite a {i+1}ª idade: "))
        idades.append(idade)

    print("Lista de idades:", idades)
    
    while idades:
        del idades[-1]
    
    print("Lista de idades vazia:", idades)

if __name__ == "__main__":
    main()
