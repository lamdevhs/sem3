
public class ABR<Element extends Comparable<Element>> extends ArbreBinaire<Element> {
	public ABR() {
		super();
	}
	public ABR(Element r, ABR<Element> g, ABR<Element> d) {
		super(r, g, d);
	}
	
	public ABR<Element> sad() {
		return (ABR<Element>) this.sad;
	}

	public ABR<Element> sag() {
		return (ABR<Element>) this.sad;
	}
	
	public void insérer(Element e) {
		if (this.estVide()) {
			this.étiquette = e;
			this.sad = new ABR<Element>();
			this.sag = new ABR<Element>();
			return;
		}
		else if (this.étiquette.compareTo(e) == -1) {
			this.sad().insérer(e);
		}
		else {
			this.sag().insérer(e);
		}
	}
	
	public boolean rechercher(Element e) {
		if (this.estVide()) return false;
		if (this.étiquette.equals(e)) return true;
		if (this.étiquette.compareTo(e) == -1)
			return this.sad().rechercher(e);
		else
			return this.sag().rechercher(e);
	}
	
	public void supprimer(Element e) {
		if (this.estVide()) return;
		if (this.étiquette.equals(e)) {
			if (this.sag.estVide()) {
				ABR<Element> oldSAD = this.sad();
				this.sag = oldSAD.sag();
				this.sad = oldSAD.sad();
				this.étiquette = oldSAD.étiquette;
				return;
			}
			Element max = this.sag().max();
			this.sag().supprimer(max);
			this.étiquette = max;
		}
		else if (this.étiquette.compareTo(e) == -1){
			this.sad().supprimer(e);
		}
		else {
			this.sag().supprimer(e);
		}
	}
	
	public Element max() {
		if (this.estVide()) return null;
		if (this.sag.estVide())
				return (Element) this.étiquette;
		else return this.sad().max();
	}
	
	public static void main(String[] args) {
		ABR<Character> abr = new ABR<Character>();
		String str = "mgpcjotaehknrvv";
		for (int i = 0; i<str.length(); i++) {
			abr.insérer(str.charAt(i));
		}
		for (int i = 0; i<str.length(); i++) {
			System.out.println(abr.rechercher(str.charAt(i)));
		}
		System.out.println(abr.taille());
		for (int i = 0; i<str.length(); i++) {
			abr.supprimer(str.charAt(i));
		}
		System.out.println(abr.taille());
		
	}
}
