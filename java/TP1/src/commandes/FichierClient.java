package commandes;

import java.util.Vector;

public class FichierClient {
	Vector<Client> catalogue;
	
	FichierClient() {
		this.catalogue = new Vector<Client>();
		Client martin = new Client(
				"Martin", "Valérie", "Albi");
		martin.ajouterCommande(12897, Commande.enCours);
		martin.ajouterCommande(86416, Commande.validée);
		martin.ajouterCommande(98716, Commande.livrée);
		this.catalogue.addElement(martin);
		
		Client ndiaye = new Client(
				"Ndiaye", "Marie", "Dakar");
		ndiaye.ajouterCommande(61573, Commande.enCours);
		ndiaye.ajouterCommande(36475, Commande.livrée);
		this.catalogue.addElement(ndiaye);
		
		Client smith = new Client(
				"Smith", "Peter", "New-York");
		this.catalogue.addElement(smith);
		
	}
	
	public Vector<Client> clientsVierges() {
		Vector<Client> v = new Vector<Client>();
		for (Client c: this.catalogue){
			if (c.historique.size() == 0) {
				v.addElement(c);
			}
		}
		return v;
	}
	
	public Vector<Commande> listerCommandes(int code) {
		Vector<Commande> v = new Vector<Commande>();
		for (Client c: this.catalogue){
			for (Commande cmd: c.historique) {
				if (cmd.codeStatus == code) {
					v.addElement(cmd);
				}
			}
		}
		return v;
	}
}
