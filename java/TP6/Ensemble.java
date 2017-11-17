

public interface Ensemble<E> {

	public void ajouter(E e);
	
	public void enlever(E e);
	
	public boolean contient(E e);
	
	public int cardinalité();
	
}
