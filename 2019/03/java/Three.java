import java.util.List;
import java.util.Scanner;

/**
 * Three
 */
public class Three {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        
        
        String line1raw = sc.nextLine();
        String line2raw = sc.nextLine();
        
        String[] line1 = line1raw.split(",");
        String[] line2 = line2raw.split(",");
        Board board = new Board(line1, line2);
        List<Point> intersects = board.getIntersections();
        int miniDist = Integer.MAX_VALUE;
        Point ORIGO = new Point(0,0);
        for(Point p : intersects)
        {
            System.out.println(p.x + " " + p.y + "\n");
            if(!p.isOrigo())
            {
                int dist = board.getDistance(p,ORIGO);

                if(dist < miniDist)
                {
                    miniDist = dist;
                }
            }

        }
        System.out.println(board.getIntersections().size());


        //System.out.println(board.toString());
        System.out.println(miniDist);
        sc.close();
    }

}