
public interface List {
	int len();
	
	Object nth(int ix) throws IndexOutOfRangeException;
	
	void insert(int ix, Object e) throws IndexOutOfRangeException;
	
	void del(int ix) throws IndexOutOfRangeException;
	
	String toString();
}
