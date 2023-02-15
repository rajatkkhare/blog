def api_resp(status: int, data: [dict, str] = None, headers: dict = None) -> tuple:
    if status // 100 == 2:
        return {"status": status, "message": "success", "data": data}, status, headers
    return {"status": status, "message": "error", "errors": data}, status, headers


def api_errors():
    return {
        "MethodNotAllowed": {
            "status": 405,
            "message": "The method is not allowed for the requested URL.",
        },
        "NotFound": {"status": 404, "message": "The requested URL was not found on the server."},
    }
