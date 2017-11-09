import java.util.ArrayList;
import java.util.Iterator;


public class BinaryTree implements Iterable<Object> {
	private BinaryTree _left;
	private BinaryTree _right;
	private Object _root;
	private BinaryTree _parent;
	
	BinaryTree(Object o, BinaryTree l, BinaryTree r) {
		this._root = o;
		this._left = l;
		this._right = r;
		if (l != null) this._left._parent = this;
		if (r != null) this._right._parent = this;
	}
	
	public boolean hasParent() {
		return this._parent != null;
	}
	
	public boolean isLeftChild() {
		if (!this.hasParent()) return false;
		return this._parent.left() == this;
	}
	
	public boolean isRightChild() {
		if (!this.hasParent()) return false;
		return this._parent.right() == this;
	}
	
	public BinaryTree parent() {
		return this._parent;
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
	
	public void infixWalkthroughInDepth (ArrayList<Object> arr) throws StackEmptyException {
		if (this.left() != null) this.left().infixWalkthroughInDepth(arr);
		if (this.root() != null) arr.add(this.root());
		if (this.right() != null) this.right().infixWalkthroughInDepth(arr);
	}
	
	public ArrayList<Object> infixWalkthroughInDepth () throws StackEmptyException {
		ArrayList<Object> out = new ArrayList<Object>();
		this.infixWalkthroughInDepth(out);
		return out;
	}
	
	public ArrayList<Object> prefixWalkthroughInDepth () throws StackEmptyException {
		ArrayList<Object> out = new ArrayList<Object>();
		Stack s = new Stack();
		BinaryTree iter = this;
		while(!s.isEmpty() || !iter.isEmpty()) {
			if (!iter.isEmpty()) {
				out.add(iter.root());
				s.cover(iter.right());
				s.cover(iter.left());
				iter = (BinaryTree) s.getTop();	s.uncover();
			}
			else  {
				iter = (BinaryTree) s.getTop();	s.uncover();
			}
		}
		
		return out;
	}

	public ArrayList<Object> walkthroughInWidth () throws StackEmptyException, EmptyQueueException, InvalidGroupException {
		ArrayList<Object> out = new ArrayList<Object>();
		StringQueue q = new StringQueue();
		BinaryTree iter = this;
		while(!q.isEmpty() || !iter.isEmpty()) {
			if (!iter.isEmpty()) {
				out.add(iter.root());
				q.push(iter.left());
				q.push(iter.right());
				iter = (BinaryTree) q.first();	q.pop();
			}
			else  {
				iter = (BinaryTree) q.first();	q.pop();
			}
		}
		
		return out;
	}
	
	public static void main(String[] args) throws StackEmptyException, EmptyQueueException, InvalidGroupException {
		BinaryTree expr = new BinaryTree(
				'+',
				new BinaryTree(
					'-',
					BinaryTree.leaf(5),
					new BinaryTree(
						'*',
						BinaryTree.leaf(2),
						BinaryTree.leaf(6))),
				new BinaryTree(
					'*',
					new BinaryTree(
						'+',
						BinaryTree.leaf(5),
						new BinaryTree(
							'/',
							BinaryTree.leaf(6),
							BinaryTree.leaf(2))),
					BinaryTree.leaf(3)));
		ArrayList<Object> al = expr.prefixWalkthroughInDepth();
		Object[] arr = new Object[expr.size()];
		al.toArray(arr);
		for (Object o: arr) {
			System.out.print(o.toString());
		}
		System.out.println();
		
		al = expr.walkthroughInWidth();
		al.toArray(arr);
		for (Object o: arr) {
			System.out.print(o.toString());
		}
		System.out.println();
		
		al = expr.infixWalkthroughInDepth();
		al.toArray(arr);
		for (Object o: arr) {
			System.out.print(o.toString());
		}
		System.out.println();
		
		// with iterators
		Iterator<Object> it = expr.iterator(BTIter.PREFIX);
		System.out.println("prefix");
		while(it.hasNext()) {
			System.out.print(it.next().toString());
		}
		System.out.println();
		/*
		it = expr.iterator(BTIter.INWIDTH);
		while(it.hasNext()) {
			System.out.print(it.next().toString());
		}
		System.out.println();
		*/
		it = expr.iterator(BTIter.POSTFIX);
		System.out.println("postfix");
		/*
		while(it.hasNext()) {
			System.out.print(it.next().toString());
		}
		*/
		System.out.println();
		
	}


	@Override
	public Iterator<Object> iterator() {
		return new BTIter(this);
	}
	
	public Iterator<Object> iterator(int mode) {
		return new BTIter(this, mode);
	}
	
}
