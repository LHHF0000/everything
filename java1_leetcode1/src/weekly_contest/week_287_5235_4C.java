package weekly_contest;

import java.util.*;

/**5235. 找出输掉零场或一场比赛的玩家
 * @date 2022.4.3
 * 122/127
 */
public class week_287_5235_4C {
    public static List<List<Integer>> findWinners(int[][] matches) {
        List<Integer> answer0 = new ArrayList<>();
        List<Integer> answer1 = new ArrayList<>();
        List<Integer> winners = new ArrayList<>();
        List<List<Integer>> answer = new ArrayList<>();
        List<Integer> losers = new ArrayList<>();
        for (int i = 0; i < matches.length; i++) {
            if (!winners.contains(matches[i][0]))
                winners.add(matches[i][0]);
            if (answer1.contains(matches[i][1]))
                    answer1.remove(answer1.indexOf(matches[i][1]));
            else if (!losers.contains(matches[i][1]))
                    answer1.add(matches[i][1]);
            if (!losers.contains(matches[i][1]))
                losers.add(matches[i][1]);
        }
//        for (int key : losers.keySet()) {
//            if (1 == losers.get(key))
//                answer1.add(key);
//        }
        for (int i = 0; i < winners.size(); i ++) {
            if (!losers.contains(winners.get(i)))
                answer0.add(winners.get(i));
        }
        answer.add(sort(answer0));
        answer.add(sort(answer1));
        return answer;
    }
    // List排序：转数组排完转List
    public static List<Integer> sort(List<Integer> list) {
        List<Integer> ll = new ArrayList<>();
        Integer[] arr = list.toArray(new Integer[0]);
        Arrays.sort(arr);
        for (int i = 0; i < arr.length; i++) {
            ll.add(arr[i]);
        }
        return ll;
    }
    public static void main(String arg[]) {
        int[][] matches = {{1,3},{2,3},{3,6},{5,6},{5,7},{4,5},{4,8},{4,9},{10,4},{10,9}};
        int[][] matches1 = {{2,3},{1,3},{5,4}, {6,4}};
        System.out.print(findWinners(matches1));
    }
}
