from django.shortcuts import render
import json

diagnosis = [
    {'id': 'P', 'name' : 'Type Presymptomatic', 'value':7},
    {'id': '0', 'name' : 'Type 0/1a', 'value': 4},
    {'id': '1', 'name' : 'Type 1', 'value' : 190},
    {'id': '2', 'name' : 'Type 2', 'value' : 209},
    {'id': '3', 'name' : 'Type 3', 'value': 171},
    {'id': '4', 'name' : 'Type 4', 'value': 2},

    {'id': '3_a', 'name' : 'Type 3a', 'parent': '3', 'value': 121},
    {'id': '3_b', 'name' : 'Type 3b', 'parent': '3', 'value': 47},
    {'id': '3_u', 'name' : 'Unknown', 'parent': '3', 'value': 3},
    ]



genders = [
    {'name' : 'Male', 'y' : 325},
    {'name' : 'Female', 'y' : 276},
    ]


races = [
    {'name' : 'White', 'y' : 525},
    {'name' : 'Asian', 'y' : 22},
    {'name' : 'Black or African American', 'y' : 14},
    {'name' : 'Unknown or Not Reported', 'y' : 10},
    {'name' : 'Native Hawaiian or Other Pacific Islander', 'y' : 8},
    {'name' : 'American Indian/Alaskan Native', 'y' : 2},


]


def data_summary(request):
    return render(request, 'data_summary.html', {
        'DIAGNOSIS': json.dumps(diagnosis),
        'GENDERS': json.dumps(genders),
        'RACES': json.dumps(races)
    })
