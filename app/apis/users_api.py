from django.http import JsonResponse


def test_api(reqeust):
    return JsonResponse(status=200, data=dict(result="패스트캠퍼스"), json_dumps_params=={"ensure_ascii": False})