let novaSenha1 = document.getElementById('id_new_password1');
let novaSenha2 = document.getElementById('id_new_password2');

function validarSenha() {
   
  //Confirmação de senha  
  if (novaSenha1.value != novaSenha2.value) {
    novaSenha2.setCustomValidity("Senhas diferentes.");
    novaSenha2.reportValidity();
    return false;
  } else {
    novaSenha2.setCustomValidity("");
    return true;
  }

}

function tamanhoDaSenha(){
    if(novaSenha1.value.length < 8){
        novaSenha1.setCustomValidity("Senha muito curta.");
        novaSenha1.reportValidity();
        return false;
       }else{
        novaSenha1.setCustomValidity("");
        return true;
       } 
}

// verificar também quando o campo for modificado, para que a mensagem suma quando as senhas forem iguais
novaSenha2.addEventListener('input', validarSenha);
novaSenha1.addEventListener('input', tamanhoDaSenha);