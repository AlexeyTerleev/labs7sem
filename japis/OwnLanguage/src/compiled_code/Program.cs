class Program
{
	static dynamic Process(dynamic el1, dynamic el2)
	{
		HashSet<string> newSet = new HashSet<string>();
		newSet.Add(el1);
		newSet.Add(el2);
		return newSet;
	}
	static void Main()
	{
		string el1 = "banana";
		string el2 = "apple";
		HashSet<string> mySet = Process(el1,el2);
		foreach (var element in mySet)
		{
			Console.WriteLine(element);
		}
	}
}