from decimal import Decimal
from django.conf import settings
from loja.models import Produto

class Cart:
    def __init__(self, request):
        
        #Inicializando o cart
        
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            #Salva um cart vaziona session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
    
    def adicionar(self, produto, quantidade=1, override_quantity =False):
        #Adiciona o producto ao cart e atualiza a quantidade
        id_produto = str(produto.id)
        if id_produto not in self.cart:
            self.cart[id_produto] = {
                'quantidade': 0,
                'preco': str(produto.preco),
            }
        if override_quantity:
            self.cart[id_produto]['quantidade'] = quantidade
        else:
            self.cart[id_produto]['quantidade'] += quantidade
        self.save()
        
    def salvar(self):
        #Marca a session como modified e salva
        self.session.modified = True
    
    def remover(self, produto):
        #Remove produto do cart
        id_produto = str(produto.id)
        if id_produto in self.cart:
            del self.cart[id_produto]
            self.save()
            
    def __iter__(self):
        #Itera os produtos do cart e pega os produtos do banco de dados
        ids_produtos = self.cart.keys()
        #Pega os objetos produto e adiciona-os ao cart
        produtos = Produto.objects.filter(id__in=ids_produtos)
        cart = self.cart.copy()
        for produto in produtos:
            cart[str(produto.id)]['product'] = produto
        for item in cart.values():
            item['preco'] = Decimal(item['preco'])
            item['preco_total'] = item['preco']* item['quantidade']
            yield item
            
    def __len__(self):
        #Conta todos os items
        return sum(item['quantidade'] for item in self.cart.values())
    
    def get_preco_total(self):
        return sum(Decimal(item['preco'])*item['quantidade'] for item in self.cart.values())
    
    def limpar(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()