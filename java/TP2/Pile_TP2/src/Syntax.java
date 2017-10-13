
public class Syntax {
	static String openers = "([{";
	static String closers = ")]}";
	
	public static boolean parenMatch(char expectedOpener, char closer) {
		int ixCloser = Syntax.openers.indexOf(expectedOpener);
		if (ixCloser < 0) return false;
		char expectedCloser = Syntax.closers.charAt(ixCloser);
		if (expectedCloser == closer) return true;
		else return false;
	}
	
	public static boolean isValidOpener(char opener) {
		return Syntax.openers.indexOf(opener) >= 0;
	}
	
	public static boolean check(String s) throws StackEmptyException {
		Stack parens = new Stack();
		int len = s.length();
		for (int i = 0; i < len; i++) {
			char c = s.charAt(i);
			int ixOpener = Syntax.openers.indexOf(c);
			if (ixOpener >= 0) {
				parens.cover(c);
				continue;
			}
			
			int ixCloser = Syntax.closers.indexOf(c);
			if (ixCloser >= 0) {
				if (parens.isEmpty()) {
					return false;
				}
				char expectedOpener = (char) parens.getTop();
				if (Syntax.parenMatch(expectedOpener, c)) {
					parens.uncover();
				}
				else return false;
			}
		}
		if (parens.isEmpty()) return true;
		//otherwise
		return false;
	}
	
	
	public static void main(String[] args) throws StackEmptyException {
		String test1 = "e<-sommet(empiler(empiler(depiler(empiler(pile_vide(),a)),b),c))";
		String test2 = "(define (smallest L A)"
				+ "(cond ( (null? L) A)"
				+ "( (< (car L) A) (smallest (cdr L)(car L)))"
				+ "(else (smallest (cdr L) A ))"
				+ ")"
				+ ")";
		String test3 = "print(L[len(L)//2-1],L[len(l)//2])";
		String test4 =
				"$('form div').filter('span .actif').each(function() {"
				+ "$(this).bind('click', function() {"
				+ "$(this).prop('disabled', true);"
				+ "});"
				+ "});";
		String[] tests = {test1, test2, test3, test4};
		int tlen = tests.length;
		for (int i = 0; i < tlen; i++) {
			System.out.println(tests[i]);
			System.out.println(Syntax.check(tests[i]));
		}
	}
}
