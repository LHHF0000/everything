package leetcode00;

import java.util.HashSet;
import java.util.Set;

/** leetcode 3 无重复字符的最长子串
 * @date 2021.9.28
 */
public class LC_3_LengthOfLongestSubstring {

	public static int myfunc(String s) {
		
        Set<Character> occ = new HashSet<Character>();     // 哈希集合，记录每个字符是否出现过
        int n = s.length(); 
        int rk = -1, ans = 0;		// 右指针，初始值为 -1，相当于我们在字符串的左边界的左侧，还没有开始移动        
        for (int i = 0; i < n && n - rk + 1 > ans; ++i) {
            if (i != 0) {  
                occ.remove(s.charAt(i - 1));	// 左指针向右移动一格，移除一个字符
            }
            while (rk + 1 < n && !occ.contains(s.charAt(rk + 1))) { 
                occ.add(s.charAt(rk + 1));		// 不断地移动右指针
                ++rk;
            }
            ans = Math.max(ans, rk - i + 1);		// 第 i 到 rk 个字符是一个极长的无重复字符子串
        }
        return ans;		            
		}
	
	public static void main(String[] args){
		String myString = "augenstern";
		System.out.println(myfunc(myString));
	}
}
