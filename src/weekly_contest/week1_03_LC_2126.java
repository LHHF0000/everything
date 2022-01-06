package weekly_contest;

/**摧毁小行星
 * 题解
 * @date 2022.1.5
 */
public class week1_03_LC_2126 {
	public static boolean asteroidsDestroyed(int mass, int[] asteroids) {
		int n = asteroids.length;
		int M = 17, W = 100005;
		int[] v = new int[M];
		long[] sum = new long[M];
		for(int i = 0; i < M; i++) v[i] = W;
		for(int x : asteroids) {
			int p = fuc(x);
			v[p] = Math.min(v[p], x);
			sum[p] = Math.min(W, sum[p] + x);
			//sum[p] += x;
		}
		for(int i = 0; i < M; i++) {
			if(v[i] < W && mass < v[i]) return false;	//v[i] < W表示改桶丢入了数据
			mass += sum[i];
		}
		return true;
	}
	
	public static int fuc(int n) {
		for(int i = 16; i >= 0; i--) {
			if(1 == ((n >> i) & 1))		//移位运算
				return i;				
		}
		return 0;
	}
	
	public static void main(String arg[]) {
		int mass = 263;
		int[] asteroids = {15};
		System.out.print(asteroidsDestroyed(mass, asteroids));
	}
}
