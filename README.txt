Hannah Brodheim
Created for the use of a school organization running elections using the Copeland Method.

The Copeland Method is a pairwise method of determining election results. It considers every participant ['A', 'B', 'C'] as though they were running against only one other participant, ie A vs B, A vs C, and B vs C. It then computes the number of individual contests each participant has won and pronounces them the overall winner.

The program is not the most efficient, a linear time O(n) algorithm is available, but since the quantities were small the less efficient solution was considered appropriate and easier to ensure accuracy.

The program reads in a file assumed to be titled "ballots.csv" where the first line of the spread sheet contains the candidates names, and each subsequent line is a ballot with every candidate ranked.  
for example
A   B	C
1   2	3
2   3	1
2   3	1

The winner and other informmation about the race is then output to "ElectionResults.txt"
