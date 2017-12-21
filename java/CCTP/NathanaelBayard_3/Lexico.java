import java.util.ArrayList;
import java.util.Iterator;

public class Lexico {
	public HashMapLexico premièresLettres;
	Lexico() {
		premièresLettres = new HashMapLexico();
	}
	
	public void ajouterMot(String mot) {
		mot = mot + "!";
		HashMapLexico here = this.premièresLettres;
		for (int i = 0; i < mot.length(); i++) {
			Character c = mot.charAt(i);
			if (here.containsKey(c)) {
				here = here.get(c);
			}
			else {
				HashMapLexico newHML = new HashMapLexico();
				here.put(c, newHML);
				here = newHML;
			}
		}
	}
	
	public HashMapLexico localiser(String prefix) {
		HashMapLexico here = this.premièresLettres;
		for (int i = 0; i < prefix.length(); i++) {
			Character c = prefix.charAt(i);
			if (here.containsKey(c)) {
				here = here.get(c);
			}
			else { throw new ExceptionPréfixeInconnu(); }
		}
		return here;
	}
	
	public ArrayList<String> compléterPréfixe(String prefix, HashMapLexico hml) {
		ArrayList<String> out = new ArrayList<String>();
		Iterator<Character> it = hml.keySet().iterator();
		while (it.hasNext()) {
			char c = it.next();
			if (c == '!') out.add(prefix);
			else {
				ArrayList<String> recOut = this.compléterPréfixe(prefix + c, hml.get(c));
				out.addAll(recOut);
			}
		}
		return out;
	}
	
	public ArrayList<String> suggestions(String prefix) {
		HashMapLexico hml = this.localiser(prefix);
		return compléterPréfixe(prefix, hml);
	}
	
	public static void main(String[] args) {
		Lexico l = new Lexico();
		// le point d'exclam final est rajouté dans la methode
		// ajouterMot
		l.ajouterMot("arbre");
		l.ajouterMot("bac");
		l.ajouterMot("barrer");
		l.ajouterMot("caler");
		l.ajouterMot("cale");
		l.ajouterMot("carton");
		l.ajouterMot("carte");
		l.ajouterMot("camion");
		l.ajouterMot("cire");
		l.ajouterMot("citron");
		l.ajouterMot("cintre");
		l.ajouterMot("citer");
		l.ajouterMot("clamer");
		l.ajouterMot("colt");
		l.ajouterMot("cou");
		l.ajouterMot("court");
		l.ajouterMot("cours");
		
		String[] prefixes = { "a", "b", "ca", "ci",
				"car", "cou", "cale" };
		for (String p: prefixes) {
			System.out.println("Suggestions pour '" + p + "' :");
			System.out.println(l.suggestions(p));
		}
		
	}
}
