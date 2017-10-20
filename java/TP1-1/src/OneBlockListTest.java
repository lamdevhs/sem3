import static org.junit.Assert.*;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class OneBlockListTest {
	
	List l;
	
	@Before
	public void setUp() throws Exception {
		l = new LinkedList();
	}
	
	@After
	public void tearDown() throws Exception {
		
	}

	@Test
	public void test1() {
		l.insert(0, 'b');
		assertEquals("[ b ]", l.toString());
		l.insert(1, 'c');
		l.insert(2, 'd');	
		l.insert(0, 'a');
		assertEquals("[ a b c d ]", l.toString());
		assertEquals('b', l.nth(1));
		assertEquals('d', l.nth(3));
		assertEquals(4, l.len());
		l.del(2);
		l.del(0);
		l.insert(1, 'e');
		assertEquals("[ b e d ]", l.toString());
	}
	
	@Test (expected = IndexOutOfRangeException.class)
	public void test2() {
		l.insert(1, 'a');
		System.out.println("Liste : "+l.toString());
	}
	
	@Test (expected = IndexOutOfRangeException.class)
	public void test3() {

		l.insert(15, 'a');
		System.out.println("Liste : " + l.toString());
	}

	@Test (expected = IndexOutOfRangeException.class)
	public void test4() {

		l.insert(0, 'a');
		l.insert(1, 'b');
		l.insert(2, 'c');
		System.out.println("4ème élément : " + l.nth(3));
	}

	@Test (expected = IndexOutOfRangeException.class)
	public void test5() {

		l.insert(0, 'a');
		l.insert(1, 'b');
		l.insert(2, 'c');
		l.del(4);
		System.out.println("Liste : " + l.toString());
	}

	@Test (expected = IndexOutOfRangeException.class)
	public void test6() {

		l.del(-1);
		System.out.println("Liste : " + l.toString());
	}

}


