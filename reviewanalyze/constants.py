from rest_framework.pagination import PageNumberPagination


class BaseResponse:
    response = {}

    @staticmethod
    def json_response(status_code, data):
        response = {
            "success": True,
            "status_code": status_code,
            "data": data
        }
        return response

    def json_success_response(self, status, message, data):
        self.response = {
            "success": True,
            "error": False,
            "status_code": status,
            "message": message,
            "data": data
        }
        return self.response

    @staticmethod
    def success_response(status_code, message):
        response = {
            "success": True,
            "status_code": status_code,
            "message": message
        }
        return response

    @staticmethod
    def error_response(status_code, message):
        response = {
            "success": False,
            "status_code": status_code,
            "error": True,
            "error_message": message
        }
        return response


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 1000