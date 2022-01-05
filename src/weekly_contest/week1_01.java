package weekly_contest;

import java.util.ArrayList;
import java.util.Scanner;

public class week1_01 {
	 public static boolean checkString(String s) {
		 int n = s.length();
		 int a = -1, b = n;
		 
		 for(int i = 0; i < n; i++) {
			 if('b' == s.charAt(i)) {
				 b = i;
				 break;
			 }
		 }
		 for(int j = n - 1; j > 0; j--) {
			 if('a' == s.charAt(j)) {
				 a = j;
				 break;
			 }
		 }
		 if(a < b) {
			 return true;
		 } else {
			 return false;
		 }
		 
	 }
	 
	 public static void main(String arg[]) {
		 Scanner sc = new Scanner(System.in);
		 String r = sc.next();
		 System.out.print(checkString(r));
	 }
}
