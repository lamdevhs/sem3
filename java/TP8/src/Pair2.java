
public class Pair2<Key, Value> {
	public Key key;
	public Value value;
	public boolean ghost;
	
	public String toString() {
		return "<" + this.key.toString()
			+ "," + this.value.toString() + ">";
	}
}