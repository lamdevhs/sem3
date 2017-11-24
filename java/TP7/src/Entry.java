
public class Entry {
	public String sectionName;
	public int lineIndex;
	
	public String toString() {
		return this.sectionName + ":" + String.valueOf(this.lineIndex);
	}
}
