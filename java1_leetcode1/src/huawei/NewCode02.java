package huawei;
public class NewCode02 {
	public static String myfunc(String s) {
		String ans = new String();
		String[] r = s.split(",");
		int n = r[0].length();
		int m = r[1].length();		
		if(0 == n && 0 == m) {
			ans = "/";
		}
		else {
			char a = r[0].charAt(n-1);
			char b = r[1].charAt(0);
			if('/' == a && '/' == b) {
				String r1 = "";
				for(int i = 1; i < m; i++) {
					r1 += r[1].charAt(i);
				}
				ans = r[0] + r1;
			} else if('/' == a || '/' == b) {
				ans = r[0] + r[1];
			} else {
				ans = r[0] + "/" + r[1];
			}			
		}
		return ans;
	}
	public void main() {
		System.out.print(myfunc("/acd,bef"));
	}
}
