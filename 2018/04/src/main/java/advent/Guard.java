package advent;

import java.util.Arrays;

public class Guard
{

	private int id;
	private int[] sleepTime;

	public Guard(int id)
	{
		this.id = id;
		this.sleepTime = new int[60];
		Arrays.fill(sleepTime, 0);
	}

	public void addSleep(int down, int up)
	{

		for (int i = down; i < up; i++)
		{
			this.sleepTime[i]++;
		}
	}

	public int[] getSleepTime()
	{
		return sleepTime;
	}

	public int getGuardID()
	{
		return id;
	}
	
	public int[] getMostFrequentMinute()
	{
		int[] minute = new int[2]; //[0] = minute on the hour, [1] = times spent sleeping on minute 
		for (int i = 0; i < sleepTime.length; i++)
		{
			if(sleepTime[i] > minute[1])
			{
				
				minute[0] = i;
				minute[1] = sleepTime[i]; 
			}
		}
			
		return minute;
	}
	
	
	@Override
	public String toString()
	{
		
		
		return "Guard #" + id;
		
		
	}
}
