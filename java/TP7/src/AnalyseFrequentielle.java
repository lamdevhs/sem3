import java.util.HashMap;
import java.util.Iterator;
import java.util.Set;

public class AnalyseFrequentielle {

    static String texteFR = "la cryptographie est une des disciplines de la cryptologie s'attachant a"
	    + "proteger des messages, assurant confidentialite, authenticite et integrite, en s'aidant souvent"
	    + "de secrets ou cles. elle se distingue de la steganographie qui fait passer inapercu un message"
	    + "dans un autre message alors que la cryptographie rend un message inintelligible a autre que"
	    + "qui de droit. elle est utilisee depuis l'antiquite, mais certaines de ses methodes les plus"
	    + "importantes comme la cryptographie asymetrique, datent de la fin du vingtieme siecle.";

    static String texteEN = "cryptography prior to the modern age was effectively synonymous with encryption,"
	    + "the conversion of information from a readable state to apparent nonsense. the originator of an"
	    + "encrypted message shared the decoding technique needed to recover the original information"
	    + "only with intended recipients, thereby precluding unwanted persons from doing the same."
	    + "the cryptography literature often uses alice for the sender, bob for the intended recipient, and eve"
	    + "for the adversary.";

    static String texteCS = "kryptografie neboli sifrovani je nauka o metodach utajovani smyslu zprav prevodem"
	    + "do podoby, ktera je citelná jen se specialni znalosti. slovo kryptografie pochazi z rectiny kryptos"
	    + "je skryty a graphein znamena psat. Nekdy je pojem obecneji pouzivan pro vedu o cemkoli spojenem se "
	    + "siframi jako alternativa k pojmu kryptologie. kryptologie zahrnuje kryptografii a kryptoanalyzu, "
	    + "neboli lusteni zasifrovanych zprav.";
    
    static String notALetter = ";.:?!' "; 
    
    public static void main(String[] args) {
		System.out.println("french :" + analyze(texteFR));
		System.out.println("english :" + analyze(texteEN));
		System.out.println("czech :" + analyze(texteCS));
		
		System.out.println("french :" + analyzeDigram(texteFR));
		System.out.println("english :" + analyzeDigram(texteEN));
		System.out.println("czech :" + analyzeDigram(texteCS));
	}
    
    public static String analyze(String text) {
    	HashMap<Character, Integer> frequencies = new HashMap<Character, Integer>();
    	int len = text.length();
    	for (int i = 0; i < len; i++) {
    		Character c = text.charAt(i);
    		if (notALetter.indexOf(c) < 0) {
    			Integer oldFreq = frequencies.get(c);
    			if (oldFreq == null) {
    				oldFreq = 0;
    			}
    			frequencies.put(c, oldFreq + 1);
    		}
    	}
    	String out = "";
    	for (int i = 0; i < 6; i++) {
    		String maxKey = maxOfMap(frequencies).toString();
    		out += maxKey;
    		frequencies.remove(maxKey.charAt(0));
    	}
    	return out;
    }
    
    public static String analyzeDigram(String text) {
    	HashMap<String, Integer> frequencies = new HashMap<String, Integer>();
    	int len = text.length();
    	for (int i = 0; i < len - 1; i++) {
    		Character c = text.charAt(i);
    		Character c2 = text.charAt(i+1);
    		if (notALetter.indexOf(c) < 0 && notALetter.indexOf(c2) < 0) {
    			String key = "" + c + c2;
    			Integer oldFreq = frequencies.get(key);
    			if (oldFreq == null) {
    				oldFreq = 0;
    			}
    			frequencies.put(key, oldFreq + 1);
    		}
    	}
    	String out = "";
    	for (int i = 0; i < 5; i++) {
    		String maxKey = maxOfMap(frequencies).toString();
    		out += maxKey + ",";
    		frequencies.remove(maxKey);
    	}
    	String maxKey = maxOfMap(frequencies).toString();
		out += maxKey;
    	return out;
    }
    
    public static Object maxOfMap(HashMap hm) {
    	Set<Object> keys = hm.keySet();
    	Iterator<Object> iter = keys.iterator();
    	Object max = null;
    	Integer maxVal = null;
    	while (iter.hasNext()) {
    		Object key = iter.next();
    		if (max == null) {
    			max = key;
    			maxVal = (Integer) hm.get(key);
    		}
    		else {
	    		Integer val = (Integer) hm.get(key);
	    		if (val > maxVal) {
	    			max = key;
	    			maxVal = val;
	    		}
    		}
    	}
    	return max;
    }

}
