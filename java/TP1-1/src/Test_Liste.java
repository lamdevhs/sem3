
public class Test_Liste {

	public static void main(String[] args) {

		List l;
		l = new LinkedList();
		test1(l);
		test2(l);
		test3(l);
		test4(l);
		test5(l);
		test6(l);
	}

	/**
	 * On ne cherche qu'à valider le fonctionnement de la structure. On évite
	 * donc les cas problématiques
	 */
	public static void test1(List l) {

		l.insert(0, 'b');
		System.out.println("Liste : " + l.toString());
		l.insert(1, 'c');
		System.out.println("Liste : " + l.toString());
		l.insert(2, 'd');
		System.out.println("Liste : " + l.toString());
		l.insert(0, 'a');
		System.out.println("Liste : " + l.toString());
		System.out.println("1er élément : " + l.nth(1));
		System.out.println("3eme élément : " + l.nth(3));
		System.out.println("Longueur de la liste : " + l.len());
		l.del(2);
		l.del(0);
		l.insert(1, 'e');
		System.out.println("Liste : " + l.toString());
	}

	/*
	 * Dans les fonctions qui suivent, on teste le comportement de la liste dans
	 * les cas particuliers
	 */

	public static void test2(List l) {

		l.insert(1, 'a');
		System.out.println("Liste : " + l.toString());
	}

	public static void test3(List l) {

		l.insert(15, 'a');
		System.out.println("Liste : " + l.toString());
	}

	public static void test4(List l) {

		l.insert(0, 'a');
		l.insert(1, 'b');
		l.insert(2, 'c');
		System.out.println("4ème élément : " + l.nth(3));
	}

	public static void test5(List l) {

		l.insert(0, 'a');
		l.insert(1, 'b');
		l.insert(2, 'c');
		l.del(4);
		System.out.println("Liste : " + l.toString());
	}

	public static void test6(List l) {

		l.del(-1);
		System.out.println("Liste : " + l.toString());
	}

}