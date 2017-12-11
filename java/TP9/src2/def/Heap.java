package def;

import java.util.ArrayList;

public class Heap<E> {
    protected int maxIx;
    public ArrayList<E> content;
    
    Heap() {
    	this.maxIx = 0;
    	this.content = new ArrayList<E>();
    }
    
    void insert(E element) {
    	this.content.add(element);
    	int ix = this.maxIx;
    	this.maxIx += 1;
    	this.orderUp(ix);
    }
    
    // boolean == whether it did anything
    boolean orderUp(int child) {
    	int parent = this.parent(child);
    	if (parent == -1 || this.ord(child, parent)) {
    		return false;
    	}
    	else {
    		this.swap(child, parent);
    		int newIx = parent;
    		this.orderUp(newIx);
    		return true;
    	}
    }
    
    void delete(int index) {
    	E lastElement =
    			this.content.get(this.maxIx - 1);
    	this.content.set(index, lastElement);
    	this.maxIx -= 1;
    	boolean orderUpWasNeeded =
    			this.orderUp(index);
    	if (!orderUpWasNeeded) {
    		this.orderDown(index);
    	}
    }
    
    void orderDown(int parent) {
    	int childL = this.sag(parent);
    	int childR = this.sad(parent);
    	int max = parent;
    	if (childL != -1 && this.ord(max, childL)) {
    		max = childL;
    	}
    	if (childR != -1 && this.ord(max, childR)) {
    		max = childR;
    	}
    	if (max == parent) {
    		return;
    	}
    	else {
    		this.swap(max, parent);
    		int newIx = max;
    		this.orderDown(newIx);
    	}
    }
    
    void swap(int a, int b) {
    	E tmp = this.content.get(a);
    	this.content.set(a, this.content.get(b));
    	this.content.set(b, tmp);
    }
    
    int parent(int child) {
    	if (child == 0) return -1;
    	return (child - 1) / 2;
    }
    
    int sag(int child) {
    	int out = child*2 + 1;
    	if (out >= this.maxIx) return -1;
    	return out;
    }
    
    int sad(int child) {
    	int out = child*2 + 2;
    	if (out >= this.maxIx) return -1;
    	return out;
    }
    
    boolean ord(int ix, int ix2) {
    	E e = this.content.get(ix);
    	E e2 = this.content.get(ix2);
    	boolean out = ((Comparable) e).compareTo(e2) < 0;
    	//System.out.println(e.toString() + " < "
    	//    + e2.toString() + " is " + String.valueOf(out));
    	return out;
    }
    
    public static void main(String[] args) {
    	int i = (0)/2;
		System.out.println(i);
	}
    
    public ArrayList<E> toList() {
    	return this.content;
    }
    
    public String toString() {
    	String out = "[";
    	for (int i = 0; i < this.maxIx -1; i++) {
    		out += this.content.get(i).toString() + ",";
    	}
    	if (this.maxIx > 0) out += this.content.get(this.maxIx - 1);
    	return out;
    }
}
