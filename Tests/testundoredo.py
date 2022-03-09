from Logic.CRUD import adaugaRezervareUndoRedo
from Logic.cerinte import Undo, Redo


def testUndoRedo():
    lista=[]
    undo=[]
    redo=[]
    lista = adaugaRezervareUndoRedo("1", "Ionut", "economy", 100, "da", lista,undo,redo)
    assert lista == [{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]
    lista = adaugaRezervareUndoRedo("2", "Denis", "economy", 100, "da", lista,undo,redo)
    assert lista == [{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}, {'id': '2', 'nume': 'Denis', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]
    lista = adaugaRezervareUndoRedo("3", "Robert", "economy", 100, "da", lista, undo, redo)
    assert lista==[{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}, {'id': '2', 'nume': 'Denis', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}, {'id': '3', 'nume': 'Robert', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]
    assert len(lista) == 3
    lista=Undo(lista,undo,redo)
    assert lista==[{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}, {'id': '2', 'nume': 'Denis', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]
    assert len(lista) == 2
    lista=Undo(lista,undo,redo)
    assert lista==[{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]
    assert len(lista) == 1
    lista = Undo(lista, undo, redo)
    assert lista ==[]
    assert len(lista) == 0
    lista = Undo(lista, undo, redo)
    assert lista is None
    undo=[]
    redo=[]
    lista=[]
    lista = adaugaRezervareUndoRedo("1", "Ionut", "economy", 100, "da", lista,undo,redo)
    assert lista == [{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]
    lista = adaugaRezervareUndoRedo("2", "Denis", "economy", 100, "da", lista,undo,redo)
    assert lista == [{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'},
                    {'id': '2', 'nume': 'Denis', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]
    lista = adaugaRezervareUndoRedo("3", "Robert", "economy", 100, "da", lista, undo, redo)
    [{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'},
     {'id': '2', 'nume': 'Denis', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'},
     {'id': '3', 'nume': 'Robert', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]
    lista=Redo(lista,undo,redo)
    assert lista==[{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}, {'id': '2', 'nume': 'Denis', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}, {'id': '3', 'nume': 'Robert', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]
    assert len(lista) == 3
    lista = Undo(lista, undo, redo)
    assert lista == [{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'},
                     {'id': '2', 'nume': 'Denis', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]
    lista=Undo(lista,undo,redo)
    assert lista==[{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]
    assert len(lista) == 1
    lista=Redo(lista,undo,redo)
    assert lista==[{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}, {'id': '2', 'nume': 'Denis', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]
    assert len(lista) == 2
    lista = Redo(lista, undo, redo)
    assert lista == [{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}, {'id': '2', 'nume': 'Denis', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}, {'id': '3', 'nume': 'Robert', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]
    assert len(lista) == 3
    lista = Undo(lista, undo, redo)
    lista = Undo(lista, undo, redo)
    lista=adaugaRezervareUndoRedo("4", "Razvan", "economy", 100.00, "da", lista, undo, redo)
    assert lista==[{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'},
                   {'id': '4', 'nume': 'Razvan', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]
    lista=Redo(lista,undo,redo)
    assert lista == [{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'},
                     {'id': '4', 'nume': 'Razvan', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]
    lista = Undo(lista, undo, redo)
    assert lista == [{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]
    lista = Undo(lista, undo, redo)
    assert lista == []
    lista=Redo(lista,undo,redo)
    lista=Redo(lista,undo,redo)
    assert lista == [{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'},
                     {'id': '4', 'nume': 'Razvan', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]
    lista=Redo(lista,undo,redo)
    assert lista == [{'id': '1', 'nume': 'Ionut', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'},
                     {'id': '4', 'nume': 'Razvan', 'clasa': 'economy', 'pret': 100.00, 'checkin': 'da'}]