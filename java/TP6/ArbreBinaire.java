
/**
 * ArbreBinaire d'éléments comparables
 * @author David Panzoli
 *
 */
public class ArbreBinaire<Element extends Comparable<Element>> {

	protected Element étiquette;
	protected ArbreBinaire<Element> sag;
	protected ArbreBinaire<Element> sad;

	public ArbreBinaire() {
		this.étiquette = null;
		this.sag = null;
		this.sad = null;
	}

	public ArbreBinaire(Element r, ArbreBinaire<Element> g, ArbreBinaire<Element> d) {
		this.étiquette = r;
		this.sag = g;
		this.sad = d;
	}

	public boolean estVide() {
		return this.étiquette==null;
	}

	public Element racine() {
		if (this.estVide()) throw new ExceptionArbreVide();
		return this.étiquette;
	}

	public ArbreBinaire<Element> sag() {
		if (this.estVide()) throw new ExceptionArbreVide();
		return this.sag;
	}

	public ArbreBinaire<Element> sad() {
		if (this.estVide()) throw new ExceptionArbreVide();
		return this.sad;
	}

	public int taille() {
		if (this.estVide()) return 0;
		else return 1 + this.sag().taille() + this.sad().taille();
	}

	public int hauteur() {
		if (this.estVide()) return 0;
		else return 1 + Math.max(this.sag().hauteur(), this.sad().hauteur());
	}
	
	public String toString() {
		String out = "";
		if (!this.estVide()) {
			if (!this.sag().estVide()) out+= this.sag().toString();
			out += this.racine().toString();
			if (!this.sad().estVide()) out+= this.sad().toString();
		}
		return "("+out+")";
	}

}
