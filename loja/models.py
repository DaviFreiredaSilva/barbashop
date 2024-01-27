from django.db import models
from django.urls import reverse

class Categoria(models.Model):
    nome = models.CharField(max_length = 200)
    slug = models.SlugField(max_length = 200, unique =True)
    
    class Meta:
        ordering = ['nome']
        indexes = [
            models.Index(fields=['nome']),
        ]
        verbose_name='categoria'
        verbose_name_plural='categorias'
        
    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('loja:produto_por_categoria', args=[self.slug])

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='produtos',null=True, on_delete =models.SET_NULL )
    nome = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100)
    descricao =  models.CharField(max_length = 300, blank=True, default="Sem descrição.")
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='media/', blank=True, null=True)
    available = models.BooleanField(default= True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ['nome']
        indexes = [
            models.Index(fields=['id', 'slug'])
        ]
    
    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('loja:detalhe_produto', args=[self.id, self.slug])
    