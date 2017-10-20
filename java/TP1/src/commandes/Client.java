package commandes;

import java.util.Vector;

public class Client {
	String nom, prénom, ville;
	Vector<Commande> historique;
	Client(String n, String p, String v) {
		this.nom = n;
		this.prénom = p;
		this.ville = v;
		this.historique = new Vector<Commande>();
	}
	public void ajouterCommande(int id, int cs) {
		Commande c = new Commande(id, cs);
		this.historique.addElement(c);
	}
	public String toString() {
		return String.format("%s %s (%s)",
				this.prénom,
				this.nom,
				this.ville);
	}
	
	public static void printVectorClient(Vector<Client> cs) {
		for (Client c: cs) {
			System.out.println(c.toString());
		}
	}
}
