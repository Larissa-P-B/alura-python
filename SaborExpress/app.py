from modelos.restaurantes import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.0, 'grande')
bebida_suco.aplicar_desconto()
prato_paozinho = Prato('Paozinho', 2.00,'O melhor pão da cidade')
prato_paozinho.aplicar_desconto()
restaurante_praca.add_no_cardapio(bebida_suco)
restaurante_praca.add_no_cardapio(prato_paozinho)
#restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
#restaurante_japones = Restaurante('Japa', 'Japonesa')

#restaurante_mexicano.alternar_estado()

#restaurante_praca.receber_avaliacao('Gui', 10)
#restaurante_praca.receber_avaliacao('Lais', 8)
#restaurante_praca.receber_avaliacao('Emy', 2)

def main():
    restaurante_praca.exibir_cardapio
    #Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()


    