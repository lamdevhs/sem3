
public interface Queue {
	
	public boolean isEmpty();
	
	public Object first() throws EmptyQueueException;
	
	public void pop() throws EmptyQueueException, InvalidGroupException;
	
	public void push(Object o);
}
