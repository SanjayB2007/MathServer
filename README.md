# Ex.04 Design a Website for Server Side Processing
## Date:12-12-2025

## AIM:
To create a web page to calculate vehicle mileage and fuel efficiency using server-side scripts.

## FORMULA:
M = D / F
<br> M --> Mileage (in km/l)
<br> D --> Distance Travelled (in km)
<br> F --> Fuel Consumed (in l)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:
```
math.html

<html>
<head>
    <title>Mileage Calculator</title>
    <style>
        body 
        {
            background: linear-gradient(rgb(255, 0, 85), black);
        }
        .id1 
        {
            text-align: center;
            color: black;
        }
        .box 
        {
            text-align: center;
            width: 50%;
            background-color: rgb(11, 20, 184);
            border: solid 4px black;
            padding: 20px;
            margin: 50px auto;
        }
        .result 
        {
            font-weight: bold;
        }
    </style>
</head>
<body>
    
    <div class="box">
        <h2><u>Mileage Calculator</u></h2>
        <h3>Sanjay babu M (25003400)</h3>

        <form method="post">
            {% csrf_token %}
            <label>Distance</label>
            <br>
            <input type="number" name="distance"> km
            <br>
            <br>
            <label>Liters</label>
            <br>
            <input type="number" name="liters"> L
            <br>
            <br>
            <button type="submit">Calculate</button>
            <br>
            <br>
            <label>Mileage</label>
            <br>
            <input class='result' type="number" name="Mileage" value={{miles}}>Km/L
        </form>
    </div>
</body>
</html>

views.py

from django.shortcuts import render
def miles(request):
    distance = int(request.POST.get('distance', 0))
    liter = int(request.POST.get('liters', 0))
    miles = distance / liter if request.method == 'POST' and liter != 0 else 0
    print("kilometers =", distance)
    print("liters =", liter)
    print("Mileage =", miles)
    return render(request, 'mathapp/math.html', {'distance': distance, 'liter': liter, 'miles': miles})

urls.py

from django.urls import path
from mathapp import views

urlpatterns = [
    path('', views.miles, name='miles'),
]
```

## OUTPUT - SERVER SIDE:
![alt text](<Screenshot (23).png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot (22).png>)

## RESULT:
The a web page to calculate vehicle mileage and fuel efficiency using server-side scripts is created successfully.
