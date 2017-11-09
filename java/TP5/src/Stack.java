
public class Stack {
	class LinkedList {
		Object head;
		LinkedList tail;
	}
	LinkedList stack;
	
	Stack() {
		this.stack = null;
	}
	
	public boolean isEmpty() {
		return this.stack == null;
	}
	
	public Object getTop() throws StackEmptyException{
		if (this.isEmpty()) {
			throw new StackEmptyException();
		}
		return this.stack.head;
	}
	
	public void cover(Object top) {
		LinkedList new_stack = new LinkedList();
		new_stack.tail = this.stack;
		new_stack.head = top;
		this.stack = new_stack;
	}
	
	public void uncover() throws StackEmptyException {
		if (this.isEmpty()) {
			throw new StackEmptyException();
		}
		this.stack = this.stack.tail;
	}
	
	public String toString() {
		if (this.isEmpty()) return "<empty stack>";
		String out = "[";
		LinkedList stack = this.stack;
		while (stack != null) {
			out += stack.head.toString();
			stack = stack.tail;
			if (stack != null) out += ",";
		}
		return out + "]";
	}
	
	public void print() {
		System.out.println(this.toString());
	}
}
