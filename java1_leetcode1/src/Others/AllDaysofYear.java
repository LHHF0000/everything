package Others;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

public class AllDaysofYear {
    public static void main(String[] args) throws ParseException {
        String dateStart="2018-01-01";
        String dateEnd="2018-12-31";
        SimpleDateFormat date=new SimpleDateFormat("yyyy-MM-dd");
        long startTime = date.parse(dateStart).getTime();//start
        long endTime = date.parse(dateEnd).getTime();//end
        long day=1000*60*60*24;
        for(long i=startTime;i<=endTime;i+=day) {
            System.out.println(date.format(new Date(i)));
        }
    }
}
