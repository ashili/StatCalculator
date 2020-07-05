def cochranSampleSize(marginOfError, estimatedProportion):
    return ((1.96 ^ 2) * estimatedProportion * (1 - estimatedProportion)) / (marginOfError ^ 2)
