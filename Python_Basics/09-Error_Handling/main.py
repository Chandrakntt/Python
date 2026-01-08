try:
    result = 10/0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Error occured: {e}")
else:
    print("No errors!")
finally:
    print("This always runs")
    