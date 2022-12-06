namespace DaySix;

public class Solution
{
    public static int PartOneSolution(string lines)
    {
        
        int numProcessing = 0;

        while (numProcessing < lines.Length)
        {

            string subString = lines.Substring(numProcessing, 4);
            HashSet<char> subStringSet = new HashSet<char>(subString);
            if (subStringSet.Count == 4)
                break;
            numProcessing++;

        }
        // Add +1 for the last proccesed element, +3 for the last character that represents a marker
        return numProcessing + 4;
    }
    public static int PartTwoSolution(string lines)
    {
        
        int numProcessing = 0;

        while (numProcessing < lines.Length)
        {

            string subString = lines.Substring(numProcessing, 14);
            HashSet<char> subStringSet = new HashSet<char>(subString);
            if (subStringSet.Count == 14)
                break;
            numProcessing++;

        }
        // Add +1 for the last proccesed element, +13 for the last character that represents a marker
        return numProcessing + 14;
    }
}