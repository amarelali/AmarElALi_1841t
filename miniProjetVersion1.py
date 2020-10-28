class Etudiant:
    def __init__(self, numeroEtudiant , premomEtudiant , nomEtudiant ,niveauEtudiant):
        self.numeroEtudiant = numeroEtudiant
        self.premomEtudiant = premomEtudiant
        self.nomEtudiant = nomEtudiant
        self.niveauEtudiant = niveauEtudiant
class Cour:
    def __init__(self, codeCours , intituleCours , niveauCours):
        self.codeCours = codeCours
        self.intituleCours = intituleCours
        self.niveauCours = niveauCours
class Note:
    def __init__(self, numeroEtudiant , codeCours , note):
        self.numeroEtudiant = numeroEtudiant
        self.codeCours = codeCours
        self.note = note
class DB:
    def __init__(self):
        self.etudiant = []
        self.cours = []
        self.note = []

    def insertEtudiant(self, x):
        self.etudiant.append(x)

    def insertCours(self, x):
        self.cours.append(x)

    def insertNote(self, x):
        self.note.append(x)
def test(dbEtudiant,dbCours,note):
    for obj in dbEtudiant:
        
        if obj.numeroEtudiant == note.numeroEtudiant : #etudiant exist
            test1 =True
       

    for obj in dbCours:        
        if obj.codeCours == note.codeCours : #cour exist
            
            test2 =True
        

    if test1 == True and test2 == True :
        return True
def moyenneClass(dbEtudiant , dbNote):
    moyenne = 0
    for note in dbNote:
        moyenne += int(note.note)
    
    return moyenne / len(dbNote)
def moyenneEtudiant(etudiant , dbNote):
    moyenne = 0
    compteur = 0
    for note in dbNote:
        if note.numeroEtudiant == etudiant.numeroEtudiant :
            compteur+=1
            moyenne += int(note.note) 
            
    
    return moyenne / compteur
def consulter(moyenne):
    if moyenne < 20 and moyenne > 18:
        return "Ex"
    elif moyenne < 18 and moyenne > 15:
        return "T.B."
    elif moyenne < 15 and moyenne > 12:
        return "A.B."
    else:
        return "-"    


def main():
    # ajouter 2 etudiant ds data base
    e1 =Etudiant(0,"ElAli" ,"Amar" ,"B")
    e2 =Etudiant(1,"ElAli" ,"Shaza" ,"B")
    db = DB() 
    db.insertEtudiant(e1)
    db.insertEtudiant(e2)
    for obj in db.etudiant:
        print( obj.nomEtudiant)
    db.etudiant.remove(e1)
    for obj in db.etudiant:
        print("Apres suppression :" )
        # print(obj.nomEtudiant )
    e3 =Etudiant(3,"ElAli" ,"Samar" ,"B")
    db.insertEtudiant(e3)
    # editer etudiant sauf l'identifiant
    # print("etudiant avant l'editer :"+ e2.nomEtudiant +", "+ e2.premomEtudiant +", "+e2.niveauEtudiant)
    e2.nomEtudiant ="Nour"
    e2.premomEtudiant ="Deiry"
    e2.niveauEtudiant = "C"
    # print("etudiant apres l'editer :"+ e2.nomEtudiant +", "+ e2.premomEtudiant +", "+e2.niveauEtudiant)
    # ajouter cours
    c1 = Cour("NFA006","structure de donner","B")
    c2 = Cour("MVA004","Automate","B")
    db.insertCours(c1)
    db.insertCours(c2)
    # supprimer un cour
    db.cours.remove(c1)
    # edit cour 2
    # print("Cour avant l'editer :"+ c2.intituleCours +", "+ c2.niveauCours )
    c2.intituleCours ="Programmation avancer"
    c2.niveauCours ="C"
    # print("Cour apres l'editer :"+ c2.intituleCours +", "+ c2.niveauCours)
    # ajouter note
    note1 = Note(1,"MVA004",15)
    note2 = Note(3,"MVA004",10)
    test1 = test(db.etudiant ,db.cours, note1)
    test2 = test(db.etudiant ,db.cours, note2)
    if test1:
        db.insertNote(note1)
        # print(note1.note) # test insertion
    if test2:
        db.insertNote(note2)
        # print(note2.note) # test insertion
    print(note1.note) 
    
       
    # db.note.remove(note1)
    print(note2.note)
    # edite note
    note2.note="18"
    print(note2.note)

    c3 = Cour("NFA007","Paradigmes","C")
    c4 = Cour("MV874","web3","B")
    c5 = Cour("MVA006","java3","B")  
    db.insertCours(c3)
    db.insertCours(c4)
    db.insertCours(c5)
    note3 = Note(1,"NFA007",15)
    note4 = Note(1,"MV874",10)
    note5 = Note(3,"MVA006",10)
    test3 = test(db.etudiant ,db.cours, note3)
    test4 = test(db.etudiant ,db.cours, note4)
    test5 = test(db.etudiant ,db.cours, note5)
    print(test3 , test4 ,test5)
    if test3:
        db.insertNote(note3)
    if test4:
        db.insertNote(note4)
    if test5:
        db.insertNote(note5)
    
    print(moyenneClass(db.etudiant , db.note))
    print(moyenneEtudiant(e2 , db.note))
    print(" Consulter les notes d’une classe :" , consulter(moyenneClass(db.etudiant , db.note)))
    print(" Consulter les notes d’un eleve :" , consulter(moyenneEtudiant(e2 , db.note)))

    
if __name__ == "__main__":
    main()