class Point {
    int x;
    int y;

    public Point() {

    }

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }


    public String toString()
    {
        return "x: " + x + " | y: " + y;
    }


    public boolean isOrigo()
    {

        return this.x == 0 && this.y == 0;

    }
}