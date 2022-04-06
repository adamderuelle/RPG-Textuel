class Joueur():
    def __init__(self, nom, pv, pm, position, classe):
        self.nom = nom
        self.pv = pv
        self.pm = pm
        self.classe = classe
        self.effets = []
        self.competences = {"coup de poing":{"degats":10, "cout":0}}
        self.position = position
        self.fin_partie = False

    def perdre_pv(self, degats):
        self.pv -= degats
    
    def perdre_pm(self, montant):
        self.pm -= montant
    
    def set_pv(self,pv):
        self.pv = pv
    
    def set_pm(self,pm):
        self.pm = pm
        
    def add_effets(self, effet):
        self.effets.append(effet)
        
    def set_position(self, nouvelle_position):
        self.position = nouvelle_position
        
    def get_pv(self):
        return self.pv
    
    def get_pm(self):
        return self.pm
    
    def get_effets(self):
        return self.effets
    
    def get_position(self):
        return self.position
    
    def get_etat_partie(self):
        return self.fin_partie
    
    def get_classe(self):
        return self.classe
    
    def get_nom(self):
        return self.nom
    
class Classe():
    def __init__(self,nom_classe):
        self.nom = nom_classe
        self.competences = {"coup de poing":{"degats":10, "cout":0}}
        
    def get_nom(self):
        return self.nom
    
    def get_competences(self):
        return self.competences
    
    def get_competence(self, nom_competence):
        return self.competences[nom_competence]


def temp():
    t = {
        "guerrier":{"hache tournouyante":{"degats": 30, "cout":5}, "lancer de hache":{"degats":25, "cout":5}},
        "prêtre":{"soins":{"degats": 3, "cout":10, "sante":10}, "rayon de lumiére":{"degats": 35, "cout":7}},
        "magicien":{"boule de feu":{"degats": 30, "cout":5}, "rayon d'énergie":{"degats": 40, "cout":20}},
        "nécromencien":{"extraction":{}},
    }
    return t   
class Necromencien(Classe):
    
    def __init__(self, nom_classe = "nécromencien"):
        super().__init__(nom_classe)
        self.competences = {"emprisonnement":{"degats": 40, "cout":60}}
        self.armee_des_morts = {"squellete goblin":{"degats": 10, "pv":10}}
        
class Guerrier(Classe):
    
    def __init__(self, nom_classe = "guerrier"):
        super().__init__(nom_classe)
        self.competences = {"hache tournouyante":{"degats": 30, "cout":5}, "lancer de hache":{"degats":25, "cout":5}}

class Pretre(Classe):
    def __init__(self, nom_classe = "prêtre"):
        super().__init__(nom_classe)
        self.competences = {"soins":{"degats": 3, "cout":10, "sante":10}, "rayon de lumiére":{"degats": 35, "cout":7}}
        
