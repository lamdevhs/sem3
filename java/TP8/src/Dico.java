public interface Dico<Clé,Valeur> {

	public void add(Clé c, Valeur v) throws ExceptionCléDéjàExistante;
	
	public void del(Clé c);
	
	public boolean exists(Clé c);
	
	public Valeur lookup(Clé c) throws ExceptionCléIntrouvable;
	
	public Pair<Clé, Valeur> get(Clé k);
	
}
