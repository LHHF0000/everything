package huawei;

import java.util.Scanner;

/**HJ1 字符串最后一个单词的长度（较难）
 * 计算字符串最后一个单词的长度，单词以空格隔开，字符串长度小于5000。（注：字符串末尾不以空格为结尾）
 * @date 2021.11.27
 */
public class HJ_1_LengthOfLastWord {
	
	// 反过来打印
	@SuppressWarnings("resource")
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		String str = sc.nextLine();
		int count = 0;
		for(int i = str.length() - 1; i >= 0; i--) {
			if(' ' == str.charAt(i)) {
				break;
			}
			count++;
		}
		System.out.print(count);
	}
	
	// 按空格分割
//	@SuppressWarnings("resource")
//	public static void main(String[] args){
//	    Scanner sc = new Scanner(System.in);
//	    String str = sc.nextLine();
//	    String[] s = str.split(" "); //正则表达式实用性更强( str.split("\\s+"))
//	    int length = s[s.length - 1].length();
//	    System.out.println(s);
//	    System.out.println(length);
//	}
}
