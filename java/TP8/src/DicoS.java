public interface DicoS<Clé,Valeur> {

	public void add(Clé c, Valeur v) throws ExceptionFullHashTable;
	
	public void del(Clé c);
	
	public boolean exists(Clé c);
	
	public Valeur lookup(Clé c) throws ExceptionCléIntrouvable;
	
}
