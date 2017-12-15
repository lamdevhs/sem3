
public class SelectingSort {
    static char[] text = "the quick brown fox jumps over the lazy dog".toCharArray();
    
    static int tailMinIx (char[] in, int origin) {
    	int ixMin = origin;
    	char charMin = in[ixMin];
    	for (int j = origin + 1; j < in.length; j++) {
    		char c = in[j]; 
    		if (c < charMin) {
    			ixMin = j;
    			charMin = c;
    		}
    	}
    	return ixMin;
    }
    
    static void selectingSort(char[] s) {
    	for (int i = 0; i < s.length - 1; i ++) {
    		int minIx = tailMinIx(s, i);
    		swap(s, minIx, i);
    	}
    }
    
    static void swap(char[] s, int i, int j) {
    	char xi = s[i];
    	char xj = s[j];
    	s[i] = xj;
    	s[j] = xi;
    }
    
    public static void main(String[] args) {
		selectingSort(text);
		System.out.println(text);
	}
}
