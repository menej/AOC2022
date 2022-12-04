namespace DayFour;

public static class PartTwo
{
    public static int PartTwoSolution(string[] lines)
    {
        int counterOverlaps = 0;

        foreach (var line in lines)
        {
            string[] sectionRanges = line.Split(",");
            string[] firstRange = sectionRanges[0].Split("-");
            string[] secondRange = sectionRanges[1].Split("-");

            var firstSections = new HashSet<int>();
            var secondSections = new HashSet<int>();

            int firstStart = int.Parse(firstRange[0]);
            int firstEnd = int.Parse(firstRange[1]);
            int secondStart = int.Parse(secondRange[0]);
            int secondEnd = int.Parse(secondRange[1]);

            for (int i = firstStart; i <= firstEnd; i++)
            {
                firstSections.Add(i);
            }

            for (int i = secondStart; i <= secondEnd; i++)
            {
                secondSections.Add(i);
            }

            var sectionsIntersection = new HashSet<int>(firstSections);
            sectionsIntersection.IntersectWith(secondSections);
            
            if (sectionsIntersection.Any())
                counterOverlaps++;
        }

        return counterOverlaps;
    }
}