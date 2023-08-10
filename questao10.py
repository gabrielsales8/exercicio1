def sao_pares_inversos(palavra1, palavra2):
    return palavra1 == palavra2[::-1]

def main():
    palavra1 = input("Digite a primeira palavra: ")
    palavra2 = input("Digite a segunda palavra: ")
    
    if sao_pares_inversos(palavra1, palavra2):
        print("As palavras são pares inversos.")
    else:
        print("As palavras não são pares inversos.")

if __name__ == "__main__":
    main()
