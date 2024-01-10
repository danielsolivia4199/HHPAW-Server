from rest_framework.decorators import api_view
from rest_framework.response import Response
from hhpawapi.models import Employee

@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated User Account

    Method arguments:
    request -- The full HTTP request object
    '''
    uid = request.data['uid']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    employee = Employee.objects.filter(uid=uid).first()

    # If authentication was successful, respond with their token
    if employee is not None:
        data = {
            'id': employee.id,
            'name': employee.name,
            'uid': employee.uid
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)


@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
    request -- The full HTTP request object
    '''

    employee = Employee.objects.create(
        name=request.data["name"],
        uid=request.data["uid"]
    )

    # Return the user info to the client
    data = {
        'id': employee.id,
        'name': employee.name,
        'uid': employee.uid
    }
    return Response(data)
