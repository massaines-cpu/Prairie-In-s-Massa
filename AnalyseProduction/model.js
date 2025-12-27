var Model = {
  notes: [],
  addNewNote: function (){
    var newNote = {
      id: Model.notes.length,
      content: ""
//ici on peut intégrer un texte grisé qui dit qu'on peut écrire
    };
    Model.notes.push(newNote);
    View.addNote(newNote);
  },
  closeNote: function(id, text){
    Model.notes[id].content = text;
//mieux définir id
    View.disableNote(Model.notes[id]);
  }
};