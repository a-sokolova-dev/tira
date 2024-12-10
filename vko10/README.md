# [10. Dynaaminen ohjelmointi](https://tira.mooc.fi/syksy-2024/osa10/)

## [Eniten kolikkoja](maxcoin.py)

[CSES-3309](https://cses.fi/tira24s/task/3309)

The only thing that needs to be used here is common sense, really, so nothing to comment.

## [Alijonon muodostus](createseq.py)

[CSES-3126](https://cses.fi/tira24s/task/3126)

Basically the [Esimerkki: Alijonot](https://tira.mooc.fi/syksy-2024/osa10/#esimerkki-alijonot) example with slightly more advanced information to store.
I stored the substrings lengths first and then found the longest one by iterating over them separately, but it can be done on the fly (I had a different solution in mind first, but it was not very DP-like, so I decided to rework it and it ended up like this). This won't really affect the time complexity, but finding maximum on the go would be nicer.

## [Kaikki alijonot](countseq.py)

[CSES-3127](https://cses.fi/tira24s/task/3127)

See [Ratkaisujen laskeminen](https://tira.mooc.fi/syksy-2024/osa10/#ratkaisujen-laskeminen)

## [Pienimmät määrät](minways.py)

[CSES-3310](https://cses.fi/tira24s/task/3310/)

We need to store both the minimum possible number of coins to get a certain sum and the number of ways to picke the coins amounting to this sum. This is very similar to Leetcode problems [322. Coin Change](https://leetcode.com/problems/coin-change/description/) and [518. Coin Change II](https://leetcode.com/problems/coin-change-ii/description/). My initial solution was one of my previously accepted Leetcode submissions, and then I worked up from it to make the logic and the DP more explicit. Could be simplified further by using a better data structure than two separate arrays, but it looks good enough to me to call it a day.

## [Bitti poisto](countseq.py)

[CSES-3313](https://cses.fi/tira24s/task/3313)

Used recursive solution with 1-D memoization (like in the last [Esimerkki: Sulkulausekkeet](https://tira.mooc.fi/syksy-2024/osa10/#esimerkki-sulkulausekkeet) example).

## [Kurssi](course.py)

[CSES-3137](https://cses.fi/tira24s/task/3137)

The detailed example explanation for `x = 40` is really helpful for understanding how counting the possible permutations works. Then it's relatively easy to find the recursive formula for solving tasks week by week. The recursive solution works (and I left it at that), but we could also store the "solved tasks - weeks" combination for optimization like in Alijonon muodostus.
