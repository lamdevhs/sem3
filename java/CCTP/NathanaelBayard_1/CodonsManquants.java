import java.util.ArrayList;
import java.util.HashSet;
import java.util.Iterator;

public class CodonsManquants {

	public static String sequence="gttagacggagccaccctttacaatgaccaccccttccgacaaacgacaaaaaatcacttcccactataaaggagctgctactcgaacccaataaaactactgtggataattatgtcgtatcgcatatatgctcatggtcccaccaatgaatccagatgttacgcttccgattgattacgggtaccgctgccgcatttagggggtgtagtactgcgggctctgga";

	public static Character[] nucléotides = {'a', 'c', 'g', 't'};
	
	public static HashSet<String> codons (String seq) throws Exception {
		HashSet<String> out = new HashSet<String>();
		
		int seqlen = seq.length();
		if (seqlen % 3 != 0)
			throw new Exception("invalid sequence");
		
		for (int i = 0; i < seqlen; i += 3) {
			String codon = "" + seq.charAt(i)
			  + seq.charAt(i+1)
			  + seq.charAt(i+2);
			out.add(codon);
		}
		
		return out;
	}
	
	public static ArrayList<String> combinaisons () {
		ArrayList<String> out = new ArrayList<String>();
		for (Character c1: nucléotides) {
			for (Character c2: nucléotides) {
				for (Character c3: nucléotides) {
					out.add("" + c1 + c2 + c3);
				}
			}
		}
		return out;
	}
	
	public static void main(String[] args) throws Exception {
		HashSet<String> codonsPresents = CodonsManquants.codons(CodonsManquants.sequence);
		ArrayList<String> tousLesCodons = CodonsManquants.combinaisons();
		Iterator<String> it = tousLesCodons.iterator();
		ArrayList<String> codonsManquants = new ArrayList<String>(); 
		while (it.hasNext()) {
			String combinaison = it.next();
			if (!codonsPresents.contains(combinaison))
				codonsManquants.add(combinaison);
		}
		System.out.println("Liste des codons manquants:");
		System.out.println(codonsManquants);
	}
}
