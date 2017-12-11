package def;


public class PriorityQueue<E> extends Heap<E> implements Queue<E> {

	public PriorityQueue() {
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
		super.insert(e);
		
	}

	@Override
	public void shift() throws ExceptionEmptyQueue {
		//System.out.println("deleting:");
		//System.out.println(this.content);
		this.delete(0);
		//System.out.println(this.content);
	}

}
