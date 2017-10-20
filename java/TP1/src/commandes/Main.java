package commandes;

import java.util.Vector;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		FichierClient fclient = new FichierClient();
		System.out.println("Clients qui n'ont jamais passé commande:");
		Vector<Client> clientVierges = fclient.clientsVierges();
		Client.printVectorClient(clientVierges);
		System.out.println("Clients qui n'ont jamais passé commande:");
		Vector<Commande> commandesEnCours = fclient.listerCommandes(Commande.enCours);
		Commande.printCommandes(commandesEnCours);
	}

}
