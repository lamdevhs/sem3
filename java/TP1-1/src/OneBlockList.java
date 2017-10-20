
public class OneBlockList implements List {
	Object[] xs;
	int maxsize;
	int size;
	
	OneBlockList(int maxsize) {
		this.maxsize = maxsize;
		this.size = 0;
		this.xs = new Object[this.maxsize];
	}

	@Override
	public int len() {
		// TODO Auto-generated method stub
		return this.size;
	}

	@Override
	public Object nth(int ix) throws IndexOutOfRangeException {
		// TODO Auto-generated method stub
		if (ix < 0 || this.size <= ix) {
			throw new IndexOutOfRangeException(ix);
		}
		return this.xs[ix];
	}

	@Override
	public void insert(int ix, Object e) throws IndexOutOfRangeException {
		// TODO Auto-generated method stub
		if (ix < 0 || this.size < ix) {
			throw new IndexOutOfRangeException(ix);
		}
		for (int i = this.size; i > ix; i--) {
			this.xs[i] = this.xs[i - 1];
		}
		this.size += 1;
		this.xs[ix] = e;
		
	}

	@Override
	public void del(int ix) throws IndexOutOfRangeException {
		// TODO Auto-generated method stub
		if (ix < 0 || this.size <= ix) {
			throw new IndexOutOfRangeException(ix);
		}
		for (int i = ix; i < this.size - 1; i++) {
			this.xs[i] = this.xs[i + 1];
		}
		this.size -= 1;
		
	}
	
	@Override
	public String toString() {
		String out = "[";
		for (int ix = 0; ix < this.size; ix ++) {
			out += " " + this.xs[ix].toString();
		}
		if (this.size != 0) out += " ";
		out += "]";
		return out;
	}
}
