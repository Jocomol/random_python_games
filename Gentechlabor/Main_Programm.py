'''
Created on 30.11.2016

@author: Berufsbildungcenter AG
'''
from Rose import Rose
from Moskito import Moskito
from Fleischfresserpflanze import Fleischfresserpflanze

rose = Rose("Rosi", "Rot", 1, 7)
rose.wachsen()
rose.wasserGeben(2)
rose.wachsen()
rose.wasserGeben(1)
rose.wachsen()


fleischfresser = Fleischfresserpflanze("Regenbogenpflanze", "Grün", 1, 7)
fleischfresser.wachsen()
fleischfresser.wasserGeben(1000)
fleischfresser.fuettern(Moskito(3))
fleischfresser.wachsen()
fleischfresser.fuettern(Moskito(10))
fleischfresser.wachsen()
fleischfresser.wachsen()
fleischfresser.wachsen()
fleischfresser.wachsen()
fleischfresser.fuettern(Moskito(2))
