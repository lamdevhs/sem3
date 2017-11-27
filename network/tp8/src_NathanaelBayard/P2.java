import java.io.IOException;
import java.net.Inet4Address;
import java.net.InetAddress;
import java.net.UnknownHostException;
public class P2 {

	public static void main(String[] args) {
		InetAddress addr;
		String ip = "127.0.1.1"; //ifconfig n'est pas installe sur mon poste
		try {
			addr = Inet4Address.getByName(ip);
			if (addr.isReachable(1000)) System.out.println("Node " + ip + " is reachable!");
		}
		catch(UnknownHostException e) {
			e.printStackTrace();
		}
		catch (IOException i) {
			i.printStackTrace();
		}

	}

}
