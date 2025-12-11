package advent;

public class Point
{
	
	private int x,y;
	private boolean isEdge;
	
	public Point(int x, int y, boolean isEdge)
	{
		this.x = x;
		this.y = y;
		this.isEdge = isEdge;
		
	}
	public boolean getIsEdge()
	{
		return isEdge;
	}

	public int getX()
	{
		return x;
	}

	public void setX(int x)
	{
		this.x = x;
	}

	public int getY()
	{
		return y;
	}

	public void setY(int y)
	{
		this.y = y;
	}
}
