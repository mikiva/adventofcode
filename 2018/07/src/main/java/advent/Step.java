package advent;

import java.util.ArrayList;
import java.util.List;

public class Step
{
	private List<Character> mustBeFinished;
	private char step;
	private boolean isFinished;

	public Step(char step)
	{
		isFinished = false;
		mustBeFinished = new ArrayList<>();
		this.step = step;

	}
	public char getStep()
	{
		return step;
	}
	public boolean isFinished()
	{
		return mustBeFinished.isEmpty();
	}
	public void setIsFinished(boolean isFinished)
	{
		this.isFinished = isFinished;
	}
	public List<Character> getMustBeFinished()
	{
		return mustBeFinished;
	}
	

}
