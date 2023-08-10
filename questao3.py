def main():
    notas = []
    
    for i in range(4):
        nota = float(input(f"Digite a {i+1}ª nota: "))
        notas.append(nota)
    
    media = sum(notas) / len(notas)
    
    print("\nNotas digitadas:")
    for i, nota in enumerate(notas, start=1):
        print(f"Nota {i}: {nota}")
    
    print(f"Média: {media:.2f}")

if __name__ == "__main__":
    main()
