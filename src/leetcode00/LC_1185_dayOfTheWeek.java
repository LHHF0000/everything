package leetcode00;

/**一周中的第几天
 * 已知：1971.1.1是星期五
 * 2021年华为OD 
 * @date 2022.1.8
 * 43/43
 */
public class LC_1185_dayOfTheWeek {
	public static String dayOfTheWeek(int day, int month, int year) {
		int[] mon = {31,28,31,30,31,30,31,31,30,31,30,31};
		if((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) 
			mon[1] =29;
		int ans = 0;		
		ans = day - 1;
		for(int m = month; m > 1; m--) {
			ans += mon[m - 2];
		}		
		for(int y = year; y > 1971; y--) {
			if(((y-1) % 4 == 0 && (y-1) % 100 != 0) || ((y-1) % 400 == 0)) 
				ans += 366;
			else 
				ans += 365;
		}
		System.out.println(ans);
		String[] arg = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
		return arg[(ans + 5) % 7];		
	}
	public static void main(String arg[]) {
		System.out.print(dayOfTheWeek(15, 8, 1993));
	}
}

