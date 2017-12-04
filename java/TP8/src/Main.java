
public class Main {

	public static void main2(String[] args) throws ExceptionCléDéjàExistante {
		HashT<String, String> dico = new HashT<String, String>();
		dico.add("USB", "Universal Serial Bus");
		dico.add("BIOS", "Basic Input-Output System");
		dico.add("IP", "Internet Protocol");
		dico.add("BYTE", "A byte is a storage unit for data");
		
		dico.add("PC", "Personal Computer");
		
		dico.add("MAC", "Apple Macintosh");
		dico.add("ROM", "Read-Only Memory");
		dico.add("CPU", "Central Processing Unit");
		
		System.out.println(dico.toString());
	}
	
	public static void main(String[] args) throws ExceptionFullHashTable, ExceptionCléDéjàExistante {
		HashTS<String, String> dico = new HashTS<String, String>();
		dico.add("BIOS", "Basic Input-Output System");
		dico.add("BYTE", "A byte is a storage unit for data");
		dico.add("CPU", "Central Processing Unit");
		dico.add("IP", "Internet Protocol");
		dico.add("MAC", "Apple Macintosh");
		dico.add("OS", "Operating System");
		dico.add("PC", "Personal Computer");
		dico.add("PDF", "Portable Document Format");
		dico.add("RAM", "Random Access Memory");
		dico.add("ROM", "Read-Only Memory");
		dico.add("RTFM", "Read The F****** Manual");
		dico.add("USB", "Universal Serial Bus");
		dico.add("VGA", "Video Graphics Array");
		dico.add("WYSIWYG", "What You See Is What You Get");
		
		System.out.println(dico.toString());
	}

}
