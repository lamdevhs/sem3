import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;

public class HashTTest {
	public HashT<String, String> dico;
	@Before
	public void init() throws ExceptionCléDéjàExistante{
		dico =  new HashT<String, String>();
		dico.add("USB", "Universal Serial Bus");
		dico.add("BIOS", "Basic Input-Output System");
		dico.add("IP", "Internet Protocol");
		dico.add("BYTE", "A byte is a storage unit for data");
		
		dico.add("PC", "Personal Computer");
		
		dico.add("MAC", "Apple Macintosh");
		dico.add("ROM", "Read-Only Memory");
		dico.add("CPU", "Central Processing Unit");
	}
	
	@Test (expected = ExceptionCléDéjàExistante.class)
	public void testAdd() throws ExceptionCléDéjàExistante {
		dico.add("MAC", "Media Access Control");
	}

	@Test
	public void testDel() {
		dico.del("BYTE");
		assertEquals(dico.exists("BYTE"), false);
	}

	@Test
	public void testExists() {
		assertEquals(dico.exists("BIOS"), true);
		assertEquals(dico.exists("WYSIWYG"), false);
		assertEquals(dico.exists("PDF"), false);
	}

	@Test (expected = ExceptionCléIntrouvable.class)
	public void testLookupFail() throws ExceptionCléIntrouvable {
		dico.lookup("WYSIWYG");
	}

}
