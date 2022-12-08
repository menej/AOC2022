using day02;

string[] lines = File.ReadAllLines("input.txt");


var partOne = new PartOne();
var partOneSolution = partOne.PartOneSolution(lines);
Console.WriteLine(partOneSolution);

var partTwo = new PartTwo();
var partTwoSolution = partTwo.PartTwoSolution(lines);
Console.WriteLine(partTwoSolution);