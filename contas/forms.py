from django import forms

class CadastroForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    nome = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    cep = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    endereco = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    telefone = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    confirme = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}), label='Confirme a senha')
   
class LoginForm():
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))