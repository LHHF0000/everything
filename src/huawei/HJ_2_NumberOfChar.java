package huawei;

import java.util.*;

/**HJ2 计算某字符出现次数（较难）
 * 输入描述：第一行输入一个由字母和数字以及空格组成的字符串，第二行输入一个字符。
 * 输出描述：输出输入字符串中含有该字符的个数。（不区分大小写字母）
 * @date 2021.11.27
 */
public class HJ_2_NumberOfChar{

	@SuppressWarnings("resource")
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		String str = sc.nextLine().toLowerCase();
		String s = sc.nextLine().toLowerCase();
		System.out.print(str.length()-str.replaceAll(s,"").length());
	}
}

