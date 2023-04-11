package leetcode00;

import java.io.UnsupportedEncodingException;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class javatest {
	
	/**
     * @param args
     */
    public static void main(String[] args) throws UnsupportedEncodingException, NoSuchAlgorithmException {
		// 不同的空字符串
//        String str1 = new String();
//        String str2 = null;
//        String str3 = "";
//        System.out.println(str1);
//        System.out.println(str2);
//        System.out.println(str3);
//        System.out.println(str1==str2);                //内存地址的比较，返回false
//        System.out.println(str1.equals(str2));         //值的比较，返回false
//        System.out.println(str2==str3);                //内存地址的比较，返回false
//        System.out.println(str3.equals(str2));         //值的比较，返回false
//        System.out.println(str1==str3);                //内存地址的比较，返回false
//        System.out.println(str1.equals(str3));         //值的比较，返回true
//        System.out.println("Hello Java!");
    	
    	Map<String, String> mymap = new HashMap<String, String>();
    	mymap.put("1", "草拟");
    	mymap.put("2", "生效");
    	mymap.put("3", "失效");
//    	mymap.remove("1");
//    	mymap.remove("生效");
//    	mymap.remove("3","失效");
    	Map<String, String> mymap01 = new HashMap<String, String>();
    	mymap01.put("1", "A");
    	mymap01.put("2", "B");
    	mymap01.put("3", "C");
    	
//    	List<Map> listOfMap = new ArrayList<Map>();
//    	listOfMap.add(mymap);
//    	listOfMap.add(mymap01);
//    	Map map = listOfMap.get(0);
//    	System.out.println(map);
//    	System.out.println(mymap.get("1"));

//		String roleno = "abc,def";
//		roleno = roleno.substring(0, roleno.length() - 1);
//		System.out.println(roleno);

		List<String> bslines = new ArrayList<String>();
//		System.out.println(String.valueOf("003"));

		// 测试GB2312每个字符占的字节数
		String[] gb = {"12", "佳", "cdf", " ", "一个空格"};
		for (int i = 0; i < gb.length; i++) {
			byte[] bb = gb[i].getBytes("gb2312");
			System.out.println(gb[i] + ":" + bb + ":" + bb.length);
		}
//		String pwd = "ｚｘｃ１２３z1";
//		String hexStr = "";
//		MessageDigest md5 = MessageDigest.getInstance("MD5");
//		// 转换为MD5码
//		byte[] digest = md5.digest(pwd.getBytes("utf-8"));
//		hexStr = ByteUtils.toHexString(digest);
//		System.out.println(resultString);
//		System.out.println("".length());
//		System.out.println("abc".length());
//		System.out.println("周".length());
    }
}


