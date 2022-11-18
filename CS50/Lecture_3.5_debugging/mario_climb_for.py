def main(n):
    for i in range(n):
        print("#" * (i + 1))


# i believe this checks if the script is being ran on itself or if if it being called by another module
# if this script is ran on itself, then by default, name == main.
# if this script was imported by another script, it will not be the main script, instead: name = mario_for_loop.py
# in summary, the below if statement only triggers if you run "python3 mario_for_loop.py"
if __name__ == "__main__":
    main(4)
