import Lab_2.bmi as bmi

#the AAA pattern in Testing

#the 3 phase

#1. Arrange
#Set up the test condition
#Prpare the input data and prequisites

#2. Act
#Call the fn/method u want to test
#This is usally a single line

#3. Assert
#Verify result
#Check the actual output matches the expected output
#USe assertions to confirm correctness

def test_bmi_normal_weight():
    #Arrange (Initiliase data)
    height = 1.73
    weight = 57
    #Act (test with fn)
    result = bmi.calculate_bmi(height,weight)
    #Assert (check if if value output equal to expected output)
    assert result == 0

def test_bmi_over_weight():
    #Arrange (Initiliase data)
    height = 1.73
    weight = 80
    #Act (test with fn)
    result = bmi.calculate_bmi(height,weight)
    #Assert (check if if value output equal to expected output)
    assert result == 1

def test_bmi_under_weight():
    #Arrange (Initiliase data)
    height = 1.73
    weight =  30
    #Act (test with fn)
    result = bmi.calculate_bmi(height,weight)
    #Assert (check if if value output equal to expected output)
    assert result == -1