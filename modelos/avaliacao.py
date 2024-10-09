class Avaliacao:
    '''
    Inicializa uma nova instância da classe Avaliacao.

    Args:
        cliente (str): O nome do cliente que fez a avaliação.
        nota (int ou float): A nota dada pelo cliente ao restaurante. 
                                 Deve ser um valor numérico, tipicamente entre 1 e 5.
    
    Atributos:
            _cliente (str): Armazena o nome do cliente.
            _nota (int ou float): Armazena a nota dada pelo cliente ao restaurante.
        
    '''
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota