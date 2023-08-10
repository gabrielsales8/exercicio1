def main():
    lista_de_compras = ["arroz", "feijão", "macarrão", "ovos", "produtos de limpeza", "sorvete"]

    print("Lista de compras antes de ir ao mercado:", lista_de_compras)
    
    # Questão 7 - Produtos de limpeza
    if "produtos de limpeza" in lista_de_compras:
        lista_de_compras.remove("produtos de limpeza")
    
    print("Lista de compras depois de ir ao mercado:", lista_de_compras)
    
    # Questão 8 - Sorvete
    if "sorvete" in lista_de_compras:
        lista_de_compras.remove("sorvete")
    
    print("Lista de compras depois de ir à sorveteria:", lista_de_compras)

if __name__ == "__main__":
    main()
