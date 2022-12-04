using DayFour;

string[] lines = File.ReadAllLines("input.txt");

int partOneSolution = PartOne.PartOneSolution(lines);
Console.WriteLine(partOneSolution);

int partTwoSolution = PartTwo.PartTwoSolution(lines);
Console.WriteLine(partTwoSolution);
