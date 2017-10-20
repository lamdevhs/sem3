
public class StringPriorityQueue extends StringQueue implements PriorityQueue  {
    public static int groupSize = 4;
	@Override
	public void prioritaryPush(Object o) {
		Link newhead = new Link();
		newhead.next = this.head;
		newhead.value = o;
		this.head = newhead;
		if (this.isEmpty()) {
			this.foot = newhead;
		}
	}

	@Override
	public boolean isPrioritary(Object o) {
		try {
			return this.first() == o;
		} catch (EmptyQueueException e) {
			return false;
		}
	}
	
	@Override
	public void push(Object o) {
		if (this.isPrioritary(o))
			this.prioritaryPush(o);
		else
			super.push(o);
	}

	@Override
	public void pop() throws InvalidGroupException, EmptyQueueException {
		Link iter = this.head;
		if (iter == null) throw new EmptyQueueException();
		Object type = iter.next;
		for (int i = 0; i < groupSize; i++) {
			if (iter == null) throw new InvalidGroupException();
			Object o = iter.value;
			if (o != type) throw new InvalidGroupException();
			iter = iter.next;
		}
		for (int i = 0; i < groupSize; i++) {
			super.pop();
		}
	}
	
	public static void main(String[] args) {
		int  n = 30;
		PriorityQueue q = new StringPriorityQueue();
		for (int i = 0; i < n; i++) {
			Shape s = randShape();
			q.push(s);
		}
		System.out.println(q.toString());
		System.out.println("aaa");
	}
	public static Shape randShape() {
		if (randNb(2) == 0) return new Circle();
		else return new Square();
	}
	public static int randNb(int nb) {
		return (int) (Math.floor(Math.random() * nb));
	}
	
	public String toString() {
		String out = "[";
		Link iter = this.head;
		if (iter == null) return "[]";
		else out += iter.value.toString();
		iter = iter.next;
		while (iter != null) {
			out += " " + iter.value.toString();
		}
		return out + "]";
	}
}
