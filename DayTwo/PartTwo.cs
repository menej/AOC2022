namespace DayTwo;

public class PartTwo
{
    private Dictionary<char, int> handPoints { get; set; }

    public PartTwo()
    {
        handPoints = new Dictionary<char, int>
        {
            { 'A', 1 }, { 'B', 2 }, { 'C', 3 }
        };
    }

    public int PartTwoSolution(string[] lines)
    {
        int totalPoints = 0;

        foreach (string line in lines)
        {
            string[] splitLine = line.Split();
            char opponentsHand = char.Parse(splitLine[0]);
            char outcome = char.Parse(splitLine[1]);

            char myHand;

            if (outcome == 'X')
            {
                myHand = opponentsHand switch
                {
                    'A' => 'C',
                    'B' => 'A',
                    'C' => 'B',
                    _ => throw new InvalidDataException()
                };
                totalPoints += handPoints[myHand];
            }
            else if (outcome == 'Y')
            {
                totalPoints += handPoints[opponentsHand] + 3;
            }
            else if (outcome == 'Z')
            {
                myHand = opponentsHand switch
                {
                    'A' => 'B',
                    'B' => 'C',
                    'C' => 'A',
                    _ => throw new InvalidDataException()
                };
                totalPoints += handPoints[myHand] + 6;
            }
            else
            {
                throw new InvalidDataException();
            }
        }

        return totalPoints;
    }
}