
public class Thing {
    String size;
    String shape;
    String color;
    
    static String[] sizes = {"small", "big"};
    static String[] shapes = {"round", "square"};
    static String[] colors = {"yellow", "green", "black"};
    
    Thing() {
    	this.size = Thing.sizes[Thing.rand(2)];
    	this.shape = Thing.shapes[Thing.rand(2)];
    	this.color = Thing.colors[Thing.rand(3)];
    }
    
    
    private static int rand(int i) {
		return (int) Math.abs(Math.random()*i);
	}


	boolean equals(Thing other) {
    	return other.size == this.size
    			&& other.shape == this.shape
    			&& other.color == this.color;
    }
    
    public String toString() {
    	return String.format("a thing %s, %s and %s",
    			this.size,
    			this.shape,
    			this.color);
    }
}
