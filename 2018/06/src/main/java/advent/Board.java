package advent;

import java.util.ArrayList;
import java.util.List;

public class Board
{

	private List<Coordinate> coordinates;
	private List<Point> points;
	private int width;
	private int height;

	public Board(List<Coordinate> coor)
	{
		points = new ArrayList<>();

		this.coordinates = coor;

		setBoardSize();
		setBoardPoints();

		// setShortestCoordinatesToPoints();

	}

	public int findBiggestPatch()
	{
		int val = 0;
		for (Coordinate c : coordinates)
		{
			val = c.getCounts() > val ? c.getCounts() : val;
		}
		return val;
	}

	public void setShortestCoordinatesToPoints()
	{
		for (Point p : points)
		{
			boolean countThis = false;
			int minDist = 999999;
			Coordinate cor = null;
			for (Coordinate c : coordinates)
			{
				int dist = getDistance(p, c);
				if (dist < minDist)
				{
					minDist = dist;
					countThis = true;
					cor = c;

				} else if (dist == minDist)
				{
					countThis = false;
				}
			}
			if (countThis)
			{
				cor.addCounts(1);
				if (p.getIsEdge())
				{
					cor.addCounts(-1000000);
				}
			}
		}

	}

	private int getDistance(Point p, Coordinate c)
	{
		int dist = 0;

		int px = p.getX();
		int py = p.getY();

		int cx = c.getX();
		int cy = c.getY();

		dist = Math.abs(cx - px) + Math.abs(cy - py);
		return dist;
	}

	private void setBoardSize()
	{
		int x = 0, y = 0;
		for (Coordinate c : coordinates)
		{
			x = c.getX() > x ? c.getX() : x;
			y = c.getY() > y ? c.getY() : y;
		}

		this.width = 1000;
		this.height = 1000;
	}

	private void setBoardPoints()
	{

		for (int px = 0; px < this.width; px++)
		{
			for (int py = 0; py < this.height; py++)
			{
				boolean isEdge = false;
				if (px == this.width - 1 || py == this.height - 1 || px == 0 || py == 0)
				{
					isEdge = true;
				}
				points.add(new Point(px, py, isEdge));
			}
		}
	}

	public int getAllClosePoints()
	{
		int closePoints = 0;
		for (Point p : points)
		{
			int totalDist = 0;
			for (Coordinate c : coordinates)
			{
				totalDist += getDistance(p, c);

			}

			if (totalDist < 10000)
				closePoints++;

		}

		return closePoints;
	}

}
