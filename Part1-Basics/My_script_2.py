# encoding: utf-8

##################################################
# This script shows an example of variable assignment. It explores the different options for storing vales into
# variables
##################################################
#
##################################################
# Author: Diego Pajarito
# Copyright: Copyright 2020, IAAC
# Credits: [Institute for Advanced Architecture of Catalonia - IAAC, Advanced Architecture group]
# License:  Apache License Version 2.0
# Version: 1.0.0
# Maintainer: Diego Pajarito
# Email: diego.pajarito@iaac.net
# Status: development
##################################################

# We don't need any library so far

# Let's write our code

# Let's create two variables and assign them two values
Numero_1 = 50
Numero_2 = 10

# Let's assign the result of an operation to a third variable
resultado = Numero_1 + Numero_2

# Let's print out the result
print('The value assigned is:')
print(resultado)
print('....................\n')

# Let's assign a new value to this variable and print again
New_resultado = resultado + Numero_1
print('The value assigned now is:')
print(New_resultado)
print('....................\n')

# Let's assign a new value to this variable and print again
New_resultado_2 = New_resultado - Numero_2
print('The value assigned now is:')
print(New_resultado_2)
print('....................\n')
