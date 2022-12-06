using DaySix;

string lines = File.ReadAllText("input.txt").ReplaceLineEndings("");

int partOneSolution = Solution.PartOneSolution(lines);
Console.WriteLine(partOneSolution);

int partTwoSolution = Solution.PartTwoSolution(lines);
Console.WriteLine(partTwoSolution);