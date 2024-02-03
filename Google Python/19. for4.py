# Video 34

def to_celcius(x):
    return (x-32)*5/9

for x in range(0, 101, 10):
    print("Celcius: "+str(x))
    print("Fanhereit: "+str(to_celcius(x)))