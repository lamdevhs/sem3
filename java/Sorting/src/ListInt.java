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
    
    public static void main(String[] args) {
		ListInt ints = new ListInt();
		System.out.println(ints.size());
		
		long start = System.currentTimeMillis();
		int n = 1000;
		int successes = 0;
		for (int i = 0; i < n; i++) {
			int r = ListInt.randInt(ints.sup);
			if (ints.contains(r)) {
				successes++;
			}
		}
		long span = System.currentTimeMillis() - start;
		double rate = successes / n;
		System.out.println("rate: " + String.valueOf(rate));
		
	}
}
