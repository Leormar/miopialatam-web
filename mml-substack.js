// Suscripcion al boletin Vision MML LATAM en Substack
function mmlSubstack(form){
  var campo = form.querySelector('input[type=email]');
  var correo = (campo && campo.value || '').trim();
  var url = 'https://grupomiopialatam.substack.com/subscribe?utm_source=miopialatam.org&utm_medium=web';
  if (correo) { url += '&email=' + encodeURIComponent(correo); }
  window.open(url, '_blank', 'noopener');
  return false;
}
