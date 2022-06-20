# Regular Expressions
# Automata, Formal Languages
import re

# Returns the span of the word in the text if it was matched
print(re.search('patt', 'Searching pattern in text'))

# There is no 'None' in the text.
print(re.search('None', 'Searching pattern in text'))

# Scan through string looking for a match to the Pattern
match = re.search('patter', 'Searching pattern in text')
print(match)

# Matched word was 'patter'. -> .re.pattern recovers it
word = match.re.pattern
print(word)

# Matched word 'patter' was in some text. -> .string recovers it
text = match.string
print(text)

# 'patter' starts occurring at index 10 in the text
start = match.start()
print(start)

# 'patter ends occurring at index 16 in the text
end = match.end()
print(end)

# Compile a regular expression pattern, return a Pattern object
regex = re.compile('pat')
print(regex.search('Searching pat in text pat...').start())
# Not checks anymore after finding the first match
print(regex.search('Searching pat in text pat...').end())

# Manipulation to reach the final occurrence
print(re.search("(?s:.*)pat", "Searching pat in text pat..."))

# findall returns a list of matches
list_of_all_occurrings = regex.findall('Searching pat in text patt')
print(list_of_all_occurrings)

print(re.match("Match", "Match function test"))
print(re.match("function", "Match function test"))
