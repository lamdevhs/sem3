
public interface Queue<E> {

	public boolean isEmpty();
	public E head() throws ExceptionEmptyQueue;
	public void add(E e);
	public void shift() throws ExceptionEmptyQueue; 
	
}
