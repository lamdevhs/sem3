import java.util.ArrayList;

public class StructureMystère {
	public ArrayList<Integer> contenu;
	public static Integer maxDispo = 7;
	StructureMystère() {
		this.contenu = new ArrayList<Integer>();
	}
	
	public int lastIndex() {
		return this.contenu.size() - 1;
	}
	
	public void soumettre(Integer i) throws ExceptionDonnéeRefusée {
		if (i == 5 || i == 13) { // was there any other way?
			throw new ExceptionDonnéeRefusée();
		}
		if (this.dispo() != 0) { // if struct not full
			if (this.dispo() != 7) { // if struct non empty
				Integer lastItem = this.contenu.get(this.lastIndex());
				if (lastItem > i) { // the order of items in the struct must be ascending
					throw new ExceptionDonnéeRefusée();
				}
				else {
					this.contenu.add(i);
				}
			}	
			else {
				this.contenu.add(i);
			}
			
		}
	}
	
	public int dispo() {
		return StructureMystère.maxDispo - this.contenu.size();
	}
	
	public void oublier() {
		if (this.dispo() != 7)
			this.contenu.remove(this.lastIndex());
	}
}
