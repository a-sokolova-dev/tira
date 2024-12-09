# [9. Hakuongelmat](https://tira.mooc.fi/syksy-2024/osa9/#ahneet-algoritmit)

## [Summan valinta](getsum.py)

[CSES-3122](https://cses.fi/tira24s/task/3122)

As per course material: [Hakuongelmat - Ratkaisujen läpikäynti](https://tira.mooc.fi/syksy-2024/osa9/#ratkaisujen-l%C3%A4pik%C3%A4ynti)

## [Osajoukot](subsets.py)

[CSES-3120](https://cses.fi/tira24s/task/3120)

As per course material: [Hakuongelmat - Ratkaisujen läpikäynti](https://tira.mooc.fi/syksy-2024/osa9/#ratkaisujen-l%C3%A4pik%C3%A4ynti)

## [Sulkulausekkeet](brackets.py)

[CSES-3118](https://cses.fi/tira24s/task/3118)

See [Esimerkki: Sulkulausekkeet](https://tira.mooc.fi/syksy-2024/osa9/#esimerkki-sulkulausekkeet).

Don't forget to check if depth is not exceeding the given parameter k.

## [Anagrammit](anagrams.py)

[CSES-3121](https://cses.fi/tira24s/task/3121)

Nothing much to note here besides the fact that anagrams (if they can be meaningless) of a string are its permutations.

## [Oudot listat](oddlist.py)

[CSES-3119](https://cses.fi/tira24s/task/3119)

The solution is quite literal: generate all possible list, check each one for satisfying given conditions.
Also - funny task name :)

## [Kolikot nopeasti](fastcoin.py)

[CSES-3116](https://cses.fi/tira24s/task/3116)

As per course material:  [Hakuongelmat - Ahneet algoritmit](https://tira.mooc.fi/syksy-2024/osa9/#ahneet-algoritmit)

## [Ei vierekkäin](morediff.py)

[CSES-3115](https://cses.fi/tira24s/task/3115)

Can't generate and check all of the possible solutions, this will take too much time.

I used [backtracking](https://jeffe.cs.illinois.edu/teaching/algorithms/book/02-backtracking.pdf) because I like the strategy and it seems the most intuitive to me, but it can probably also be done with bruteforce by noting short sequences that satisfy the problem and then using them as subsequence templates to build the 1...n sequence.

More backtracking practice can be found on [Leetcode](https://leetcode.com/problem-list/backtracking/).

## [Lisää kolikoita](morecoin.py)

[CSES-3117](https://cses.fi/tira24s/task/3117)

Brute force! Greedy solution almost works, but there are some cases that need to be handled separately.
Can be done in different ways code-wise, but I prefer grabbing all the fives first and then look at what's left and if it makes sense to exchange some of the fives + the leftover change back to smaller other coins.