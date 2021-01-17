"""
  @Author       : liujianhan
  @Date         : 21/1/16 23:48
  @Project      : DailyTinyImprovement
  @FileName     : contextmanager_优雅的异常捕获.py
  @Description  : Placeholder
"""
import contextlib
from typing import Union, Callable


# @contextlib.contextmanager
# def catches(*exceptions, raises: Union[BaseException, Callable[[Exception], BaseException]], log=False):
#     exceptions = exceptions or (Exception,)
#     try:
#         yield
#     except exceptions as ex:
#         if callable(raises):
#             raises = raises(ex)
#         if log:
#             log_error(__name__, raises)
#         raise raises from ex
#
# @catches(ExternalServiceError, raise_to=APIError('Error calling external service'), log=True)
# def service_call(...):
#     external_service.call()

if __name__ == '__main__':
    pass