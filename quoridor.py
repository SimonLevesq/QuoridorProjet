import networkx as nx


# TODO: Définissez votre classe QuoridorError ici.


class Quoridor:
    """Classe pour encapsuler le jeu Quoridor.
    Attributes:
        état (dict): état du jeu tenu à jour.
        TODO: Identifiez les autres attribut de votre classe
    Examples:
        >>> q.Quoridor()
    """
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

        """Constructeur de la classe Quoridor.
        Initialise une partie de Quoridor avec les joueurs et les murs spécifiés,
        en s'assurant de faire une copie profonde de tout ce qui a besoin d'être copié.
        Args:
            joueurs (List): un itérable de deux joueurs dont le premier est toujours celui qui
                débute la partie. Un joueur est soit une chaîne de caractères soit un dictionnaire.
                Dans le cas d'une chaîne, il s'agit du nom du joueur. Selon le rang du joueur dans
                l'itérable, sa position est soit (5,1) soit (5,9), et chaque joueur peut
                initialement placer 10 murs. Dans le cas où l'argument est un dictionnaire,
                celui-ci doit contenir une clé 'nom' identifiant le joueur, une clé 'murs'
                spécifiant le nombre de murs qu'il peut encore placer, et une clé 'pos' qui
                spécifie sa position (x, y) actuelle. Notez que les positions peuvent être sous
                forme de tuple (x, y) ou de liste [x, y].
            murs (Dict, optionnel): Un dictionnaire contenant une clé 'horizontaux' associée à
                la liste des positions (x, y) des murs horizontaux, et une clé 'verticaux'
                associée à la liste des positions (x, y) des murs verticaux. Par défaut, il
                n'y a aucun mur placé sur le jeu. Notez que les positions peuvent être sous
                forme de tuple (x, y) ou de liste [x, y].
        Raises:
            QuoridorError: L'argument 'joueurs' n'est pas itérable.
            QuoridorError: L'itérable de joueurs en contient un nombre différent de deux.
            QuoridorError: Le nombre de murs qu'un joueur peut placer est plus grand que 10,
                            ou négatif.
            QuoridorError: La position d'un joueur est invalide.
            QuoridorError: L'argument 'murs' n'est pas un dictionnaire lorsque présent.
            QuoridorError: Le total des murs placés et plaçables n'est pas égal à 20.
            QuoridorError: La position d'un mur est invalide.
        """
        pass

    def __str__(self):
        """Représentation en art ascii de l'état actuel de la partie.
        Cette représentation est la même que celle du projet précédent.
        Returns:
            str: La chaîne de caractères de la représentation.
        """
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

        pass

    def déplacer_jeton(self, joueur, position):
        """Déplace un jeton.
        Pour le joueur spécifié, déplacer son jeton à la position spécifiée.
        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).
            position (Tuple[int, int]): Le tuple (x, y) de la position du jeton (1<=x<=9 et 1<=y<=9).
        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: La position est invalide (en dehors du damier).
            QuoridorError: La position est invalide pour l'état actuel du jeu.
        """
        if joueur > 2 or joueur < 1:
            raise QuoridorError("Le numéro du joueur est autre que 1 ou 2.")
        if position[0] > 9 or position[0] < 1 or position[1] > 9 or position[1] < 1:
            raise QuoridorError("La position est invalide (en dehors du damier).")
        if abs(position[0] - self.joueurs[joueur-1]['pos'][0]) > 1 or abs(position[1] - self.joueurs[joueur-1]['pos'][1]) > 1:
            raise QuoridorError("La position est invalide pour l'état actuel du jeu.")
        else:
            self.joueurs[joueur-1]['pos'] =  position
        pass

    def état_partie(self):
        """Produire l'état actuel de la partie.
        Returns:
            Dict: Une copie de l'état actuel du jeu sous la forme d'un dictionnaire.
                  Notez que les positions doivent être sous forme de tuple (x, y) uniquement.
        Examples:
            {
                'joueurs': [
                    {'nom': nom1, 'murs': n1, 'pos': (x1, y1)},
                    {'nom': nom2, 'murs': n2, 'pos': (x2, y2)},
                ],
                'murs': {
                    'horizontaux': [...],
                    'verticaux': [...],
                }
            }
            où la clé 'nom' d'un joueur est associée à son nom, la clé 'murs' est associée
            au nombre de murs qu'il peut encore placer sur ce damier, et la clé 'pos' est
            associée à sa position sur le damier. Une position est représentée par un tuple
            de deux coordonnées x et y, où 1<=x<=9 et 1<=y<=9.
            Les murs actuellement placés sur le damier sont énumérés dans deux listes de
            positions (x, y). Les murs ont toujours une longueur de 2 cases et leur position
            est relative à leur coin inférieur gauche. Par convention, un mur horizontal se
            situe entre les lignes y-1 et y, et bloque les colonnes x et x+1. De même, un
            mur vertical se situe entre les colonnes x-1 et x, et bloque les lignes y et y+1.
        """
        return {'joueurs': self.joueurs, 'murs': self.murs}        
        pass

    def jouer_coup(self, joueur):
        self.joueur = joueur
        if self.joueur != 1 or self.joueur != 2:
            raise QuoridorError('Le numéro du joueur est autre que 1 ou 2.')
        if partie_terminée:
            raise QuoridorError('La partie est déjà terminée.')
        x = self.joueur[0]['pos'][0]
        X = self.joueur[1]['pos'][0]
        y = self.joueur[0]['pos'][1]
        Y = self.joueur[1]['pos'][1]

        if (9-y) > Y:
            déplacer_jeton(self, joueur[0], (x, y+1)
            return ('déplacer jeton', (x+1, y))
        
        if y == Y:
            placer_mur(self, joueur[0], (X+1, Y), horizontal)
            return ('placer mur horizontal', (X+1, Y))
        
        if y < Y:
            placer_mur(self, joueur[0], (X-1, Y-1), vertical)
            return ('placer mur vertical', (X-1, Y-1))

        """Jouer un coup automatique pour un joueur.
        Pour le joueur spécifié, jouer automatiquement son meilleur coup pour l'état actuel
        de la partie. Ce coup est soit le déplacement de son jeton, soit le placement d'un
        mur horizontal ou vertical.
        Args:
            joueur (int): Un entier spécifiant le numéro du joueur (1 ou 2).
        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: La partie est déjà terminée.
            
        Returns:
            Tuple[str, Tuple[int, int]]: Un tuple composé du type et de la position du coup joué.
        """
        pass

    def partie_terminée(self):
        y1 = joueurs[0]['pos'][1]
        y2 = joueurs[1]['pos'][1]

        if (9-y1) > y2 and y1 == 9:
            return (True, joueurs[0]['nom'])

        if (9-y1) < y2 and y2 == 1:
            return(True, joueurs[1]['nom'])
        
        else:
            return False


        Returns:
            str/bool: Le nom du gagnant si la partie est terminée; False autrement.
        """
        pass

    def placer_mur(self, joueur, position, orientation):
        """Placer un mur.
        Pour le joueur spécifié, placer un mur à la position spécifiée.
        Args:
            joueur (int): le numéro du joueur (1 ou 2).
            position (Tuple[int, int]): le tuple (x, y) de la position du mur.
            orientation (str): l'orientation du mur ('horizontal' ou 'vertical').
        Raises:
            QuoridorError: Le numéro du joueur est autre que 1 ou 2.
            QuoridorError: Un mur occupe déjà cette position.
            QuoridorError: La position est invalide pour cette orientation.
            QuoridorError: Le joueur a déjà placé tous ses murs.
        """
        pass


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