import java.util.ArrayList;

public class HashT<Key, Value> implements Dico<Key, Value> {

	
	private ArrayList<Pair<Key, Value>> data;
	public static int size = 15;
	
	HashT() {
		this.data = new ArrayList<Pair<Key, Value>>(HashT.size);
		for (int i = 0; i < HashT.size; i++) {
			this.data.add(null);
		}
	}
	
	protected int hashKey(Key c) {
		return Math.abs(c.hashCode() % HashT.size);
	}

	@Override
	public void add(Key c, Value v) throws ExceptionCléDéjàExistante {
		if (this.exists(c)) {
			throw new ExceptionCléDéjàExistante();
		}
		int hashK = this.hashKey(c);
		Pair<Key, Value> newP = new Pair<Key, Value>();
		newP.key = c;
		newP.value = v;
		this.data.set(hashK, newP);
	}

	@Override
	public void del(Key c) {
		int hashK = this.hashKey(c);
		this.data.set(hashK, null);
		
	}

	@Override
	public boolean exists(Key c) {
		Pair<Key, Value> p = this.get(c);
		if (p != null) {
			return p.key == c;
		}
		return false;
	}

	@Override
	public Value lookup(Key c) throws ExceptionCléIntrouvable {
		if (this.get(c) == null) {
			throw new ExceptionCléIntrouvable();
		}
		return this.get(c).value;
	}

	@Override
	public Pair<Key, Value> get(Key k) {
		int hashK = this.hashKey(k);
		Pair<Key, Value> there = this.data.get(hashK);
		return there;
	}
	
	public String toString() {
		String out = "";
		int lim = HashT.size;
		for (int i = 0; i < lim; i++) {
			Pair<Key, Value> p = this.data.get(i);
			out += String.valueOf(i) + " - ";
			if (p != null) {
				out += p.toString();
			}
			out += "\n";
		}
		return out;
	}
}
