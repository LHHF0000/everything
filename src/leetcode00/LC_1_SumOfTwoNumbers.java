package leetcode00;

/**两数之和
 * 输入：nums = [2,7,11,15], target = 9
 * 输出：[0,1]
 * @date 2021.11.29
 */
public class LC_1_SumOfTwoNumbers {

	public static int[] myfunc(int[] nums, int target) {
		int n  = nums.length;
        int[] ans = new int[2];
        for(int i = 0; i < n; i++) {
            for(int j = i + 1; j < n; j++) {
                if(target == nums[i] + nums[j]) {
                    ans[0] = i;
                    ans[1] = j;
                    break;
                }
            }
        }
        return ans;
	}
	
	public static void main(String[] args) {
		int[] nums = new int[]{3,2,4};
		int target = 6;
		int[] an = myfunc(nums , target);
		System.out.print(an[0]);
		System.out.print(an[1]);
	}
}
