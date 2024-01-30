from .cart import Cart

def cart(request):
    nome_usuario = None
    if request.user.is_authenticated:
        nome_usuario = request.user.email.split('@')[0]
    return {
        'cart': Cart(request        ),
        'nome_usuario': nome_usuario,
        }