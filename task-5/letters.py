word = input("Введите слово: ").lower()

vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
vowel_count = 0
consonant_count = 0

for letter in word:
    if letter in vowels.keys():
        vowels[letter] += 1
        vowel_count += 1
    else:
        consonant_count += 1

print(
    f"В слове {vowel_count} гласных и {consonant_count} согласных")

for letter, counter in vowels.items():
    if counter == 0:
        print(f"{letter}: False")
    else:
        print(f"{letter}: {counter}")
