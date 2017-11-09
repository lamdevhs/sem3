import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class QueueTests {
	Queue q;
	@Before
	public void init() {
		q = new StringQueue();
	}

	@Test
	public void testEmptiness() throws EmptyQueueException, InvalidGroupException {
		assertEquals(q.isEmpty(), true);
		q.push(0);
		assertEquals(q.isEmpty(), false);
		q.pop();
		assertEquals(q.isEmpty(), true);
	}

	@Test (expected = EmptyQueueException.class)
	public void testFirstOfEmptyErr() throws EmptyQueueException {
		q.first();
	}

	@Test (expected = EmptyQueueException.class)
	public void testPopEmptyErr() throws EmptyQueueException, InvalidGroupException {
		q.pop();
	}
	
	@Test
	public void testOrder() throws EmptyQueueException, InvalidGroupException {
		int a = 0;
		int b = 1;
		int c = 2;
		q.push(a); q.push(b); q.push(c);
		assertEquals(q.first(), a); q.pop();
		assertEquals(q.first(), b); q.pop();
		assertEquals(q.first(), c); q.pop();
		assertEquals(q.isEmpty(), true);
	}
}

