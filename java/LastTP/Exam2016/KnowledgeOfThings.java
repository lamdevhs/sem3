import java.util.HashMap;
import java.util.Scanner;

public class KnowledgeOfThings extends HashMap<Thing,String>{

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	
	KnowledgeOfThings() {
		Thing dot = new Thing();
		dot.color = "black";
		dot.shape = "round";
		dot.size = "small";
		this.put(dot, "a dot");
	}

	public static void main(String[] args) {
		KnowledgeOfThings know = new KnowledgeOfThings();
		Scanner sc = new Scanner(System.in);
		while(true) {
			Thing t = new Thing();
			System.out.print("I'm thinking about ");
			System.out.println(t);
			String ansNL = sc.nextLine();
		    String ans = ansNL.substring(0, ansNL.length() - 1);
			if (!know.containsKey(t)) {
				System.out.println("I didn't know! I'll remember it.");
				know.put(t, ans);
			}
			else {
				String expected = know.get(t);
				if (ans == expected) {
					System.out.println("Yes, that's it, kudos!");
				}
				else {
					System.out.print("Nah, the right answer was: ");
					System.out.println(expected);
					System.out.println("G'bye looser! :P");
					break;
				}
			}
		}
		sc.close();
	}
}
