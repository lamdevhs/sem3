
public class Perf {
	public static long timer(long ref) {
		return System.currentTimeMillis() - ref;
	}
	
	public static long time() {
		return System.currentTimeMillis();
	}
	
	public static int randNb(int nb) {
		return (int) (Math.floor(Math.random() * nb));
	}
	
	public static void main(String[] args) {
		int n = 100 * 1000;
		int n2 = 50 * 1000;
		testInsertDelRandAll(n2); 
		testInsertTailAll(n);
		testInsertHeadAll(n);
		testInsertRandAll(n);
	}
	
	public static void testInsertTailAll(int n) {
		LinkedList ll = new LinkedList();
		OneBlockList obl = new OneBlockList(n);
		testInsertTail(obl, "OneBlockList", n);
		testInsertTail(ll, "LinkedList", n);
	}
	
	public static void testInsertTail(List l, String s, int n) {
		long ref = time();
		int dummy = 0;
		int lastIx = 0;
		for (int i = 0; i < n; i++) {
			l.insert(lastIx, dummy);
			lastIx++;
		}
		long res = timer(ref);
		System.out.println("testInsertTail: " + s + " " + res);
		
	}
	
	public static void testInsertHeadAll(int n) {
		LinkedList ll = new LinkedList();
		OneBlockList obl = new OneBlockList(n);
		testInsertHead(ll, "LinkedList", n);
		testInsertHead(obl, "OneBlockList", n);
	}
	
	public static void testInsertHead(List l, String s, int n) {
		long ref = time();
		int dummy = 0;
		for (int i = 0; i < n; i++) {
			l.insert(0, dummy);
		}
		long res = timer(ref);
		System.out.println("testInsertHead: " + s + " " + res);
		
	}

	public static void testInsertRandAll(int n) {
		LinkedList ll = new LinkedList();
		OneBlockList obl = new OneBlockList(n);
		testInsertRand(ll, "LinkedList", n);
		testInsertRand(obl, "OneBlockList", n);
	}
	
	public static void testInsertRand(List l, String s, int n) {
		long ref = time();
		int dummy = 0;
		int ix;
		int size = 0;
		for (int i = 0; i < n; i++) {
			ix = randNb(size);
			l.insert(ix, dummy);
			size++;
		}
		long res = timer(ref);
		System.out.println("testInsertRand: " + s + " " + res);
		
	}
	
	public static void testInsertDelRandAll(int n) {
		LinkedList ll = new LinkedList();
		OneBlockList obl = new OneBlockList(n);
		testInsertDelRand(ll, "LinkedList", n);
		testInsertDelRand(obl, "OneBlockList", n);
	}

	public static void testInsertDelRand(List l, String s, int n) {
		long ref = time();
		testInsertRand(l, s, n);
		int ix;
		int size = n;
		while (size > 0) {
			ix = randNb(size);
			l.del(ix);
			size--;
		}
		long res = timer(ref);
		System.out.println("testInsertDelRand: " + s + " " + res);
		
	}
	

}
