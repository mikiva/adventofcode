import java.util.Scanner;

public class Two
{
    public static void main(String[] args)
    {

        int goal = 19690720;
        Scanner sc = new Scanner(System.in);
        String rawInput = "";

        if (sc.hasNext())
        {
            rawInput = sc.next();
        }
        String[] input = rawInput.split(",");

        int[] intcodes = new int[input.length];
        int[] orig = new int[input.length];

        for (int i = 0; i < input.length; i++)
        {
            intcodes[i] = Integer.parseInt(input[i]);
            orig[i] = intcodes[i];
        }
        int noun = 12;
        int verb = 2;
        intcodes[1] = noun;
        intcodes[2] = verb;
        System.out.println("PART 1: " + run(intcodes));


        System.arraycopy(orig, 0, intcodes, 0, intcodes.length);

        outerLoop:
        for (int i = 0; i < 100; i++)
        {
            for (int j = 0; j < 100; j++)
            {

                intcodes[1] = i;
                intcodes[2] = j;
                try
                {
                    int result = run(intcodes);
                    if (result == goal)
                    {
                        noun = i;
                        verb = j;

                        break outerLoop;
                    }
                } catch (Exception e)
                {
                }

                System.arraycopy(orig, 0, intcodes, 0, intcodes.length);
            }

        }
        int result = (100 * noun) + verb;
        System.out.println("PART 2: " + result);


    }


    private static int run(int[] intcodes)
    {
        int chunkSize = 4;

        for (int i = 0; i < intcodes.length; i = i + chunkSize)
        {
            int opcode = intcodes[i];
            int first = intcodes[i + 1];
            int second = intcodes[i + 2];
            int resultLocation = intcodes[i + 3];

            int result = 0;
            switch (opcode)
            {
                case 1:
                    result = intcodes[first] + intcodes[second];
                    break;
                case 2:
                    result = intcodes[first] * intcodes[second];
                    break;
                case 99:
                    result = -1;
                    break;

            }

            if (result >= 0)
            {
                intcodes[resultLocation] = result;
            } else
            {
                break;
            }
        }

        return intcodes[0];


    }


}
