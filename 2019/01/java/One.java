import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class One {


    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        List<Integer> modules = new ArrayList<>();

        int total = 0;

        try {

            while (sc.hasNext()) {
                int item = sc.nextInt();
                int totalFuel = 0;
                int fuel = getFuel(item);

                modules.add(fuel);
                total += fuel;
            }


            int total2 = 0;
            for (int fuel : modules) {

                while (fuel > 0)
                {
                    total2 += fuel;
                    fuel = getFuel(fuel);

                }
            }
            System.out.println("1. Total: " + total);
            System.out.println("2. Total: " + total2);


        } catch (Exception e) {
            System.out.println(e);
        }


    }


    public static int getFuel(int mass) {
        int fuel = 0;

        fuel = (int) Math.floor(mass / 3);
        fuel = fuel - 2;


        return fuel;

    }
}
