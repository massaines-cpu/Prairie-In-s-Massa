const PLUS_BTN = document.getElementById('plus');
//changer plus pour 'Afficher une nouvelle note'
PLUS_BTN.addEventListener('click', Model.addNewNote);

const CALEPIN = document.getElementById('calepin');
//Peut-être l'appeler "Gestionnaire de tâches"
var Control = {
  validateNote: function(event){
    var noteId = event.target.parentNode.id;
    var noteText = event.target.parentNode.childNodes[1].value;
//Mettre un texte grisé pour dire qu'on peut saisir du texte
    Model.closeNote(noteId, noteText);
//Mettre la possibilité de pouvoir revenir sur la note ? Donc de pas la fermer
  }
};