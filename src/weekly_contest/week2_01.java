package weekly_contest;

import java.util.HashSet;
import java.util.Set;

/**5976.检查是否每一行每一列都包含全部整数
 * @date 2022.1.9
 * 214/214
 */
public class week2_01 {
	public static boolean checkValid(int[][] matrix) {
		int n = matrix[0].length;
		int flag = 0;
		Set<Integer> o = new HashSet<Integer>();		
		for(int i = 0; i < n; i++) {
			o.add(i + 1);
		}
		for(int i = 0; i < n; i++) {
			int[] tmp = matrix[i];
			Set<Integer> t = new HashSet<Integer>();
			t.addAll(o);
			for(int j = 0; j < n; j++) {
				if(t.contains(tmp[j])) {
					t.remove(tmp[j]);
				}					
				else {
					flag = 1;
					break;
				}					
			}
		}
		for(int i = 0; i < n; i++) {
			Set<Integer> t = new HashSet<Integer>();
			t.addAll(o);
			for(int j = 0; j < n; j++) {
				if(t.contains(matrix[j][i])) {
					t.remove(matrix[j][i]);
				} else {
					flag = 1;
					break;
				}
			}
		}
		if(1 == flag) {
			return false;
		} else {
			return true;
		}		
    }
	public static void main(String[] arg) {
		int[][] test = {{1,2,3},{3,1,2},{2,3,1}};
		System.out.print(checkValid(test));
	}
}
