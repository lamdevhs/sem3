package structure_tas;

public class ExceptionFileVide extends RuntimeException {
    
    public ExceptionFileVide() {
	super("la file est vide");
    }

}
