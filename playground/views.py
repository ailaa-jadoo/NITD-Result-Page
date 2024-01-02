from django.shortcuts import render
from django.http import HttpResponse
from urllib3.exceptions import InsecureRequestWarning
import requests

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# def say_hello(request):
#     return render(request, 'hello.html')

def search_student(request):
    return render(request, 'search_student.html')

def student_details(request, student_id):
    sgcg = "https://erp.nitdelhi.ac.in/CampusLynxNITD/CounsellingRequest?sid=2005&refor=StudentSeatingMasterService"
    details = "https://erp.nitdelhi.ac.in/CampusLynxNITD/CounsellingRequest?sid=2002&refor=StudentSeatingMasterService"
    grades = "https://erp.nitdelhi.ac.in/CampusLynxNITD/CounsellingRequest?sid=2003&refor=StudentSeatingMasterService"

    data_to_send_1 = f'jdata={{"sid":"2005","mname":"ExamSgpaCgpaDetailOfStudent","studentID":"{student_id}","instituteID":"NITDINSD1506A0000001","registrationID":"NITDRETD2208A0000001"}}'
    data_to_send_2 = f'jdata={{"sid":"2002","mname":"ExamSgpaCgpaDetailOfStudent","studentID":"{student_id}","instituteID":"NITDINSD1506A0000001","registrationID":"NITDRETD2208A0000001"}}'

    sgcg_response = requests.post(sgcg, data=data_to_send_1, headers={'Content-Type': 'application/x-www-form-urlencoded'}, verify=False).json()
    details_response = requests.post(details, data=data_to_send_2, headers={'Content-Type': 'application/x-www-form-urlencoded'}, verify=False).json()

    if not details_response:
        return render(request, 'error.html', {'student_id': student_id})

    collapse = ["", "collapseOne", "collapseTwo", "collapseThree", "collapseFour", "collapseFive", "collapseSix", "collapseSeven", "collapseEight"]
    semester = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight"]

    responses = []
    for stynumber in range(1, 8):
        data_to_send = f'jdata={{"sid":"2003","mname":"studentGrade","studentID":"{student_id}","instituteID":"NITDINSD1506A0000001","stynumber":{stynumber}}}'
        grades_response = requests.post(grades, data=data_to_send, headers={'Content-Type': 'application/x-www-form-urlencoded'}, verify=False).json()

        if not grades_response:
            break

        responses.append(grades_response)

    return render(request, 'student_details.html', {'sgcg': sgcg_response, 'details': details_response, 'grades': responses, 'student_id': student_id, 'collapse': collapse, 'semester': semester})
