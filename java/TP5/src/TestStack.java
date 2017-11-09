import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class TestStack {
	Stack s;
	@Before
	public void init() {
		s = new Stack();
	}

	@Test
	public void testStack() {
		assertEquals(s.stack, null);
	}

	@Test
	public void testIsEmpty() throws StackEmptyException {
		assertEquals(s.isEmpty(), true);
		s.cover(1);
		assertEquals(s.isEmpty(), false);
		s.uncover();
		assertEquals(s.isEmpty(), true);
	}

	@Test (expected = StackEmptyException.class)
	public void testGetTopError() throws StackEmptyException {
		Object a = s.getTop();
		System.out.println("top = " + a.toString());
	}
	
	@Test
	public void testGetTopNoError() throws StackEmptyException {
		s.cover(1); s.cover(2);
		assertEquals(s.getTop(), 2);
		s.uncover();
		assertEquals(s.getTop(), 1);
	}

	@Test
	public void testCover() throws StackEmptyException {
		assertEquals(s.isEmpty(), true);
		s.cover(1); assertEquals(s.getTop(), 1);
		s.cover(2); assertEquals(s.getTop(), 2);
		s.uncover(); assertEquals(s.getTop(), 1);
		s.cover(3); assertEquals(s.getTop(), 3);
	}

	@Test (expected = StackEmptyException.class)
	public void testUncoverError() throws StackEmptyException {
		s.uncover();
	}
	
	@Test
	public void testUncoverNoError() throws StackEmptyException {
		s.cover(1); s.cover(2);
		s.uncover(); assertEquals(s.isEmpty(), false);
		s.uncover(); assertEquals(s.isEmpty(), true);
	}

}
