import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class PriorityQueueTest {
    PriorityQueue<Character> h;
    @Before
    public void init() {
    	h = new PriorityQueue<Character>();
    	String s = "helloworld";
    	for (int i = 0; i < s.length(); i++) {
    		Character c = s.charAt(i);
    		h.insert(c);
    		System.out.println(h.content);
    	}
    }
	@Test
	public void test() {
    	String out = "";
    	while (h.maxIx > 0) {
    		out += h.content.get(0);
    		h.delete(0);
    	}
    	assertEquals(out, "wroolllhed");
    	assertEquals(h.maxIx, 0);
	}
}
