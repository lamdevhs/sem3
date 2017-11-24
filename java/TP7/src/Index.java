import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Set;

public class Index extends HashMap<String, ArrayList<Entry>> {

    /**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	static String[] sections = {"abstract", "intro", "related", "contribution", "foundations", "model", "experiment", "discussion", "conclusion" };

	public void buildIndex(String section, String word) throws IOException {
		ArrayList<String> lines = Index.readSection(section);
		if (lines == null) {
			return;
		}
		ArrayList<Entry> entries = this.get(word);
		if (entries == null) {
			entries = new ArrayList<Entry>();
		}
		int lenLines = lines.size();
		for (int i = 0; i<lenLines; i++) {
			String line = lines.get(i);
			if (line.indexOf(word) >= 0) {
				Entry e = new Entry();
				e.lineIndex = i;
				e.sectionName = section;
				entries.add(e);
			}
		}
		this.put(word, entries);
	}
	
	public static ArrayList<String> readSection(String section) throws IOException {
		if (! Arrays.asList(Index.sections).contains(section)) {
			return null;
		}
		ArrayList<String> lines = new ArrayList<String>();
		FileReader in = new FileReader("src/" + section + ".txt");
		try (BufferedReader br = new BufferedReader(in)) {
		    String line = br.readLine();
		    while (line != null) {
				//System.out.println(line);
		    	lines.add(line);
				line = br.readLine();
		    }
		}
		return lines;
	}
	
    public static void main(String args[]) throws IOException {
		String[] forIndex = {"cortexionist", "neural network",
				"knowledge", "pattern", "simulation",
				"intelligence", "memory", "behavior",
				"learning"};
		Index myIndex = new Index();
		for (String section: sections) {
			for (String word: forIndex) {
				myIndex.buildIndex(section, word);
			}
		}
    }
    
    public String toString() {
    	String out = "";
    	Set<String> keys = this.keySet();
    	for (String key: keys) {
    		ArrayList<Entry> entries = this.get(key);
    	}
    }


}
