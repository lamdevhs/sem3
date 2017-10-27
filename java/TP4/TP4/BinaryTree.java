
public class BinaryTree {
	private BinaryTree _left;
	private BinaryTree _right;
	private Object _root;
	
	BinaryTree(Object o, BinaryTree l, BinaryTree r) {
		this._root = o;
		this._left = l;
		this._right = r;
	}

	
	public static BinaryTree emptyTree() {
		BinaryTree empty = new BinaryTree(null, null, null);
		return empty;
	}

	public static BinaryTree leaf(Object o) {
		BinaryTree leaf = new BinaryTree(
				o,
				BinaryTree.emptyTree(),
				BinaryTree.emptyTree());
		return leaf;
	}

	public Object root() {
		return this._root;
	}

	public BinaryTree left() {
		return this._left;
	}
	
	public BinaryTree right() {
		return this._right;
	}
	
	public boolean isEmpty() {
		return this._root == null;
	}

	
	public boolean isLeaf() {
		if (this.isEmpty()) return false;
		return this.left().isEmpty() && this.right().isEmpty();
	}
	
	public int size() {
		if (this.isEmpty()) return 0;
		else return this._left.size()
				+ this._right.size() + 1;
	}
	
	public int height() {
		if (this.isEmpty()) return 0;
		else return Math.max(
				this._left.height(),
				this._right.height())
				+ 1;
	}
	
}
