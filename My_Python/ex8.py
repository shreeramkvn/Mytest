formatter = "%r,%r,%r,%r"

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
        "I had to try this program",
        "I will try this program.",
        "I did tried this program.",
        "No matter what. I will have this program typed."
)
