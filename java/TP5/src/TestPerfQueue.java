
public class TestPerfQueue {
	public static void main(String[] args) throws EmptyQueueException, InvalidGroupException {
		OneBlockQueue obq = new OneBlockQueue();
		StringQueue sq = new StringQueue();
		int n = 500*1000;
		test(n, obq, "OneBlockQueue");
		test(n, sq,  "StringQueue");
	}
	
	static String alphabet = "abcdefghijklmnopqrstuvwxyz";
	
	public static void test(int n, Queue q, String label) throws EmptyQueueException, InvalidGroupException {
		long ref = time();
		
		for (int i = 0; i < n; i ++) {
			pushRandChar(q);
		}
		while(!q.isEmpty()){
			q.pop();
		}
		
		long res = timer(ref);
		System.out.println("test " + label + " : " + res);
	}
	
	public static void pushRandChar(Queue q) {
		int rint = randNb(26);
		char rchar = alphabet.charAt(rint);
		q.push(rchar);
	}
	
	public static long timer(long ref) {
		return System.currentTimeMillis() - ref;
	}
	
	public static long time() {
		return System.currentTimeMillis();
	}
	
	public static int randNb(int nb) {
		return (int) (Math.floor(Math.random() * nb));
	}
}
