def sampleSize( confidenceInterval, width):
    marginOfError = width / 2
    pHat = .5
    qHat = 1 - pHat
    return (pHat * qHat) * ((1.96 / marginOfError) ^ 2)