package advent;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Iterator;
import java.util.LinkedHashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;
import java.util.TreeSet;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Runner
{

	private List<String> steps;
	private List<Character> stepsToDo;
	private char[] alphabet;
	private final int MIN_WORK_TIME = 60;

	public Runner(List<String> steps)
	{
		alphabet = "-ABCDEFGHIJKLMNOPQRSTUVWXYZ".toCharArray();
		this.steps = steps;
		Collections.sort(steps);
		//System.out.println(String.format("Part 1: %s", part1()));

		System.out.println(String.format("Part 2: %s", part2()));

	}

	public String part1()
	{
		String part1 = part1Steps();
		return part1;
	}

	public String part2()
	{
		Map<Character, List<Character>> map = setUpSteps();

Set<Character> finished = new LinkedHashSet<>();
		Set<Character> sortedSteps = new TreeSet<>();
		for(String str : steps)
		{
			sortedSteps.add(getStep(str)[0]);
			sortedSteps.add(getStep(str)[1]);
		}







		return "String";
	}
	
	public String part1Steps()
	{

		Map<Character, List<Character>> map = setUpSteps();

		Set<Character> sortedSteps = new TreeSet<>();
		Set<Character> finished = new LinkedHashSet<>();

		for (String str : steps)
		{
			sortedSteps.add(getStep(str)[0]);
			sortedSteps.add(getStep(str)[1]);
		}

		int count = 0;
		boolean running = true;
		while (running)
		{
			Iterator<Character> it = sortedSteps.iterator();
			while (it.hasNext())
			{
				char step = (char) it.next();

				if (stepIsAvailable(step, map, finished))
				{
					finished.add(step);
					break;
				}
			}
			running = !isFinished(sortedSteps, finished);
		}

		StringBuilder str = new StringBuilder();
		for (char c : finished)
			str.append(c);
		return str.toString();
	}

	public boolean stepIsAvailable(char step, Map<Character, List<Character>> map, Set<Character> fin)
	{

		if (!map.containsKey(step) && !fin.contains(step))
			return true;

		for (Map.Entry<Character, List<Character>> entry : map.entrySet())
		{

			if (step != (char) entry.getKey())
				continue;

			Iterator<Character> iter = entry.getValue().iterator();
			while (iter.hasNext())
			{
				Character ste = iter.next();
				if (!fin.contains(ste))
				{
					continue;
				}
				if (fin.contains(ste))
				{
					iter.remove();
				}

				if (entry.getValue().isEmpty() && !fin.contains(step))
				{
					// System.out.println(entry.getValue() + " "+ entry.getKey());
					return true;

				}

			}
		}

		return false;
	}

	public boolean isFinished(Set<Character> list, Set<Character> finished)
	{
		boolean is = true;
		Iterator<Character> iter = list.iterator();

		while (iter.hasNext())
		{
			Character c = iter.next();
			if (!finished.contains(c))
			{
				is = false;
			}
		}
		return is;
	}

	public Map<Character, List<Character>> setUpSteps()
	{
		Map<Character, List<Character>> stepM = new TreeMap<>();
		for (String s : steps)
		{
			char[] step = getStep(s);

			if (stepM.containsKey(step[1]))
			{
				stepM.get(step[1]).add(step[0]);
			}
			else
			{
				stepM.put(step[1], new ArrayList<Character>(Arrays.asList(step[0])));
			}
		}

		for (Map.Entry<Character, List<Character>> m : stepM.entrySet())
		{
			Collections.sort(m.getValue());
		}

		return stepM;
	}

	public char[] getStep(String in)
	{

		String regex = "^Step (?<must>\\S).*step (?<begin>\\S).*";
		Pattern p = Pattern.compile(regex);
		Matcher m = p.matcher(in);
		char[] c = new char[2];

		if (m.find())
		{
			c[0] = m.group("must").charAt(0);
			c[1] = m.group("begin").charAt(0);
		}

		return c;
	}

}
