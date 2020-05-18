def testName():
    print("Testing __name__")


print("top level statement")

if __name__ == "__main__":
    testName()  # used to execute the function only if executed separately
    print("oop.py is being run directly")
else:
    print("oop.py is being used by some other file")
