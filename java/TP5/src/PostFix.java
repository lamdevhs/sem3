
public class PostFix {
	static String digits = "0123456789"; 
	static String operators = "+-*/";
	static int[] priorities = {1,1,2,2};
	
	public static int eval (String expr) throws StackEmptyException, IncorrectPostFixExpr{
		Stack operands = new Stack();
		int elen = expr.length();
		for (int i = 0; i < elen; i++) {
			char c = expr.charAt(i);
			int maybeInt = PostFix.evalDigit(c);
			if (maybeInt >= 0) {
				operands.cover(maybeInt);
				continue;
			}
			
			int ix = operators.indexOf(c);
			if (ix < 0) {
				// unrecognized char:
				throw new IncorrectPostFixExpr("Unrecognized char");
			}
			if (operands.isEmpty()) throw new IncorrectPostFixExpr("Operands lacking");
			int b = (int) operands.getTop(); operands.uncover();
			if (operands.isEmpty()) throw new IncorrectPostFixExpr("Operands lacking");
			int a = (int) operands.getTop(); operands.uncover();
			int res = evalOp(c, a, b);
			operands.cover(res);
		}
		return (int) operands.getTop();
	}
	
	private static int evalOp(char c, int a, int b) throws IncorrectPostFixExpr {
		switch (c){
			case '+': return a + b;
			case '-': return a - b;
			case '*': return a * b;
			case '/': return a / b;
			default: throw new IncorrectPostFixExpr("Unsupported operator");
		}
	}

	public static int evalDigit(char c) {
		int ix = PostFix.digits.indexOf(c);
		if (ix < 0) return -1;
		else return ix;
	}
	
	public static String fromInfix(String expr) throws StackEmptyException, IncorrectPostFixExpr {
		Stack stack = new Stack();
		String out = "";
		int elen = expr.length();
		for (int i = 0; i < elen; i++) {
			char c = expr.charAt(i);
			
			//stack.print();
			//System.out.println("out = " + out);
			//System.out.println("----------------\n");
			//System.out.println(c);
			
			int ixDigit = digits.indexOf(c);
			if (ixDigit >= 0) {
				//System.out.println(">> is digit");
				out += c;
				continue;
			}
			if (c == '(') {
				//System.out.println(">> is (");
				stack.cover(c);
				continue;
			}
			if (c == ')') {
				//System.out.println(">> is )");
				char top = (char) stack.getTop(); 
				while (top != '(') {
					out += top;
					stack.uncover();
					top = (char) stack.getTop();
				}
				stack.uncover();
				continue;
			}
			
			//System.out.println(">> is operator");
			while (true) {
				boolean isEmpty = stack.isEmpty();
				if (isEmpty) break;
				
				char top = (char) stack.getTop();
				int priorityTop = priority(top);
				int priorityCurrent = priority(c);
				if (priorityTop < priorityCurrent) break;
				
				out += top;
				
				stack.uncover();
			}
			stack.cover(c);
		}
		
		boolean isEmpty = stack.isEmpty();
		while (!isEmpty) {
			char top = (char) stack.getTop();
			out += top;
			stack.uncover();
			isEmpty = stack.isEmpty();
		}
		return out;
	}
	
	public static int priority(char op) throws IncorrectPostFixExpr {
		if (op == '(') return 0;
		int ix = operators.indexOf(op);
		if (ix < 0) throw new IncorrectPostFixExpr("Unknown operator " + op);
		return priorities[ix];
	}
	
	public static void main(String[] args) throws StackEmptyException, IncorrectPostFixExpr {
		String[] tests = {"328*4-+", "12+3+", "12+3*", "123*+", "27+85-*"};
		int tlen = tests.length;
		for (int i = 0; i < tlen; i++) {
			System.out.println(tests[i]);
			System.out.println(PostFix.eval(tests[i]));
		}
		System.out.println("======");
		String[] testsInfix = {"3+((2*8)-4)", "(1+2)+3", "(1+2)*3", "1+(2*3)", "(2+7)*(8-5)"};
		int inlen = testsInfix.length;
		for (int i = 0; i < inlen; i++) {
			System.out.println(testsInfix[i]);
			String converted = PostFix.fromInfix(testsInfix[i]);
			System.out.println(converted);
			System.out.println(converted.equals(tests[i]));
		}
	}
}
