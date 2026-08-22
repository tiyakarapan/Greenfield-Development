from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def at_risk_students(request):
    return Response({'message': 'at-risk-students report is not implemented yet.'})


@api_view(['GET'])
def facilitator_mismatches(request):
    return Response({'message': 'facilitator-mismatches report is not implemented yet.'})


@api_view(['GET'])
def exam_records(request):
    return Response({'message': 'exam-records report is not implemented yet.'})


@api_view(['GET'])
def intake_report(request):
    return Response({'message': 'intake report is not implemented yet.'})


@api_view(['GET'])
def course_demand(request):
    return Response({'message': 'course-demand report is not implemented yet.'})


@api_view(['GET'])
def roster(request):
    return Response({'message': 'roster report is not implemented yet.'})


@api_view(['GET'])
def transcript(request, student_id):
    return Response({'message': f'transcript report for student {student_id} is not implemented yet.'})


@api_view(['GET'])
def export_students(request):
    return Response({'message': 'student export is not implemented yet.'})


@api_view(['GET'])
def prerequisite_check(request):
    return Response({'message': 'prerequisite-check report is not implemented yet.'})
