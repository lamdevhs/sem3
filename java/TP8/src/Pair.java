public class Pair<Key, Value> {
		public Key key;
		public Value value;
		
		public String toString() {
			return "<" + this.key.toString()
				+ "," + this.value.toString() + ">";
		}
	}