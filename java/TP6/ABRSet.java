
public class ABRSet<Element extends Comparable<Element>> extends ABR<Element> implements Ensemble<Element> {
	
	public ABRSet() {
		super();
	}
	
	private ABRSet<Element>  _build(Element r, ABRSet<Element> g, ABRSet<Element> d) {
		return (ABRSet<Element>) new ABR(r, g, d);
	}
	
	public void ajouter(Element e) {
		if (this.contient(e) == false)
			this.insérer(e);
		
	}

	public void enlever(Element e) {
		this.supprimer(e);
		// TODO Auto-generated method stub
		
	}

	public boolean contient(Element e) {
		// TODO Auto-generated method stub
		return this.rechercher(e);
	}

	@Override
	public int cardinalité() {
		// TODO Auto-generated method stub
		return this.taille();
	}

}
