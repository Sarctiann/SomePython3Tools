# Command Line Tools
### [ ◀️ Go Back](https://github.com/Sarctiann/SomePython3Tools)
***

## SorteredDict

This module provide the **sort_dict** function for sort a Dictionary

A Sample
```python
sarctiann@neon-sarc > bpython -i SorteredDict.py 
Make sure to run in interactive mode (python3 -i SorteredDict.py)
bpython version 0.21 on top of Python 3.10.0 /usr/local/bin/python3.10

>>> print(a)
{4: ['e', 30], 5: ['c', 20], 6: ['a', 10], 1: ['b', 60], 2: ['d', 50], 3: ['f', 40]}

>>> sort_dict(a,
┌───────────────────────────────────────────────────────────────────────────────────────────────────┐
│ sort_dict: (dic, sortIDX=int=None, FilterIDX=int=None, GreaterThan=None, SmallerThan=None)        │
│ Recive:                                                                                           │
│ A DICTIONARY to sort [,                                                                           │
│     sortIDX =>      sort index criteria.  None => for key,                                        │
│     FilterIDX =>    filter index criteria. None => for key,                                       │
│     GreaterThan =>  (for filter) greater or equal,                                                │
│     SmallerThan =>  (for filter) smaller or equal                                                 │
│ ]                                                                                                 │
│                                                                                                   │
│ Return: the sort dictionary by passed criteria.                                                   │
└───────────────────────────────────────────────────────────────────────────────────────────────────┘

...

>>> sorted_by_key = sort_dict(a)
>>> sorted_by_key
{1: ['b', 60], 2: ['d', 50], 3: ['f', 40], 4: ['e', 30], 5: ['c', 20], 6: ['a', 10]}

>>> sorted_by_second_value = sort_dict(a, 1)
>>> sorted_by_second_value
{6: ['a', 10], 5: ['c', 20], 4: ['e', 30], 3: ['f', 40], 2: ['d', 50], 1: ['b', 60]}

>>> sorted_by_first_value_and_filtered_by_second = sort_dict(a, 0, 1, 20, 40)
>>> sorted_by_first_value_and_filtered_by_second
{5: ['c', 20], 4: ['e', 30], 3: ['f', 40]}
```

***

## compareCars

This is a program to compare second hand cars by mileage, model and price.

A Sample
> I add some quotes after for highlighting the text
```python
"Let's consider the following comparison parameters:"
Mileage -       Best: 0        Worst: 100000
Model   -       Best: 2021     Worst: 2016
Price   -       Best: 0        Worst: 40000

And they have the following weight:
Miles: 50.0%, Model: 30.0%, Price 20.0%

Do you want to redefine the parameters? (y/any): y


How much would be the best mileage? 0
Which would be the best (year)? 100
How much would be the best price? 0
How much would be the worst mileage? 100
Which would be the worst (year)? 0
How much would be the worst price? 100

Define they weight:

Miles: 5
Model: 3
Price: 2

"So, Let's consider the following comparison parameters:"
Mileage -       Best: 0        Worst: 100
Model   -       Best: 100      Worst: 0
Price   -       Best: 0        tWorst: 100

And they have the following weight:
Miles: 50.0%, Model: 30.0%, Price 20.0%


Enter Car Name: Foo  
Enter Foo Mileage: 10
Enter Foo Model: 50
Enter Foo Price: 80
Add another Car? (y/any) y

Enter Car Name: Baz 
Enter Baz Mileage 50
Enter Baz Model: 80
Enter Baz Price: 60
Add another Car? (y/any) n

Foo scores:
        Kms => 90.0
        Model => 50.0
        Price => 20.0
Baz scores:
        Kms => 50.0
        Model => 80.0
        Price => 40.0

Foo score: 64.0
Baz score: 57.0


Press Enter to exit.
```

***

## Percentages

It seems simple, but sometimes we need to do unusual calculations. That is why I write this module that contains a instantiable class: "Percentron" that has simple operations and others not so simple to operate with values (val) and percentages (per) adding and subtracting of increases and discounts.

```python
python3 -i clTools/Percentages.py

        *** Percentage operations ***:

        1) Start this module in interactive mode (python3 -i Percentages.py)
        2) Instantiate Percentron ( Eg. p = Percentron(...) ).
        3) More Info => Percentron.help() | help(Percentron)

                                                                Sebastián Atlántico

>>> Percentron.help()

values (val) and percentages (per) operations

.val_increase(p, *,val):
         Increase values a "p" percent
                        Eg. 100(val) + 20%(p) = 120

.val_discount(p, *,val):
         Discounts "p" percent to values
                        Eg. 100(val) - 20%(p) = 80

.val_from_increase(p, *,val):
         Obtains the value resulting from increase "p" percent to values
                        Eg. 100(val) from increase 20%(v) = 83.33...

.val_from_discount(p, *,val):
         Obtains the value resulting from discount "p" percent to values
                        Eg. 100(val) from discount 20%(p) = 125

.per_addition(p, *,val):
         (assumes values are percentages)
                        Add the percentage "p" to percentages (values)
                        Eg. 100%(per) + 10%(p) = 120%

.per_subtraction(p, *,val):
         (assumes values are percentages)
                        Subtract the percentage "p" to percentages (values)
                        Eg. 100%(per) - 10%(p) = 80%

.per_from_addition(p, *,val):
         (assumes values are percentages)
                        Obtains the percentage resulting from addition of "p" percent 
                        to percentages (values)
                        Eg. 100%(per) from addition 10%(p) = 81.83...%

.per_from_subtraction(p, *,val):
         (assumes values are percentages)
                        Obtains the percentage resulting from subtraction of "p" percent 
                        to percentages (values)
                        Eg. 100%(per) from subtraction 10%(p) = 122.22...%

.per_from_val_increase(p, *,val):
         Obtains the percentage from "v" as resulting increase to values
                        Eg. 100(val) increased to 110(v) = 10%

.per_from_val_discount(p, *,val):
         Obtains the percentage from "v" as resulting discount to values
                        Eg. 100(val) discounted to 90(v) = 10%

Remember, val and per are a keyword arguments
```

### [ ◀️ Go Back](https://github.com/Sarctiann/SomePython3Tools)
