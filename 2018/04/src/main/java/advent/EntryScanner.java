package advent;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class EntryScanner
{

	public EntryScanner()
	{

	}

	public void scanEntry(String entry)
	{

		System.out.println(entry);
		String regex = ".*:(\\d\\d)\\].*";

		Pattern p = Pattern.compile(regex);

		Matcher m = p.matcher(entry);

		System.out.println(m.matches());

	}

	public int getGuardID(String entry)
	{

		int id = -1;

		String regex = ".*#(?<id>[0-9]+).*";

		Pattern p = Pattern.compile(regex);

		Matcher m = p.matcher(entry);
		m.find();

		try
		{
			id = Integer.parseInt(m.group("id"));
		} catch (Exception e)
		{
			System.out.println(entry);
		}

		return id;
	}

	public int sleepOrWakeUp(String line)
	{
		int time = -1;
		String regex = ".*:(?<time>[0-9]+)\\].*";

		Pattern p = Pattern.compile(regex);

		Matcher m = p.matcher(line);
		m.find();
		try
		{

			time = Integer.parseInt(m.group("time"));
		} catch (Exception e)
		{
			System.out.println("SLEEP OR WAKE UP");
			System.out.println(line);
		}

		return time;
	}

}
