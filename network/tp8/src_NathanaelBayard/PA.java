
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;
public class PA {
	public static void main(String[] args) {
		ServerSocket server;
		Socket connection;
		String quitString = ":q";
		//String quitStringLn = quitString;
		try{
			server = new ServerSocket(4444);
			System.out.println("Waiting for a client to connect...");
			connection = server.accept();
			System.out.println("A client has connected! :)");
			BufferedReader fromClient = new BufferedReader( new InputStreamReader( connection.getInputStream() ) );
			PrintWriter toClient = new PrintWriter( connection.getOutputStream(), true);
			System.out.println("[waiting for PB to say something]");
			Scanner fromConsole = new Scanner(System.in);
			
			String msgFromClient = fromClient.readLine();
			if (msgFromClient.compareTo(quitString) == 0) {
				System.out.print("Quitting (triggered by the client).");
			}
			else {
				System.out.println("[PB says] " + msgFromClient);
				
				System.out.println("Enter something for the client. type `"+ quitString
						+ "` to quit.");
				
				while (true) {
					String msgFromConsole = fromConsole.nextLine();
					toClient.println(msgFromConsole);
					if (msgFromConsole.compareTo(quitString) == 0) {
						System.out.print("Quitting.");
						break;
					}
					msgFromClient = fromClient.readLine();
					if (msgFromClient.compareTo(quitString) == 0) {
						System.out.print("Quitting (triggered by the client).");
						break;
					}
					System.out.println("[PB says] " + msgFromClient);
				}
			}
			connection.close();
			fromConsole.close();
		}
		catch(IOException i){
			System.out.println("Impossible d'écouter sur le port 4444: serait-il occupé?");
		}
	}
}