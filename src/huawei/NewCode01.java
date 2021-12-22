package huawei;

import java.util.Scanner;

public class NewCode01 {
	@SuppressWarnings("resource")
	public static void main(String arg[]) {
		Scanner sc = new Scanner(System.in);
		String ss = sc.next();
		int n = ss.length();
		int flag = 0;
		if(!(ss.contains("o"))) {
			System.out.print(n);
		} else {
			for(int i = 0; i < n; i++) {
				if('o' == ss.charAt(i))
					flag++;
			}
			if(flag%2 == 0) {
				System.out.print(n);
			} else {
				System.out.print(n - 1);
			}
		}	
	}
}
