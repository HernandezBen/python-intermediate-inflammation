"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def daily_mean(data):
    """Calculate the daily max of a 2D inflammation data array

    :param data: 2d array containing the inflamation data
    :returns: 1D array containing the mean of the data along the columns
    """
    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array

    :param data: 2d array containing the inflamation data
    :returns: 1D array containing the max of the data along the columns
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily max of a 2D inflammation data array

    :param data: 2d array containing the inflamation data
    :returns: 1D array containing the min of the data along the columns
    """
    return np.min(data, axis=0)


def daily_std(data):
    """Calculate the daily max of a 2D inflammation data array

    :param data: 2d array containing the inflamation data
    :returns: 1D array containing the std of the data along the columns
    """
    return np.std(data, axis=0)


def daily_above_threshold(patient_num, data, threshold):
    """Checks if each daily inflammation value for a given patient
    exceedes a given threshold.

    :param data: 2d array containing the inflamation data
    :param threshold: threshold value to check for each daily value
    :patient_num: patient row number
    :returns: An integer representing the number of days a patient's inflammation
    is over a given threshold
    """
    def count(a, b):
        if b:
            return a + 1
        else:
            return a

    above_threshold = map(lambda x: x > threshold, data[patient_num])
    return reduce(count, above_threshold, 0)
