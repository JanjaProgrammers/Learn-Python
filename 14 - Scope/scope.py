x = 1
def foo():
    x = 5
    def inner():
        nonlocal x
        x=2
        print(f"Inner sees x as {x}")
    inner()
    print(f"Local sees x as {x}")

foo()
print(f"Global sees x as {x}")
