def vowels(text):
    count = 0
    for ch in text:
        if ch in "aeiou":
            count += 1
    return count


def consonants(text):
    count = 0
    for ch in text:
        if ch.isalpha() and ch not in"aeiou":
            count += 1
            return count
        

        def ratio(vowel_count,consonant_count):
            if consonant_count == 0:
                print("Invalid number(no consonants)")
            else:
                r = vowel_count/ consonant_count
                print("ratio(vowels:consonants)=",r)

                text = input("enter any sentance:").lower()

                v = vowels(text)
                c = consonants(text)

                print("number of vowels:",v)
                print("number of consonants:", c)

                ratio(v, c)

            