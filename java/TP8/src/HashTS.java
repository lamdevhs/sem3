import java.util.ArrayList;

public class HashTS<Key, Value> implements DicoS<Key, Value> {

	
	private ArrayList<Pair2<Key, Value>> data;
	public static int size = 15;
	
	HashTS() {
		this.data = new ArrayList<Pair2<Key, Value>>(HashTS.size);
		for (int i = 0; i < HashTS.size; i++) {
			this.data.add(null);
		}
	}
	
	protected int hashKey(Key c) {
		return Math.abs(c.hashCode() % HashTS.size);
	}

	@Override
	public void add(Key c, Value v) throws ExceptionFullHashTable {
		int where = this.nextEmptyCell(c);
		if (where == -1) {
			throw new ExceptionFullHashTable();
		}
		Pair2<Key, Value> newP = new Pair2<Key, Value>();
		newP.key = c;
		newP.value = v;
		newP.ghost = false;
		this.data.set(where, newP);
	}
	
	public int nextEmptyCell(Key c) {
		int i = this.hashKey(c);
		int lim = (i - 1) % HashTS.size;
		do {
			if (this.data.get(i) == null) {
				return i;
			}
			else if (this.data.get(i).ghost == true) {
				return i;
			}
			i = (i+1) % HashTS.size;
			
		} while (i != lim);
		return -1;
	}
	
	public int indexByKey(Key c) {
		int i = this.hashKey(c);
		int lim = (i - 1) % HashTS.size;
		do {
			Pair2<Key, Value> p = this.data.get(i);
			if (p != null) {
				if(p.ghost != true && p.key == c) {
					return i;
				}
			}
			else {
				return -1;
			}
			i = (i+1) % HashTS.size;
			
		} while (i != lim);
		return -1;
	}

	@Override
	public void del(Key c) {
		int where = this.indexByKey(c);
		if (where != -1) {
			this.data.get(where).ghost = true;
		}
	}

	@Override
	public boolean exists(Key c) {
		return this.indexByKey(c) != -1;
	}

	@Override
	public Value lookup(Key c) throws ExceptionCléIntrouvable {
		int where = this.indexByKey(c);
		if (where == -1) {
			throw new ExceptionCléIntrouvable();
		}
		return this.data.get(where).value;
	}
	
	public String toString() {
		String out = "";
		int lim = HashTS.size;
		for (int i = 0; i < lim; i++) {
			Pair2<Key, Value> p = this.data.get(i);
			out += String.valueOf(i) + " - ";
			if (p != null) {
				out += p.toString();
			}
			out += "\n";
		}
		return out;
	}

}
