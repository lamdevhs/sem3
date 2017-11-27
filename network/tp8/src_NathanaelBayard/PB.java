
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;
public class PB {
	public static void main(String[] args) throws IOException {
		InetAddress addr;
		Socket connection;
		String quitString = ":q";
		String msgFromConsole;
		try{
			connection = new Socket("localhost", 4444);
			int port = connection.getLocalPort();
			System.out.println("This client uses the local port = " + port);
			System.out.println("Enter something for the server, type: `"+ quitString
						+ "` to quit.");
			
			BufferedReader fromServer = new BufferedReader( new InputStreamReader( connection.getInputStream() ) );
			PrintWriter toServer = new PrintWriter( connection.getOutputStream(), true);
			Scanner fromConsole = new Scanner(System.in);
			while (true) {
				msgFromConsole = fromConsole.nextLine();
				toServer.println(msgFromConsole);
				if (msgFromConsole.compareTo(quitString) == 0) {
					System.out.print("Quitting.");
					break;
				}
				String msgFromServer = fromServer.readLine();
				if (msgFromServer.compareTo(quitString) == 0) {
					System.out.print("Quitting (triggered by the server).");
					break;
				}
				System.out.println("[PA says] " + msgFromServer);
			}
			connection.close();
			fromConsole.close();
		} catch(UnknownHostException e){
			e.printStackTrace();
		}
		catch(IOException ioe){}
		
	}
}