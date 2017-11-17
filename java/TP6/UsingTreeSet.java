import java.util.TreeSet;

public class UsingTreeSet {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String text = "Je fais souvent ce rêve étrange et pénétrant" 
				+ " D une femme inconnue et que j aime et qui m aime"
				+ " Et qui n est chaque fois ni tout à fait la même"
				+ " Ni tout à fait une autre et m aime et me comprend"
				+ ""
				+ " Car elle me comprend et mon coeur transparent"
				+ " Pour elle seule hélas cesse d être un problème"
				+ " Pour elle seule et les moiteurs de mon front blême "
				+ " Elle seule les sait rafraîchir en pleurant "
				+ ""
				+ " Est elle brune blonde ou rousse Je l ignore"
				+ " Son nom Je me souviens qu il est doux et sonore"
				+ " Comme ceux des aimés que la Vie exila " 
				+ "" 
				+ " Son regard est pareil au regard des statues"
				+ " Et pour sa voix lointaine et calme et grave elle a"
				+ " L inflexion des voix chères qui se sont tues";
		String[] words = text.split(" ");
		
		TreeSet<String> ts = new TreeSet<String>();
		for (String word: words) {
			ts.add(word);
		}
		System.out.println(String.valueOf(ts.size()));
	}

}
