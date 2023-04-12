package huawei;

import java.util.ArrayList;
import java.util.List;

/**
 * 给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
说明：
拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。
示例 1：
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
示例 2：
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。
示例 3：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
 * @author Serein
 *
 */
public class mianshi2 {
	@SuppressWarnings("unchecked")
	public static void main(String[] arg) {
		String s1 = "catsandog";
		List wordDict = new ArrayList<String>();
		wordDict.add("cats");
		wordDict.add("dog");
		wordDict.add("sand");
		wordDict.add("and");
		wordDict.add("cat");
		int n = s1.length();
		int m = wordDict.size();
		String w1 = (String) wordDict.get(0);
		String s2 = s1;
		for(int i = 0; i < m; i++) {			
			if(s2.contains((String) wordDict.get(i))) {
				s2 = s2.replaceAll((String) wordDict.get(i), "");
			}
		}
		if(s2.isEmpty()) {
			System.out.print(true);			
		}else {
			System.out.print(false);	
		}
	}
}
