package commandes;

import java.util.Vector;

public class Commande {
	int identifiant, codeStatus;
    public static int enCours = 0;
    public static int validée = 1;
    public static int livrée = 2;
    public static int payée = 3;

	Commande(int id, int cs){
		this.identifiant = id;
		this.codeStatus = cs;
	}
	
	public String statusToString() {
		int cs = this.codeStatus;
		if (cs == Commande.enCours) return "en cours";
		if (cs == Commande.validée) return "validée";
		if (cs == Commande.livrée) return "livrée";
		if (cs == Commande.payée) return "payée";
		return "(status non reconnu)";
	}
	
	public String toString() {
		return String.format("Commande: %d, status = %s",
				this.identifiant, this.statusToString());
	}
	
	public static void printCommandes(Vector<Commande> cmds) {
		for (Commande cmd: cmds) {
			System.out.println(cmd.toString());
		}
	}


}
