package structure_dico.table_de_hachage;

public interface Dictionnaire<Clé,Valeur> {

	public void ajouter(Clé c, Valeur v) throws ExceptionCléDéjàExistante;
	
	public void supprimer(Clé c);
	
	public boolean estPrésent(Clé c);
	
	public Valeur rechercher(Clé c) throws ExceptionCléIntrouvable;
	
}
