
public class LigneCommande {
	String article;
	double prixUnitaire;
	int quantité;
	
	LigneCommande(String a, double pu, int q){
		this.article = a;
		this.prixUnitaire = pu;
		this.quantité = q;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		LigneCommande l1 =
				new LigneCommande("Bac 16L, tri-matière renforcé", 86.80, 1);
		LigneCommande l2 =
				new LigneCommande("Protection ThermaQuiet aluminium noir", 14.90, 1);
		LigneCommande l3 =
				new LigneCommande("Fixation à clip 1/8\" 6.5mm", 4.35, 5);
		
		LigneCommande[] lignes = {l1,l2,l3};
		
		double totalPrice = 0;
		for (LigneCommande l: lignes) {
			totalPrice += l.prixUnitaire * l.quantité;
		}
		System.out.println(String.format("Total price = %f", totalPrice));
	}

}
