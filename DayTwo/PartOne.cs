namespace DayTwo;

public class PartOne
{
    private Dictionary<char, int> HandPoints { get; set; }

    public PartOne()
    {
        HandPoints = new Dictionary<char, int>
        {
            { 'X', 1 }, { 'Y', 2 }, { 'Z', 3 },
            { 'A', 1 }, { 'B', 2 }, { 'C', 3 }
        };
    }

    public int PartOneSolution(string[] lines)
    {
        int totalPoints = 0;

        foreach (string line in lines)
        {
            string[] splitLine = line.Split();
            char opponentsHand = char.Parse(splitLine[0]);
            char myHand = char.Parse(splitLine[1]);

            if (HandPoints[opponentsHand] == HandPoints[myHand])
            {
                totalPoints += HandPoints[myHand] + 3;
            }
            else if (opponentsHand == 'A' && myHand == 'Z' ||
                     opponentsHand == 'B' && myHand == 'X' ||
                     opponentsHand == 'C' && myHand == 'Y')
            {
                totalPoints += HandPoints[myHand];
            }
            else
            {
                totalPoints += HandPoints[myHand] + 6;
            }
        }

        return totalPoints;
    }
}