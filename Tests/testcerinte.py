from Domain.rezervare import getpret, getclasa, getId
from Logic.CRUD import adaugarezervare, getbyid
from Logic.cerinte import cerinta4, cerinta5, cerinta6economy, cerinta6economyplus, cerinta6business, cerinta7, cerinta8



def testcerinta4():
    lista = []
    lista = adaugarezervare("1", "Ionut", "economy", 317.78, "da", lista)
    lista = adaugarezervare("2", "Denis", "business", 1119.90, "nu", lista)
    lista = adaugarezervare("3", "Robert", "economy plus", 890.02, "da", lista)
    lista = cerinta4(lista, 'Ionut')
    assert getclasa(getbyid("1", lista)) == "economy plus"
    assert getclasa(getbyid("2", lista)) == "business"
    assert getclasa(getbyid("3", lista)) == "economy plus"
    lista = cerinta4(lista, 'Robert')
    assert getclasa(getbyid("1", lista)) == "economy plus"
    assert getclasa(getbyid("2", lista)) == "business"
    assert getclasa(getbyid("3", lista)) == "business"
    lista = cerinta4(lista, 'Denis')
    assert getclasa(getbyid("1", lista)) == "economy plus"
    assert getclasa(getbyid("2", lista)) == "business"
    assert getclasa(getbyid("3", lista)) == "business"

def testcerinta5():
    lista = []
    lista = adaugarezervare("1", "Ionut", "economy", 100, "da", lista)
    lista = adaugarezervare("2", "Denis", "business", 1119.90, "nu", lista)
    lista = adaugarezervare("3", "Robert", "economy plus", 1000, "da", lista)
    lista = cerinta5(lista , 20)
    assert getpret(getbyid("1", lista)) == 80.0
    assert getpret(getbyid("2", lista)) == 1119.90
    assert getpret(getbyid("3", lista)) == 800.0

def testcerinta6economy():
    lista = []
    lista = adaugarezervare("1", "Ionut", "economy", 317.78, "da", lista)
    lista = adaugarezervare("2", "Denis", "business", 1119.90, "nu", lista)
    lista = adaugarezervare("3", "Robert", "economy plus", 890.02, "da", lista)
    lista = adaugarezervare("4", "Ionut", "economy", 1078, "da", lista)
    lista = adaugarezervare("5", "Denis", "business", 800, "nu", lista)
    lista = adaugarezervare("6", "Robert", "economy plus", 1067, "da", lista)
    assert cerinta6economy(lista) == 1078

def testcerinta6economyplus():
    lista = []
    lista = adaugarezervare("1", "Ionut", "economy", 317.78, "da", lista)
    lista = adaugarezervare("2", "Denis", "business", 1119.90, "nu", lista)
    lista = adaugarezervare("3", "Robert", "economy plus", 890.02, "da", lista)
    lista = adaugarezervare("4", "Ionut", "economy", 1078, "da", lista)
    lista = adaugarezervare("5", "Denis", "business", 800, "nu", lista)
    lista = adaugarezervare("6", "Robert", "economy plus", 1067, "da", lista)
    assert cerinta6economyplus(lista) == 1067

def testcerinta6business():
    lista = []
    lista = adaugarezervare("1", "Ionut", "economy", 317.78, "da", lista)
    lista = adaugarezervare("2", "Denis", "business", 1119.90, "nu", lista)
    lista = adaugarezervare("3", "Robert", "economy plus", 890.02, "da", lista)
    lista = adaugarezervare("4", "Ionut", "economy", 1078, "da", lista)
    lista = adaugarezervare("5", "Denis", "business", 800, "nu", lista)
    lista = adaugarezervare("6", "Robert", "economy plus", 1067, "da", lista)
    assert cerinta6business(lista) == 1119.90

def testcerinta7():
    lista = []
    lista = adaugarezervare("1", "Ionut", "economy", 317.78, "da", lista)
    lista = adaugarezervare("2", "Denis", "business", 1119.90, "nu", lista)
    lista = adaugarezervare("3", "Robert", "economy plus", 890.02, "da", lista)
    lista = adaugarezervare("4", "Ionut", "economy", 1078, "da", lista)
    lista = adaugarezervare("5", "Denis", "business", 800, "nu", lista)
    lista = adaugarezervare("6", "Robert", "economy plus", 1067, "da", lista)

    rezultat = cerinta7(lista)

    assert getId(rezultat[0]) == "2"
    assert getId(rezultat[1]) == "4"
    assert getId(rezultat[2]) == "6"
    assert getId(rezultat[3]) == "3"
    assert getId(rezultat[4]) == "5"
    assert getId(rezultat[5]) == "1"

def testcerinta8():
    lista = []
    lista = adaugarezervare("1", "Ionut", "economy", 100, "da", lista)
    lista = adaugarezervare("2", "Ionut", "business", 100, "nu", lista)
    lista = adaugarezervare("3", "Robert", "economy plus", 200, "da", lista)
    lista = adaugarezervare("4", "Ionut", "economy", 100, "da", lista)
    lista = adaugarezervare("5", "Robert", "business", 800, "nu", lista)
    lista = adaugarezervare("6", "Robert", "economy plus", 200, "da", lista)

    rezultat = cerinta8(lista)
    assert len(rezultat) == 2
    assert rezultat['Ionut'] == 300
    assert rezultat['Robert'] == 1200


