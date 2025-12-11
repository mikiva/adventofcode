package advent;

import java.util.ArrayList;
import java.util.List;

public class Coordinate
{

	public int x, y;
	public String id;
	List<Point> points;
	private int counts = 0;

	public Coordinate(Integer[] coor, String id)
	{
		points = new ArrayList<>();
		this.id = id;
		this.x = coor[0];
		this.y = coor[1];
	}
	
	public void addCounts(int count)
	{
		counts += count;
	}
	public int getCounts()
	{
		return counts;
	}
	public int getX()
	{
		return x;
	}
	public int getY()
	{
		return y;
	}
}
