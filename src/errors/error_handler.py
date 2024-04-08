from src.http_types.http_response import HttpResponse
from .errors_types.http_conflict import HttpConflict
from .errors_types.http_not_found import HttpNotFound

def error_handler(error: Exception) -> HttpResponse:
    if isinstance(error, (HttpConflict, HttpNotFound)):
        return HttpResponse(
            body={
                "errors": [{
                    "error_name": error.name,
                    "details": error.message
                }]
            }, status_code= error.status_code
        )
    
    return HttpResponse(
            body={
                "errors": [{
                    "error_name": "",
                    "details": str(error)
                }]
            },
            status_code= 000
        )