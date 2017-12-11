package def;


public class ExceptionEmptyQueue extends RuntimeException {
    
    /**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	public ExceptionEmptyQueue() {
	super("la file est vide");
    }

}
