package leetcode00;

/**leetcode 121 买卖股票的最佳时机
 * 思路：记录历史最低价格、计算prices[i]-min
 * @date 2021.9.29
 */
public class LC_121_MaxProfit {
	public static int myfunc(int[] prices){
		int ans = 0;
		int n = prices.length;
		int min = prices[0];
		if(n < 2)
			return 0;
		for(int i = 1; i < n; i++){
			ans = Math.max(ans, prices[i] - min);
			min = Math.min(min, prices[i]);
		}
		return ans;
	}
	public static void main(String[] args){
		int[] prices = {1,2,3};
		System.out.println(myfunc(prices));
	}
}
