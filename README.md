# llm_out_dedupulication
function test for repetitive output dedupulication of LLM


# String Deduplication Techniques

This repository demonstrates three techniques for removing repeating patterns from strings: LZ78, KMP, and Suffix Arrays.

## Methods:

1. **LZ78**: A compression algorithm that adds consecutive duplicate substrings to a dictionary.
2. **KMP**: A string searching (or substring searching) algorithm which pre-processes the pattern to derive a failure function.
3. **Suffix Arrays**: An array of integers giving the starting positions of suffixes of a string in lexicographic order.

## Usage:

```python
import deduplication

text = "Your sample text here..."
dedup_text = deduplication.remove_with_suffix_array(text)
print(dedup_text)

## Example:

text = "圧縮データを短いテキストに変換する圧縮データを短いテキストに変換する圧縮データを短いテキストに変換する"

print(remove_longest_repeating_substring(text))

'''
output: 圧縮データを短いテキストに変換する
