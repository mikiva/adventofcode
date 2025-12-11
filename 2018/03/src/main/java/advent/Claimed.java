package advent;

import java.util.ArrayList;
import java.util.List;

public class Claimed {

	List<Integer> list;
	int claimCount;
	
	public Claimed()
	{
		list = new ArrayList<>();
		claimCount = 0;
	}
	
	public void addClaim(int id)
	{
		list.add(id);
		claimCount++;
	}
	public List<Integer> getClaimed()
	{
		return list;
	}
	
	public int getClaimCount()
	{
		return claimCount;
	}
	
	
	
}
