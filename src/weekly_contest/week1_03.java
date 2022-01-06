package weekly_contest;

import java.util.ArrayList;

/**摧毁小行星
 * 自己想的思路
 * @date 2022.1.5
 * 超出时间限制：49/67
 */
public class week1_03 {
	public static boolean asteroidsDestroyed(int mass, int[] asteroids) {
		int mass0 = mass;
		int n = asteroids.length;
		int flag = 0;
		ArrayList list = new ArrayList<Integer>();
		for(int i = 0; i < n; i++) {
			if(mass0 >= asteroids[i]) {
				mass += asteroids[i];
			} else {
				list.add(asteroids[i]);
			}
		}
		if(0 == list.size()) {
			flag = 1;
		} else {
			int[] array = new int[list.size()];
			for(int i = 0; i < list.size();i++){
		        array[i] = (int) list.get(i);
		    }
			for(int i = 0 ; i < array.length ; i++) {
				for (int j = 0; j < array.length -  i - 1; j++) {
					if(array[j] > array[j + 1]) {
						int tmp;
						tmp = array[j + 1];
						array[j + 1] = array[j];
						array[j] = tmp;
					}
				}
			}			
			for(int k = 0; k < array.length; k++) {
				if(mass >= array[k]) {
					mass += array[k];
					flag = 1;
				} else {
					flag = 0;
					break;
				}
			}
		}		
		if(0 == flag) {
			return false;
		} else {
			return true;
		}
    }
	public static void main(String arg[]) {
		int mass = 263;
		int[] asteroids = {15};
		System.out.print(asteroidsDestroyed(mass, asteroids));
	}
}
