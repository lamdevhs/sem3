
public class Cycles {
	public static String[] libellés = {"er", "nd", "ème"};
	public static int[] durées = {3,2,3};
	
	public static void printing() {
		int len = Cycles.libellés.length;
		for (int i=0; i<len; i++){
			int d = durées[i];
			String l = libellés[i];
			System.out.println(String.format("Le %d%s cycle universitaire dure %d ans."
					  , i+1, l, d));
		}
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Cycles.printing();
	}
}
