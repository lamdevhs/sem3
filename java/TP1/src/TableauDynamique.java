import java.util.Vector;

public class TableauDynamique {
    public static char[] pool = {'a', 'b', 'c', 'd', 'e'}; 
	public static void main(String[] args) {
		// TODO Auto-generated method stub
        Vector<Character> v = new Vector<Character>(500);
        String s = "v.size = %d; v.capacity = %d";
                
        for (int i=0; i<500; i++){
        	int randi= (int)(Math.random() * pool.length);
        	char randc = TableauDynamique.pool[randi];
        	v.addElement(randc);
        	String sloop = "Round %d; ; new elem = %c; ";
        	System.out.print(String.format(sloop, i, randc));
        	System.out.println(
        			String.format(s, v.size(), v.capacity()));
        }
        for (int j=0; j<300; j++) {
        	v.remove(0);
        }
        System.out.print("After having removed 300 elements: ");
    	System.out.println(
    			String.format(s, v.size(), v.capacity()));
    	v.trimToSize();
    	System.out.print("After trimToSize: ");
    	System.out.println(
    			String.format(s, v.size(), v.capacity()));
           	
        
	}

}
