
public class StringQueue implements Queue {
	class Link {
		Link next;
		Object value;
	}
	
	Link head;
	Link foot;
	
	StringQueue() {
		this.head = null;
		this.foot = null;
	}
	
	public boolean isEmpty() {
		return this.head == null;
	}
	
	public Object first() throws EmptyQueueException {
		if (this.isEmpty())
			throw new EmptyQueueException();
		return this.head.value;
	}

	public void pop() throws EmptyQueueException, InvalidGroupException {
		if (this.isEmpty())
			throw new EmptyQueueException();
		this.head = this.head.next;
	}

	public void push(Object o) {
		Link newFoot = new Link();
		newFoot.next = null;
		newFoot.value = o;
		if (!this.isEmpty())
			this.foot.next = newFoot;
		else
			this.head = newFoot;
		this.foot = newFoot;
	}
}
