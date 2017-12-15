import java.util.ArrayList;

public class ListInt extends ArrayList<Integer> {
	public int sup = 100*1000;
    ListInt() {
    	for (int i = 0; i < this.sup; i++) {
    		if (ListInt.randBool()) {
    			this.add(i);
    		}
    	}
    }
    
    static boolean randBool() {
    	return ListInt.randInt(2) == 0;
    }
    
    static int randInt(int sup) {
    	return (int) Math.abs(Math.random() * sup);
    }
    
    boolean dsearch(int toSearch) {
    	int inf = 0;
    	int sup = this.size();
    	while(inf < sup - 1) {
    		int mid = (inf + sup) / 2;
    		int el = this.get(mid);
    		if (el == toSearch) {
    			return true;
    		}
    		if (el < toSearch) {
    			inf = mid;
    		}
    		else {
    			sup = mid;
    		}
    	}
    	if (this.get(inf) == toSearch) {
    		return true;
    	}
    	return false;
    }
    
    public static void main(String[] args) {
		ListInt ints = new ListInt();
		System.out.println(ints.size());
		
		long start = System.currentTimeMillis();
		int n = 1000;
		double successes = 0;
		for (int i = 0; i < n; i++) {
			int r = ListInt.randInt(ints.sup);
			if (ints.contains(r)) {
				successes++;
			}
		}
		long span = System.currentTimeMillis() - start;
		double rate = successes / n;
		System.out.println("rate: " + String.valueOf(rate));
		System.out.println("span (ms): " + String.valueOf(span));
		
		/////////
		// dicho:
		
		start = System.currentTimeMillis();
		successes = 0;
		for (int i = 0; i < n; i++) {
			int r = ListInt.randInt(ints.sup);
			if (ints.dsearch(r)) {
				successes++;
			}
		}
		span = System.currentTimeMillis() - start;
		rate = successes / n;
		System.out.println("rate: " + String.valueOf(rate));
		System.out.println("span (ms): " + String.valueOf(span));
	
	}
}
