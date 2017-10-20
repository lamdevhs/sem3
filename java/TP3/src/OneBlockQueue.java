import java.util.ArrayList;

public class OneBlockQueue extends ArrayList<Object> implements Queue {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	
	OneBlockQueue() {
		super();
	}
	
	public boolean isEmpty() {
		return this.size() == 0;
	}
	
	public Object first() throws EmptyQueueException {
		if (this.isEmpty())
			throw new EmptyQueueException();
		return this.get(0);
	}
	
	public void pop() throws EmptyQueueException {
		if (this.isEmpty())
			throw new EmptyQueueException();
		this.remove(0);
	}
	
	public void push(Object o) {
		this.add(o);
	}
}
