package Others;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class javaRegEx {
    public static void main(String[] args) {
        String s1 = "abv123456";//true
        String s2 = "12345678";//false
        String s3 = "Abcbbbbbb";//false
        String s4 = "Abc123";//true
        Pattern pattern0 = Pattern.compile("^[A-Za-z0-9]+$");
        Pattern pattern1 = Pattern.compile("[A-Za-z]+");
        Pattern pattern2 = Pattern.compile("[0-9]+");
        Matcher b1 = pattern0.matcher(s1);
        Matcher b2 = pattern0.matcher(s2);
        Matcher b3 = pattern0.matcher(s3);
        Matcher b4 = pattern0.matcher(s4);
//        System.out.print(b1.matches() + "\t");
//        System.out.print(b2.matches() + "\t");
//        System.out.print(b3.matches() + "\t");
//        System.out.print(b4.matches() + "\t");
//        Matcher m1 = pattern1.matcher(s1);  Matcher mm1 = pattern2.matcher(s1);
//        Matcher m2 = pattern1.matcher(s2);  Matcher mm2 = pattern2.matcher(s2);
//        Matcher m3 = pattern1.matcher(s3);  Matcher mm3 = pattern2.matcher(s3);
//        Matcher m4 = pattern1.matcher(s4);  Matcher mm4 = pattern2.matcher(s4);
//        System.out.print(m1.matches() + "\t");System.out.println(mm1.matches());
//        System.out.print(m2.matches() + "\t");System.out.println(mm2.matches());
//        System.out.print(m3.matches() + "\t");System.out.println(mm3.matches());
//        System.out.print(m4.matches() + "\t");System.out.println(mm4.matches());

//        System.out.println(s1.matches("[a-z]"));
        System.out.println(s1.matches(".*[a-zA-Z].*") && s1.matches(".*[0-9].*"));
        System.out.println(s2.matches(".*[a-zA-Z].*") && s2.matches(".*[0-9].*"));
        System.out.println(s3.matches(".*[a-zA-Z].*") && s3.matches(".*[0-9].*"));
        System.out.println(s4.matches(".*[a-zA-Z].*") && s4.matches(".*[0-9].*"));
    }
}
