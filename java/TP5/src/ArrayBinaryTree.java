
public class ArrayBinaryTree {
	private String values;
	
	ArrayBinaryTree(String v) {
		this.values = v;
	}
	
	public char leaf(int ix) {
		return this.values.charAt(ix);
	}
	
	public int leftIx(int ix) {
		int res = 2*ix + 1;
		if (res >= this.values.length()) return -1;
		return res;
	}
	
	public int rightIx(int ix) {
		int res = 2*ix + 2;
		if (res >= this.values.length()) return -1;
		return res;
	}
	
	public int size() {
		return 0;
	}
	
	public int height() {
		if (this.values.length() == 0) return 0;
		int cpt = 0;
		int ix = 0;
		while(ix != -1) {
			cpt++;
			ix = this.leftIx(ix);
				// attempt to reach next level
		}
		return cpt;
	}
}
