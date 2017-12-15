import java.util.ArrayList;

public class YM {
  int y;
  int m;
  boolean leapYear;
  static int[] monthSize =
	  {-1,31,28,31,30, //.. april
		31,30,31,31, //.. august
		30,31,30,31}; //.. december
  
  YM(int y, int m) throws InvalidMonth {
	  if (m > 12 || m < 1) {
		  InvalidMonth im = new InvalidMonth();
		  im.val = m;
		  throw im;
	  }
	  this.y = y;
	  this.m = m;
	  this.leapYear = YM.leapYear(y);
  }
  
  static boolean leapYear(int y){
	  if (y % 4 != 0) return false;
	  if (y % 100 != 0) return true;
	  if (y % 400 != 0) return false;
	  return true;
  }
  
  int monthSize() {
	  if (this.m == 2 && this.leapYear)
		  return 29;
	  else return YM.monthSize[this.m];
  }
  
  static YM fromStr(String s) throws InvalidYM, InvalidMonth {
	  int slash = s.indexOf("/");
	  if (slash == -1) throw new InvalidYM();
	  int y = Integer.parseInt(s.substring(0, slash));
	  int m = Integer.parseInt(s.substring(slash+1));
	  return new YM(y, m);
  }
  
  public String toString() {
	  return String.valueOf(this.y) + "/"
			  + String.valueOf(this.m);
  }
  
  public static void main(String[] args) {
	String[] strs = {
			"2005/02",
			"2015/04",
			"2016/03",
			"2014",
			"2015/14",
			"2000/02",
			"2013/07"
	};
	for (String s: strs) {
		YM ym;
		try {
			ym = YM.fromStr(s);
			System.out.print(ym);
			System.out.print(" -> ");
			System.out.print(ym.monthSize());
			System.out.println(" jours");
		} catch (InvalidYM e) {
			// TODO Auto-generated catch block
			System.out.print(s);
			System.out.print(" -> ");
			System.out.println("Le format est incomplet");
		} catch (InvalidMonth e) {
			System.out.print(s);
			System.out.print(" -> ");
			System.out.println(String.format(
					"Le mois est invalide (%d>%d)", e.val, 12));
		}
	}
}
}
