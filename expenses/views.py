from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from MainExpensis.error_messages import expense_value_cannot_be_negative_error
from expenses.models import Expense
from expenses.serializers import ExpenseSerializerPost, ExpenseSerializerGet
from expenses.service import get_expense_by_id
from users.service import get_user_by_auth_header


class ExpenseList(APIView):
    """ Create a new expense """

    def post(self, request):
        serializer = ExpenseSerializerPost(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data['value'] < 0:
                return Response(status=status.HTTP_400_BAD_REQUEST, data=expense_value_cannot_be_negative_error)
            serializer.validated_data['user'] = get_user_by_auth_header(request.headers.get('Authorization'))
            save_resp = serializer.save()
            return Response(ExpenseSerializerGet(save_resp).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """ Get expenses by logged user"""

    def get(self, request):
        user = get_user_by_auth_header(request.headers.get('Authorization'))  # get user by auth header
        if user is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        expenses = Expense.objects.filter(user=user).order_by('-date', '-id')
        serializer = ExpenseSerializerGet(expenses, many=True)
        return Response(serializer.data)


class ExpenseDetail(APIView):
    """ update expense """

    def put(self, request, expense_id):
        expense = get_expense_by_id(expense_id)
        token_user = get_user_by_auth_header(request.headers.get('Authorization'))
        if expense is None or expense.user != token_user:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ExpenseSerializerPost(expense, data=request.data)
        if serializer.is_valid():
            save_resp = serializer.save()
            return Response(ExpenseSerializerGet(save_resp).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """delete expense"""

    def delete(self, request, expense_id):
        expense = get_expense_by_id(expense_id)
        if expense is None or expense.user != get_user_by_auth_header(request.headers.get('Authorization')):
            return Response(status=status.HTTP_404_NOT_FOUND)
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request, expense_id):
        expense = get_expense_by_id(expense_id)
        if expense is None or expense.user != get_user_by_auth_header(request.headers.get('Authorization')):
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ExpenseSerializerGet(expense)
        return Response(serializer.data)
