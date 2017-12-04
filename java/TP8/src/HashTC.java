import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;

public class HashTC<Key, Value> implements Dico<Key, Value>{

	private ArrayList<LinkedList<Pair<Key, Value>>> data;
	public static int size = 15;
	
	HashTC() {
		this.data = new ArrayList<LinkedList<Pair<Key, Value>>>(HashT.size);
		for (int i = 0; i < HashT.size; i++) {
			this.data.add(null);
		}
	}
	
	protected int hashKey(Key c) {
		return Math.abs(c.hashCode() % HashT.size);
	}
	
	public LinkedList<Pair<Key, Value>> getList(Key c) {
		return this.data.get(this.hashKey(c));
	}
	
	@Override
	public void add(Key c, Value v) throws ExceptionCléDéjàExistante {
		if (this.exists(c)) throw new ExceptionCléDéjàExistante();
		LinkedList<Pair<Key, Value>> L = this.getList(c);
		if (L == null) {
			L = new LinkedList<Pair<Key, Value>>();
			this.data.set(this.hashKey(c), L);
		}
		Pair<Key, Value> newP = new Pair<Key, Value>();
		newP.key = c;
		newP.value = v;
		L.add(newP);
	}

	@Override
	public void del(Key c) {
		int ix = this.indexInList(c);
		if (ix == -1) return;
		
		LinkedList<Pair<Key, Value>> L = this.getList(c);
		L.remove(ix);	
	}

	@Override
	public boolean exists(Key c) {
		int ix = this.indexInList(c);
		if (ix == -1) {
			return false;
		}
		return true;
		
	}
	
	public int indexInList(Key c) {
		LinkedList<Pair<Key, Value>> L = this.getList(c);
		if (L != null) {
			Iterator<Pair<Key, Value>> iter = L.iterator();
			int i = 0;
			boolean found = false;
			while (iter.hasNext()) {
				Pair<Key, Value> n = iter.next();
				if (n.key == c) {
					found = true;
					break;
				}
				i++;
			}
			if (found) return i;
		}
		return -1;
	}

	@Override
	public Value lookup(Key c) throws ExceptionCléIntrouvable {
		int ix = this.indexInList(c);
		if (ix == -1) {
			throw new ExceptionCléIntrouvable();
		}
		
		LinkedList<Pair<Key, Value>> L = this.getList(c);
		return L.get(ix).value;
	}

	@Override
	public Pair<Key, Value> get(Key k) {
		// TODO Auto-generated method stub
		return null;
	}

}
