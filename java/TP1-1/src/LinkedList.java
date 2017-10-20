
public class LinkedList implements List {
	class Link {
		Object head;
		Link tail;
	}
	
	Link list;
	
	LinkedList() {
		this.list = null;
	}

	@Override
	public int len() {
		// TODO auto-generated method stub
		Link it = this.list;
		int acc = 0;
		while (it != null) {
			it = it.tail;
			acc++;
		}
		return acc;
	}

	@Override
	public Object nth(int ix) throws IndexOutOfRangeException {
		// TODO Auto-generated method stub
		Link it = this.list;
		int i = ix;
		while (i != 0) {
			if (it == null) throw new IndexOutOfRangeException(ix);
			it = it.tail;
			i--;
		}
		if (it == null) throw new IndexOutOfRangeException(ix);
		return it.head;
	}

	@Override
	public void insert(int ix, Object e) throws IndexOutOfRangeException {
		// TODO Auto-generated method stub
		Link next = this.list;
		Link prev = null;
		Link newLink = new Link();
		newLink.head = e;
		int i = ix;
		while (i != 0) {
			if (next == null) throw new IndexOutOfRangeException(ix);
			prev = next;
			next = next.tail;
			i--;
		}
		newLink.tail = next;
		if (ix == 0) this.list = newLink;
		else prev.tail = newLink;
	}

	@Override
	public void del(int ix) throws IndexOutOfRangeException {
		// TODO Auto-generated method stub
		Link todel = this.list;
		Link prev = null;
		int i = ix;
		while (i != 0) {
			if (todel == null) throw new IndexOutOfRangeException(ix);
			prev = todel;
			todel = todel.tail;
			i--;
		}
		if (ix == 0) this.list = todel.tail;
		else prev.tail = todel.tail;
	}
	
	@Override
	public String toString() {
		String out = "[";
		for (Link it = this.list; it != null; it = it.tail) {
			out += " " + it.head.toString();
		}
		if (this.len() != 0) out += " ";
		out += "]";
		return out;
	}
}
