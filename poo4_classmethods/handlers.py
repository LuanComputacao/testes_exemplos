class VendasHandler:

    @staticmethod
    def vender(lista_de_produtos: list, nomes_dos_produtos: list):
        """Remove um produto da lista e retorna a nova lista e o valor da venda

        Procura um produto na lista com o nome do produto fornecido

        :param nomes_dos_produtos:
        :param lista_de_produtos:
        :return:
        """
        total = 0

        for nome in nomes_dos_produtos:
            lista_de_produtos, preco = VendasHandler.retirar_produto_da_lista_por_nome(
                lista_de_produtos, nome)
            total += preco

        return lista_de_produtos, total

    @staticmethod
    def retirar_produto_da_lista_por_nome(lista_de_produtos, nome_do_produto):
        """Retira o produto e retorna o valor do mesmo

        :param lista_de_produtos:
        :param nome_do_produto:
        :return:
        """
        valor_da_venda = 0

        for i, p in enumerate(lista_de_produtos):
            if p.nome == nome_do_produto:
                valor_da_venda = p.preco
                del lista_de_produtos[i]
                break

        return lista_de_produtos, valor_da_venda
