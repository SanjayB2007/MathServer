from django.shortcuts import render
def miles(request):
    distance = int(request.POST.get('distance', 0))
    liter = int(request.POST.get('liters', 0))
    miles = distance / liter if request.method == 'POST' and liter != 0 else 0
    print("kilometers =", distance)
    print("liters =", liter)
    print("Mileage =", miles)
    return render(request, 'mathapp/math.html', {'distance': distance, 'liter': liter, 'miles': miles})