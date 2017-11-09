import java.util.ArrayList;
import java.util.Iterator;
import java.util.NoSuchElementException;
import java.util.TreeSet;

public class BTIter implements Iterator<Object> {
	private Stack s;
	private Stack parents; // for postfix: all the roots that need be added after their children
	//private StringQueue q;
	private BinaryTree here;
	private BinaryTree previous;
	private int mode;
	
	// MODES
	public static final int PREFIX = 0;
	public static final int POSTFIX = 1;
	//public static int INFIX = 2;
	//public static int INWIDTH = 3;
	
	BTIter(BinaryTree bt) {
		this(bt, BTIter.PREFIX);
		
	}
	
	BTIter(BinaryTree bt, int mode) {
		this.mode = mode;
		//this.mode = BTIter.PREFIX;
		switch (this.mode) {
			case BTIter.POSTFIX: this.parents = new Stack(); this.s = new Stack();
			break;
			case BTIter.PREFIX: this.s = new Stack();
			break;
			//case BTIter.INWIDTH: this.q = new StringQueue();
			//break;
			default: this.mode = BTIter.PREFIX; this.s = new Stack();
		}
		this.here = bt;
	}

	@Override
	public boolean hasNext() {
		return !this.s.isEmpty() || !this.here.isEmpty();
	}

	@Override
	public void remove() {
		// TODO Auto-generated method stub
		
	}

	@Override
	public Object next() {
		Object out;
		if (!this.hasNext())
		//if (this.mode == BTIter.PREFIX) {
			if (!this.here.isEmpty()) {
				out = this.here.root();
				this.s.cover(this.here.right());
				this.s.cover(this.here.left());
				try {
					this.here = (BinaryTree) this.s.getTop(); this.s.uncover();
					
				} catch (StackEmptyException e) {
					// TODO Auto-generated catch block
					throw new NoSuchElementException();
				}
				return out;
			}
			else {
				try {
					this.here = (BinaryTree) this.s.getTop(); this.s.uncover();
					
				} catch (StackEmptyException e) {
					// TODO Auto-generated catch block
					throw new NoSuchElementException();
				}
				return this.next();
			}
		//}
		
		/*
		else { //if (this.mode == BTIter.POSTFIX) {
			// when we finished a right tree: add its parent's label:
			if (this.previous != null && this.previous.isRightChild()) {
				try {
					this.here = (BinaryTree) this.parents.getTop(); this.parents.uncover();
				} catch (StackEmptyException e) {
					// TODO Auto-generated catch block
					throw new NoSuchElementException();
				}
				out = this.here.root();
				if (this.here.isLeftChild()) this.here = null;
				return out;
			}
			
			else if (!this.here.isEmpty()) {
				this.s.cover(this.here.right());
				this.s.cover(this.here.left());
				this.parents.cover(this.here);
				try {
					//this.previous = this.here; // possibly useless
					this.here = (BinaryTree) this.s.getTop(); this.s.uncover();
					
				} catch (StackEmptyException e) {
					// TODO Auto-generated catch block
					throw new NoSuchElementException();
				}
				return this.next();
			}
			else {
				if (this.here.isRightChild()) this.previous = here;
				else {
					try {
						//this.previous = this.here;
						
						this.here = (BinaryTree) this.s.getTop(); this.s.uncover();
					
					} catch (StackEmptyException e) {
						// TODO Auto-generated catch block
						throw new NoSuchElementException();
					}
				}
				return this.next();
			}
			
		}*/
		
	}
	
	
	//-----------------------------
	//-----------------------------
	//-----------------------------
	
	public static void main(String[] args) {
		ArrayList<Integer> ints = new ArrayList<Integer>();
		int card = 100;
		for (int i = 0; i < card; i++) {
			ints.add(randNb(11));
		}
		Iterator<Integer> it = ints.iterator();
		while (it.hasNext()){
			if (it.next() % 2 == 0) {
				it.remove();
			}
		}
		for (Integer i: ints) {
			System.out.print(i.intValue());
		}
		System.out.println();
		
		TreeSet<Integer> set = new TreeSet<Integer>();
		set.add(1); set.add(2); set.add(3); set.add(4);
		Iterator<Integer> itset = set.iterator();
		while(itset.hasNext()) {
			itset.next();
			//set.add(itset.next().intValue() + 100);
			itset.remove();
		}
		System.out.println(set.isEmpty());
	}
	
	public static int randNb(int nb) {
		return (int) (Math.floor(Math.random() * nb));
	}

}
