from django.shortcuts import render

def churn_rate(request):
    InitialCust=int(request.POST.get('initial_customer', '0'))
    PresentCust=int(request.POST.get('present_customer', '0'))

    churn=(InitialCust/PresentCust*100) if request.method=='POST' else 0

    print("Initial Customer=",InitialCust)
    print("Present customer=",PresentCust)
    print("Churn rate=",churn)

    return render(request,'myapp/math.html', {
        'InitialCust':InitialCust,
        'PresentCust':PresentCust,
        'churn': churn
    })