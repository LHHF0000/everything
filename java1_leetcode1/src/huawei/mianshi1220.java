package huawei;

import java.util.Scanner;

/**
 * 一、给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。【简单】
示例 1：
输入：x = 121
输出：true

示例 2：
输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3：
输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数

示例 4：
输入：x = -101
输出：false

提示：
-231 <= x <= 231 - 1

 * @author Serein
 *
 */

public class mianshi1220 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int a = sc.nextInt();
//		int a = 121;
		if(a < 0) {
			System.out.print(false);
		}
		else {
			String s = String.valueOf(a);
			int n = s.length();
			String t = "";
			for(int i = n - 1; i >= 0; i--) {
				t += s.charAt(i);
			}
			if(t.equals(s)) {
				System.out.print(true);
			}else {
				System.out.print(false);
			}
		}		
	}
}
