def oneCal():
    reps = float(request.GET['R'])
    weight = float(request.GET['W'])
    rxw = weight * (1 + (reps/30))
    return rxw