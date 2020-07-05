from Calculator.Calculator import Calculator
from Statistics.Mean import mean
from Statistics.SampleMean import sample_mean
from CsvReader.CsvReader import CsvReader
from Statistics.Mode import mode
from Statistics.Variance import variance
from Statistics.ZScore import zScore
from Statistics.Median import median
from Statistics.StdDev import stdDev
from Statistics.SimpleRandomSample import simpleRandomSample
from Statistics.ConfidenceInterval import confidenceInterval
from Statistics.MarginOfError import marginOfError
from Statistics.CochranSampleSize import cochranSampleSize
from Statistics.SampleSize import sampleSize
from Statistics.Randoms import randomRange, randomRangeSeed, randomList, randomListItem, randomListItemMultiple, randomListItemSeedMultiple


class Statistics(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self):
        self.result = mean(self.data)
        return self.result

    def sample_mean(self, sample_size):
        self.result = sample_mean(self.data, sample_size)
        return self.result

    def median(self):
        self.result = median(self.data)
        return self.result

    def mode(self):
        self.result = mode(self.data)
        return self.result

    def variance(self):
        self.result = variance(self.data)
        return self.result

    def z_score(self):
        self.result = zScore(self.data)
        return self.result

    def std_dev(self):
        self.result = stdDev(self.data)
        return self.result
