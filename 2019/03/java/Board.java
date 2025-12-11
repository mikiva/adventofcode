import java.util.ArrayList;
import java.util.List;

/**
 * Board
 */
public class Board {

    Point currPoint;
    List<Segment> segmentsLine1;
    List<Segment> segmentsLine2;
    int startX, startY;
    List<Point> intersections;

    public Board(String[] line1, String[] line2) {
        currPoint = new Point(0, 0);
        segmentsLine1 = draw(line1);
        segmentsLine2 = draw(line2);
        intersections = new ArrayList<>();
    }

    public List<Segment> draw(String[] line) {

        currPoint = new Point(0, 0);

        List<Segment> segments = new ArrayList<>();
        for (String s : line) {
            char dir = s.charAt(0);
            int distance = Integer.valueOf(s.substring(1));
            Point newP = walk(dir, distance);
            Segment seg = new Segment(currPoint, newP);
            segments.add(seg);
            currPoint = newP;
        }

        return segments;
    }

    public Point walk(char dir, int distance) {
        Point newPoint = new Point(currPoint.x, currPoint.y);

        switch (dir) {
        case 'U':
            newPoint.x += distance;
            break;
        case 'D':
            newPoint.x -= distance;
            break;
        case 'L':
            newPoint.y -= distance;
            break;
        case 'R':
            newPoint.y += distance;
            break;
        }

        return newPoint;

    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();

        sb.append(segmentsLine1.size() + "\n");
        sb.append(segmentsLine2.size() + "");
        return sb.toString();

    }

    public List<Point> getIntersections() {
        List<Point> inter = new ArrayList<>();

        
        Segment s1;
        Segment s2;
        for (int i = 0; i < segmentsLine1.size(); i++) {
            s1 = segmentsLine1.get(i);
            for (int j = 0; j < segmentsLine2.size(); j++) {
                s2 = segmentsLine2.get(j);

                if(intersect(s1,s2))
                {
                    inter.add(getIntersection(s1, s2));

                    
                }

            }
        }

        return inter;

    }

    public boolean intersect(Segment s1, Segment s2) {

        if((s1.xmin >= s2.xmin && s1.xmin <= s2.xmax) &&
        (s2.ymin >= s1.ymin && s2.ymin <= s1.ymax))
        {
            return true;
        }
        else if((s2.xmin >= s1.xmin && s2.xmin <= s1.xmax) &&
        (s1.ymin >= s2.ymin && s1.ymin <= s2.ymax ))
        {
            return true;
        }
        else{
            return false;
        }

    }
    public Point getIntersection(Segment s1, Segment s2)
    {
        if((s1.xmin >= s2.xmin && s1.xmin <= s2.xmax) &&
        (s2.ymin >= s1.ymin && s2.ymin <= s1.ymax))
        {
            return new Point(s1.xmin, s2.ymin);
        }
        else if((s2.xmin >= s1.xmin && s2.xmin <= s1.xmax) &&
        (s1.ymin >= s2.ymin && s1.ymin <= s2.ymax ))
        {
            return new Point(s2.xmin, s1.ymin);
        }
        else{
            return new Point(0,0);
        }
    }

    public int getDistance(Point p1, Point p2)
    {

        return Math.abs((p1.x - p2.x)) + Math.abs((p1.y - p2.y));


    }



    class Segment {
        Point p1;
        Point p2;
        int xmax;
        int xmin;
        int ymax;
        int ymin;

        public Segment(Point p1, Point p2) {
            this.p1 = p1;
            this.p2 = p2;

            xmax = Math.max(p1.x, p2.x);
            xmin = Math.min(p1.x, p2.x);
            ymax = Math.max(p1.y, p2.y);
            ymin = Math.min(p1.y, p2.y);

        }
        public String toString()
        {
            return "p1: " + p1.toString() + " p2: " + p2.toString();
        } 
    }
}