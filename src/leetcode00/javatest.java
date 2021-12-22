package leetcode00;

import java.util.HashMap;
import java.util.Map;

public class javatest {
	
	/**
     * @param args
     */
    public static void main(String[] args) {        
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
    	System.out.println(mymap.get("1"));
    }
}


