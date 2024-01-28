from django import forms

class CadastroForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control my-1'}))
    nome = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-1'}))
    cep = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control my-1'}))
    endereco = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-1'}))
    telefone = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control my-1'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-1'}))
    confirme = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-1'}), label='Confirme a senha')
   
class LoginForm():
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))