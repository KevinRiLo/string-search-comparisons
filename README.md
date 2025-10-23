# string-search-comparisons
Project intended to implement string-searching algorithms from scratch and compare them

Implement (from scratch, not via libraries) and compare at least four classic string-search algorithms: naive (using a sliding window)*, KMP, Boyer-Moore, and Aho-Corasick. Explore how each algorithm organizes pattern matching and measure how they perform on texts of varying lengths and with different numbers of patterns. Your program should accept a text file and one or more search patterns, run each algorithm, and output evaluation metrics. For the multi-pattern case, Aho-Corasick should be implemented and compared against performing repeated single-pattern searches. 
* Naive search: Given a text T of length n and a pattern P of length m, align P at every possible start position.
