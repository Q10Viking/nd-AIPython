while True:
    try:
        x = int(input("Enter a number: "))
        break
    except ValueError:
        print("That's not a valid number!")
    except KeyboardInterrupt:
        # ctrl + c
        print("No input taken.Over!")
        break
    finally:
        print('\nAttempted Input\n')

print("Done!")

'''
Enter a number: we
That's not a valid number!

Attempted Input

Enter a number: 2

Attempted Input

Done!
'''