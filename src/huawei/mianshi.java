package huawei;

/**
 * 给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。
输入为三个整数：day、month 和 year，分别表示日、月、年。

您返回的结果必须是这几个值中的一个 {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}。

示例 1：
输入：day = 31, month = 8, year = 2019
输出："Saturday"

示例 2：
输入：day = 18, month = 7, year = 1999
输出："Sunday"

1971年的1月1日是星期5

 * @author Serein
 *
 */
public class mianshi {
	public static void main(String s[]) {
		int day = 31;
		int month = 8;
		int year = 2019;
		int day0 = 1;
		int month0 = 1;
		int year0 = 1971;
		
		int[] mon = {31,28,31,30,31,30,31,31,30,31,30,31};
		int ans = 0;		
		
		for(int m = month; m > 0; m--) {
			int days = mon[m-1];
			for(int i = days; i > 0; i--) {
				ans++;
			}
		}
		
		for(int y = year; y > year0; y--) {
			ans += 365;
		}
		String[] arg = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
		System.out.print(arg[(ans+5)%7]);
		
	}
//	public static void main(String arg[]) {
//		String ar = "day = 31, month = 8, year = 2019";
//		int n = ar.length();
//		String 
//		System.out.print(ar.charAt(6));
//	}
}
