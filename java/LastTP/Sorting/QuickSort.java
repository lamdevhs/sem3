import java.util.ArrayList;

public class QuickSort extends ArrayList<Integer>{
    /**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	QuickSort() {
    	int card = 30;
    	for (int i = 0; i < card; i ++) {
    		this.add(randInt(101));
    	}
    }
	
	void quickSort(int inf, int sup) {
		if (inf >= sup) return;
		int pivIx = this.splitSort(inf, sup);
		quickSort(inf, pivIx - 1);
		quickSort(pivIx + 1, sup);
	}
	
	void swap(int i, int j) {
		int xi = this.get(i);
		this.set(i, this.get(j));
		this.set(j, xi);
	}
	
	int splitSort(int inf, int pivIx) {
		int sup = pivIx - 1;
		int piv = this.get(pivIx);
		int i = inf;
		int j = sup;
		boolean stuck = false;
		while (i < j) {
			//by recursive hypothesis,
			//any element strictly before i
			//is a min (inferior to piv)
			//any element strictly after j
			//is a max
			
			//search next max from the left
			int k;
			for (k = i; k <= j; k++) {
				if (this.get(k) >= piv) {
					break;
				}
			}
			i = k;
			// the first max found to the left
			// was already sorted (after j)
			// so we finish,
			// and swap the pivot and
			// the first max to the left found
			// which in theory is equal to j + 1
			if (i > j) {
				this.swap(pivIx, i);
				pivIx = i;
				break;
			}
			//search next min from the right
			int l;
			for (l = j; l >= i; l--) {
				if (this.get(l) < piv) {
					break;
				}
			}
			j = l;
			// the first min found to the right
			// was already sorted (before i)
			// so we finish,
			// and swap the pivot with
			// j + 1, which is the last max
			// to the right
			if (i > j) {
				this.swap(pivIx, j+1);
				pivIx = j+1;
				break;
			}
			// else: we got a max at index i
			// and a min at index j: we swap them
			// then shift on both indices;
			this.swap(i, j);
			i++;
			j++;
			// if i <= j, all will be ok
			if (i > j) {
				//we swap the pivot and i,
				// which is the first max to the left
				this.swap(pivIx, i);
				pivIx = i;
				break;
			}
		}
		return pivIx;
	}
    
    static boolean randBool() {
    	return ListInt.randInt(2) == 0;
    }
    
    static int randInt(int sup) {
    	return (int) Math.abs(Math.random() * sup);
    }
    
    public static void main(String[] args) {
		QuickSort qs = new QuickSort();
		qs.quickSort(0, qs.size() - 1);
		System.out.println(qs);
	}
}
