package huawei;

import java.util.*;

/**HJ3 明明的随机数
 * 输入描述：注意：输入可能有多组数据(用于不同的调查)。每组数据都包括多行，第一行先输入随机整数的个数 N ，
 * 				 接下来的 N 行再输入相应个数的整数。具体格式请看下面的"示例"。
 * 输出描述：返回多行，处理后的结果
 * @date 2021.11.28
 */
public class HJ_3_RandomNumber {
    @SuppressWarnings({ "resource", "rawtypes", "unchecked" })
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNext()){ 
        	int num = sc.nextInt(); 
	        TreeSet set = new TreeSet();
	        for(int i = 0; i < num; i++){
	        	set.add(sc.nextInt()); 
	        } 	        
	        Iterator iterator = set.iterator(); 
	        while(iterator.hasNext()){ 
	        	System.out.println(iterator.next()); 
	        } 
        } 
    } 
}