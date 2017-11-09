
public class Expr {
	public static void main(String[] args) throws Exception {
		BinaryTree expr = new BinaryTree(
			'+',
			new BinaryTree(
				'-',
				BinaryTree.leaf(5),
				new BinaryTree(
					'*',
					BinaryTree.leaf(2),
					BinaryTree.leaf(6))),
			new BinaryTree(
				'*',
				new BinaryTree(
					'+',
					BinaryTree.leaf(5),
					new BinaryTree(
						'/',
						BinaryTree.leaf(6),
						BinaryTree.leaf(2))),
				BinaryTree.leaf(3)));
		System.out.println(expr.size());
		System.out.println(expr.height());
		int res = Expr.evalExpr(expr);
		System.out.println(res);
		
		foo();
	}
	
	public static void foo() throws Exception {
		ArrayBinaryTree t = new ArrayBinaryTree(
				"abcde ghi k  n ");
		System.out.println(t.height());
	}
	
	public static int evalExpr(BinaryTree b) throws Exception{
		if (b.isLeaf()) return (int)b.root();
		if (b.left().isEmpty() || b.right().isEmpty())
			// b has only one child, which is forbidden
			// (an expr is a strict binary tree)
			throw new Exception("InvalidExpression"); 
		if (b.isEmpty()) throw new Exception("EmptyExpression");
		// otherwise, b does have two non-null children 
		int evalLeft = Expr.evalExpr(b.left());
		int evalRight = Expr.evalExpr(b.right());
		return Expr.evalOp((char)b.root(), evalLeft, evalRight);
	}
	
	public static int evalOp(char c, int a, int b) throws Exception {
		switch (c) {
			case '+': return a + b;
			case '-': return a - b;
			case '/': return a / b;
			case '*': return a * b;
			default: throw new Exception("Invalid Expression");
		}
	}
}
