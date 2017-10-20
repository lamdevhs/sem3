
public class IndexOutOfRangeException extends RuntimeException {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	public IndexOutOfRangeException(int i) { 
		super("Erreur d'indice : "+i);
	}
}

