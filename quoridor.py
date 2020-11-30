import networkx as nx


class QuoridorError(Exception):
    pass


class Quoridor:
    def __init__(self, joueurs, murs=None):
        self.joueurs = joueurs
        self.murs = murs

        def itérable(obj):
            try:
                iter(obj)
                return True
            except TypeError:
                return False
    
        if itérable(self.joueurs) is False:
            raise QuoridorError("L'argument 'joueurs' n'est pas itérable.")
        
        if len(self.joueurs) > 2:
            raise QuoridorError("L'itérable de joueurs en contient un nombre différent de deux.")
        
        if type(self.joueurs) is dict and self.murs != None:

            if self.joueurs[0]['murs'] > 10 or self.joueurs[1]['murs'] > 10 or self.joueurs[0]['murs'] < 0 or self.joueurs[1]['murs'] < 0:
                raise QuoridorError("Le nombre de murs qu'un joueur peut placer est plus grand que 10, ou négatif.")
        
            if self.joueurs[0]['pos'][0] < 1 or self.joueurs[0]['pos'][1] < 1 or self.joueurs[0]['pos'][0] > 9 or self.joueurs[0]['pos'][1] > 9:
                raise QuoridorError("La position d'un joueur est invalide.")
        
            if self.joueurs[1]['pos'][0] < 1 or self.joueurs[1]['pos'][1] < 1 or self.joueurs[1]['pos'][0] > 9 or self.joueurs[1]['pos'][1] > 9:
                raise QuoridorError("La position d'un joueur est invalide.")
        
            if type(self.murs) is not dict:
                raise QuoridorError("L'argument 'murs' n'est pas un dictionnaire lorsque présent.")
        
            if self.joueurs[0]['murs'] + self.joueurs[1]['murs'] + len(self.murs['horizontaux']) + len(self.murs['verticaux']) != 20:
                raise QuoridorError("Le total des murs placés et plaçables n'est pas égal à 20.")
        
            for i in self.murs['horizontaux']:
                if i[0] < 1 or i[0] > 9:
                    raise QuoridorError("La position d'un mur est invalide.")
                if i[1] < 1 or i[1] > 9:
                    raise QuoridorError("La position d'un mur est invalide.")
        
            for i in self.murs['horizontaux']:
                if i[0] < 1 or i[0] > 9:
                    raise QuoridorError("La position d'un mur est invalide.")
                if i[1] < 1 or i[1] > 9:
                    raise QuoridorError("La position d'un mur est invalide.")
        else:
            self.joueurs = [{'nom': joueurs[0], 'murs': 10, 'pos': (5,1)}, {'nom': joueurs[1], 'murs': 10, 'pos': (5,9)}]
            self.murs = {'horizontaux': [], 'verticaux': []}

    def __str__(self):
        top = '   ' + '-'*35 + ' \n'
        bas = '--|' + '-'*35 + ' \n' + '  | 1   2   3   4   5   6   7   8   9  '

        #Magnifique bloc
        dam = [['9 |', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', '|',
               '\n  |', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', '|\n'],
                ['8 |', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', '|',
                '\n  |', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', '|\n'],
                 ['7 |', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', '|',
                 '\n  |', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', '|\n'],
                  ['6 |', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', '|',
                  '\n  |', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', '|\n'],
                   ['5 |', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', '|',
                    '\n  |', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', '|\n'],
                    ['4 |', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', '|',
                    '\n  |', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', '|\n'],
                     ['3 |', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', '|',
                     '\n  |', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', '|\n'],
                      ['2 |', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', '|',
                      '\n  |', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', ' ', '   ', '|\n'],
                       ['1 |', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', ' ', ' . ', '|\n']]
  
        #Legende
        nom1 = self.joueurs[0]['nom']
        nom2 = self.joueurs[1]['nom']
        def legende_joueur(nom1, nom2):
            if len(nom1) > len(nom2):
                leg = (f'Légende:\n   1={nom1}, murs=' + '|'*(self.joueurs[0]['murs'])
                           + f'\n   2={nom2},' + ' '*(len(nom1)-len(nom2)+1) +'murs=' + '|'*(self.joueurs[1]['murs']) + '\n')
            else:
                leg = (f'Légende:\n   1={nom1},' + ' '*(len(nom2)-len(nom1)+1) + 'murs=' + '|'*(self.joueurs[0]['murs'])
                           + f'\n   2={nom2}, murs=' + '|'*(self.joueurs[1]['murs']) + '\n')
            return leg

        #position1
        pox1 = self.joueurs[0]['pos'][0]
        poy1 = self.joueurs[0]['pos'][1]
        dam[-poy1][pox1 + (pox1 - 1)] = ' 1 '
    
        #position2
        pox2 = self.joueurs[1]['pos'][0]
        poy2 = self.joueurs[1]['pos'][1]
        dam[-poy2][pox2 + (pox2 - 1)] = ' 2 '

        #mursV
        murv = self.murs['verticaux']
        listmurv = range(len(murv))
        for i in listmurv:
            dam[-(murv[i][1])][murv[i][0]*2 - 2] = '|'
            dam[-(murv[i][1]+1)][murv[i][0]*2 - 2] = '|'
            dam[-(murv[i][1]+1)][murv[i][0]*2 + 17] = '|'

        #murH
        murh = self.murs['horizontaux']
        listmurh = range(len(murh))
        for j in listmurh:
            dam[-(murh[j][1])][murh[j][0]*2 + 18] = '---'
            dam[-(murh[j][1])][murh[j][0]*2 + 19] = '-'
            dam[-(murh[j][1])][murh[j][0]*2 + 20] = '---'

        joinall = (
                  (''.join(dam[0])) + (''.join(dam[1])) + (''.join(dam[2])) + (''.join(dam[3])) +
                  (''.join(dam[4])) + (''.join(dam[5])) + (''.join(dam[6])) + (''.join(dam[7])) + (''.join(dam[8]))
                    )
        return legende_joueur(nom1, nom2) + top + joinall + bas

    def déplacer_jeton(self, joueur, position):
        posjoueur = self.joueurs[joueur-1]['pos']

        if joueur > 2 or joueur < 1:
            raise QuoridorError("Le numéro du joueur est autre que 1 ou 2.")
        
        if position[0] > 9 or position[0] < 1 or position[1] > 9 or position[1] < 1:
            raise QuoridorError("La position est invalide (en dehors du damier).")
        
        if abs(position[0] - posjoueur[0]) > 1 or abs(position[1] - posjoueur[1]) > 1:
            raise QuoridorError("La position est invalide pour l'état actuel du jeu.")
        
        if position == self.joueurs[0]['pos'] or position == self.joueurs[1]['pos']:
            raise QuoridorError("La position est invalide pour l'état actuel du jeu.")
        
        for i in self.murs['horizontaux']: 
            if (posjoueur[0] == i[0] or posjoueur[0] == i[0]+1) and (posjoueur[1] == i[1]-1) and position[1] == i[1]:
                raise QuoridorError("La position est invalide pour l'état actuel du jeu.")
            if (posjoueur[0] == i[0] or posjoueur[0] == i[0]+1) and (posjoueur[1] == i[1]) and position[1] == i[1]-1:
                raise QuoridorError("La position est invalide pour l'état actuel du jeu.")

        for i in self.murs['verticaux']: 
            if (posjoueur[1] == i[1] or posjoueur[1] == i[1]+1) and (posjoueur[0] == i[0]-1) and position[0] == i[0]:
                raise QuoridorError("La position est invalide pour l'état actuel du jeu.")
            if (posjoueur[1] == i[1] or posjoueur[1] == i[1]+1) and (posjoueur[0] == i[0]) and (position[0] == i[0]-1):
                raise QuoridorError("La position est invalide pour l'état actuel du jeu.")
  
        else:
            self.joueurs[joueur-1]['pos'] =  position

    def état_partie(self):
        return {'joueurs': self.joueurs, 'murs': self.murs}

    def jouer_coup(self, joueur):
        if joueur < 1 or joueur > 2:
            raise QuoridorError('Le numéro du joueur est autre que 1 ou 2.')
        if Quoridor.partie_terminée(self):
            raise QuoridorError('La partie est déjà terminée.')
        x = self.joueurs[0]['pos'][0]
        X = self.joueurs[1]['pos'][0]
        y = self.joueurs[0]['pos'][1]
        Y = self.joueurs[1]['pos'][1]

        if (9-y) > Y:
            for i in self.murs['horizontaux']:
                if (i[0] == x or i[0] == x-1) and (i[1] == y+1):
                    Quoridor.déplacer_jeton(self, joueur, (x+1, y))
                    return ('déplacer jeton', (x+1, y))
                
            for i in self.murs['verticaux']:
                if (i[0] == x-1) and (i[1] == y+1):
                    Quoridor.déplacer_jeton(self, joueur, (x+1, y))
                    return ('déplacer jeton', (x+1, y))

            Quoridor.déplacer_jeton(self, joueur, (x, y+1))
            return ('déplacer jeton', (x, y+1))
        
        if y <= Y:
            Quoridor.placer_mur(self, joueur, (X-1, Y-1), 'vertical')
            return ('placer mur vertical', (X-1, Y-1))

    def partie_terminée(self):
        y1 = self.joueurs[0]['pos'][1]
        y2 = self.joueurs[1]['pos'][1]

        if y1 == 9:
            return (self.joueurs[0]['nom'])

        if y2 == 1:
            return (self.joueurs[1]['nom'])
        
        else:
            return False

    def placer_mur(self, joueur, position, orientation):
        if joueur > 2 or joueur < 1:
            raise QuoridorError("Le numéro du joueur est autre que 1 ou 2.")

        for i in self.murs['horizontaux']:
            if orientation == 'horizontal' and (i[0] == position[0] and (i[1] == position[1] or i[1] == position[1]+1 or i[1] == position[1]-1)):
                raise QuoridorError("Un mur occupe déjà cette position.")
            if orientation == 'vertical' and (i[0]-1 == position[0] and i[1]+1 == position[1]):
                raise QuoridorError("Un mur occupe déjà cette position.")

        for i in self.murs['verticaux']:
            if orientation == 'vertical' and (i[1] == position[1] and (i[0] == position[0] or i[0] == position[0]+1 or i[0] == position[0]-1)):
                raise QuoridorError("Un mur occupe déjà cette position.")
            if orientation == 'horizontal' and (i[0]+1 == position[0] and i[1]-1 == position[1]):
                raise QuoridorError("Un mur occupe déjà cette position.")

        if (orientation == 'horizontal' and (position[0] >= 9 or position[1] <= 1)):
            raise QuoridorError("La position est invalide pour cette orientation.")
        
        if (orientation == 'vertical' and (position[1] >= 9 or position[1] <= 1)):
            raise QuoridorError("La position est invalide pour cette orientation.")
        
        if position[0] < 1 or position[1] < 1 or position[0] > 9 or position[1] > 9:
            raise QuoridorError("La position est invalide pour cette orientation.")

        if self.joueurs[joueur-1]['murs'] == 0:
            raise QuoridorError("Le joueur a déjà placé tous ses murs.")
        
        else:
            self.joueurs[joueur-1]['murs'] -= 1
            if orientation =='horizontal':
                self.murs['horizontaux'].append(position)
            else:
                self.murs['verticaux'].append(position)

def construire_graphe(joueurs, murs_horizontaux, murs_verticaux):
    """Construire un graphe de la grille.
    Crée le graphe des déplacements admissibles pour les joueurs.
    Vous n'avez pas à modifer cette fonction.
    Args:
        joueurs (List[Tuple]): une liste des positions (x,y) des joueurs.
        murs_horizontaux (List[Tuple]): une liste des positions (x,y) des murs horizontaux.
        murs_verticaux (List[Tuple]): une liste des positions (x,y) des murs verticaux.
    Returns:
        DiGraph: le graphe bidirectionnel (en networkX) des déplacements admissibles.
    """
    graphe = nx.DiGraph()

    # pour chaque colonne du damier
    for x in range(1, 10):
        # pour chaque ligne du damier
        for y in range(1, 10):
            # ajouter les arcs de tous les déplacements possibles pour cette tuile
            if x > 1:
                graphe.add_edge((x, y), (x-1, y))
            if x < 9:
                graphe.add_edge((x, y), (x+1, y))
            if y > 1:
                graphe.add_edge((x, y), (x, y-1))
            if y < 9:
                graphe.add_edge((x, y), (x, y+1))

    # retirer tous les arcs qui croisent les murs horizontaux
    for x, y in murs_horizontaux:
        graphe.remove_edge((x, y-1), (x, y))
        graphe.remove_edge((x, y), (x, y-1))
        graphe.remove_edge((x+1, y-1), (x+1, y))
        graphe.remove_edge((x+1, y), (x+1, y-1))

    # retirer tous les arcs qui croisent les murs verticaux
    for x, y in murs_verticaux:
        graphe.remove_edge((x-1, y), (x, y))
        graphe.remove_edge((x, y), (x-1, y))
        graphe.remove_edge((x-1, y+1), (x, y+1))
        graphe.remove_edge((x, y+1), (x-1, y+1))

    # s'assurer que les positions des joueurs sont bien des tuples (et non des listes)
    j1, j2 = tuple(joueurs[0]), tuple(joueurs[1])

    # traiter le cas des joueurs adjacents
    if j2 in graphe.successors(j1) or j1 in graphe.successors(j2):

        # retirer les liens entre les joueurs
        graphe.remove_edge(j1, j2)
        graphe.remove_edge(j2, j1)

        def ajouter_lien_sauteur(noeud, voisin):
            """
            :param noeud: noeud de départ du lien.
            :param voisin: voisin par dessus lequel il faut sauter.
            """
            saut = 2*voisin[0]-noeud[0], 2*voisin[1]-noeud[1]

            if saut in graphe.successors(voisin):
                # ajouter le saut en ligne droite
                graphe.add_edge(noeud, saut)

            else:
                # ajouter les sauts en diagonale
                for saut in graphe.successors(voisin):
                    graphe.add_edge(noeud, saut)

        ajouter_lien_sauteur(j1, j2)
        ajouter_lien_sauteur(j2, j1)

    # ajouter les destinations finales des joueurs
    for x in range(1, 10):
        graphe.add_edge((x, 9), 'B1')
        graphe.add_edge((x, 1), 'B2')

    return graphe