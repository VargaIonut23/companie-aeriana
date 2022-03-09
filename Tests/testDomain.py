from Domain.rezervare import getcheckin, getpret, getclasa, getnume, getId, creeazarezervare


def testRezervare():
    rezervare = creeazarezervare('213#' , 'Ionut' , 'economy' , 317.78 , 'da')
    assert getId(rezervare) == '213#'
    assert getnume(rezervare) == 'Ionut'
    assert getclasa(rezervare) == 'economy'
    assert getpret(rezervare) == 317.78
    assert getcheckin(rezervare) == 'da'

