
public class App2 {
	static int pile = 0;
	public static void main(String[] args) {
		List l = new LinkedList();
		List l2 = new OneBlockList(20);
		test1(l); test1(l2);
	}
	
	public static void test1(List l) {
		int size = 20;
		for (int i = 0; i < size; i++) {
			int coin = pileFace();
			if (coin == App2.pile) {
				l.insert(0, randNb(10));
			}
			else {
				int coin2 = pileFace();
				if (coin2 == App2.pile) l.insert(0, true);
				else l.insert(0, false);
			}
			
		}
		System.out.println(l.toString());
	}
	
	public static int randNb(int nb) {
		return (int) (Math.floor(Math.random() * (nb)));
	}
	
	public static int pileFace() {
		return randNb(2);
	}

}