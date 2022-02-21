package leetcode00;

public class Schedule_wzx {
    public static void main(String[] args) {
        String[] a = {"01阮华明",
                "02郭芷菡",
                "03莫洛菲",
                "04李金凝",
                "05王子茜",
                "06林锦菊",
                "07黄嘉敏",
                "08蔡金旋",
                "09王紫辉",
                "10闫利霞",
                "11赵晓宇",
                "12李子萱",
                "13黎欣睿"};
        String[] b = new String[13];
        for(int i = 0; i < 13; i++) {
            b[i] = a[12 - i];
//            System.out.println(b[i]);
        }

        int j = 0;

        for(int week = 1; week < 25; week++) {
            int q, w, e;
            q = j % 13;
            j++;
            w = j % 13;
            j++;
            e = j % 13;
            j++;
            System.out.println("第" + week + "周： " + '\t' + "分工A:" + b[q] + '\t'
                    + "分工B:" + b[w] + '\t' + "分工C:" + b[e]);
        }
    }
}
