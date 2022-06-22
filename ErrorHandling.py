while True:
    try:
        age = int(input('What is your age? '))
        10/age
    except ValueError:
        print('Please enter a number')
        continue
    except ZeroDivisionError:
        print('Enter age greater than zero')
        break
    else:
        print('thank you')
        break
    finally:
        print('Hey I will run no matter what')