
public class PriorityQueue<E> extends Heap<E> implements Queue<E> {

	PriorityQueue() {
		super();
	}
	
	@Override
	public boolean isEmpty() {
		return this.maxIx == 0;
	}

	@Override
	public E head() throws ExceptionEmptyQueue {
		if (this.isEmpty()) throw new ExceptionEmptyQueue();
		return this.content.get(0);
	}

	@Override
	public void add(E e) {
		this.add(e);
		
	}

	@Override
	public void shift() throws ExceptionEmptyQueue {
		this.delete(0);
	}

}
