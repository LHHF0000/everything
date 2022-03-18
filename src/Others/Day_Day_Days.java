package Others;

/**计算任意两个日期之间差的天数
 * @date 2022.3.18
 */
public class Day_Day_Days {
    public static int numberOfDays(String day1, String day2) {
        int[] sd = stringToIntArray(day1);
        int[] ed = stringToIntArray(day2);
        int ans = 0;
        if (ed[0] > sd[0]) {
            // 先计算ed当年天数
            ans += ed[2];
            for (int m = ed[1]; m > 1; m --) {
                ans += daysOfMon(ed[0], m - 1);
            }
            // 再计算间隔的整年
            for (int y = ed[0]; y > sd[0]; y--) {
                if (y - 1 > sd[0]) {
                    ans += isLeapYear(y)? 366 : 365;
                } else {    // 最后计算sd当年天数
                    for (int m = 12; m >= sd[1]; m--) {
                        if (m > sd[1]) {
                            ans += daysOfMon(y, m);
                        } else {
                            ans += daysOfMon(y, m) - sd[2];
                        }
                    }
                }
            }
        } else if (ed[0] == sd[0]) {    //同年
            if (ed[1] > sd[1]) {
                ans += ed[2];
                for (int i = ed[1]; i > sd[1]; i--) {
                    if (i - 1 > sd[1]) {
                        ans += daysOfMon(ed[0], i - 1);
                    } else {
                        ans += daysOfMon(ed[0], i - 1) - sd[2];
                    }
                }
            } else if (ed[1] == ed[1]) {    //同月
                ans += ed[2] - sd[2];
            } else if (ed[1] < ed[1]) {
                ans = 0;
            }
        } else {
            ans = 0;
        }
        return ans;
    }

    public static void main(String arg[]) {
        System.out.print(numberOfDays("1998-1-2", "2022-3-18"));
    }

    // 返回当月天数
    public static int daysOfMon(int year, int month) {
        int[] mon = {31,28,31,30,31,30,31,31,30,31,30,31};
        if(isLeapYear(year))
            mon[1] = 29;
        return mon[month - 1];
    }

    // 判断是否闰年
    public static boolean isLeapYear(int year) {
        if((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)
            return true;
        else
            return false;
    }

    // 字符串转整形数组
    public static int[] stringToIntArray(String str) {
        String[] st = str.split("-");
        int[] intArray = new int[st.length];
        for (int i = 0; i < st.length; i++) {
            intArray[i] = Integer.valueOf(st[i]);
        }
        return intArray;
    }
}
