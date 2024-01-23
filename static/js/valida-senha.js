let senha = document.getElementById('id_senha');
let confirme = document.getElementById('id_confirme');

function validarSenha() {
  if (senha.value != confirme.value) {
    confirme.setCustomValidity("Senhas diferentes!");
    confirme.reportValidity();
    return false;
  } else {
    confirme.setCustomValidity("");
    return true;
  }
}

// verificar também quando o campo for modificado, para que a mensagem suma quando as senhas forem iguais
confirme.addEventListener('input', validarSenha);