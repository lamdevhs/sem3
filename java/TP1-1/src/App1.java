
public class App1 {
	public static void main(String[] args) {
		List l = new LinkedList();
		List l2 = new OneBlockList(20);
		test1(l); test1(l2);
	}
	
	public static void test1(List l) {
		int size = 20;
		for (int i = 0; i < size; i++) {
			l.insert(0, randNb());
		}
		System.out.println(l.toString());
		filter(l);
		System.out.println(l.toString());
	}
	
	public static int randNb() {
		return (int) (Math.floor(Math.random() * (20)) - 10);
	}
	
	public static void filter(List l) {
		int ix = l.len();
		for (int i = 0; i < ix; i++) {
			int e = (int)l.nth(i);
			if (e % 2 == 0 || e < 0) {
				l.del(i);
				ix = l.len();
				i--;
			}
		}
	}
}
