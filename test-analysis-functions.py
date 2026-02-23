def count_words(t):return len(t.split())
def count_vowels(t):return sum(1 for c in t if c.lower() in"aeiou")
def count_consonants(t):return sum(1 for c in t if c.isalpha() and c.lower() not in"aeiou")
def reverse_text(t):return t[::-1]
def is_palindrome(t):return t.lower()==t[::-1].lower()
def remove_vowels(t):return "".join(c for c in t if c.lower() not in"aeiou")
def word_frequency(t):
    d={}
    for w in t.lower().split():d[w]=d.get(w,0)+1
    return d
def longest_word(t):
    w=max(t.split(),key=len)
    return w,len(w)

def analyze_text(t):
    print("=== TEXT ANALYSIS ===")
    print("Words:",count_words(t))
    print("Vowels:",count_vowels(t))
    print("Consonants:",count_consonants(t))
    print("Reversed:",reverse_text(t))
    print("Palindrome:","Yes" if is_palindrome(t) else"No")
    print("Without vowels:",remove_vowels(t))
    w,l=longest_word(t)
    print("Longest word:",w,"("+str(l)+" letters)")
    print("Word Frequency:",word_frequency(t))

t=input("Enter text: ")
analyze_text(t)