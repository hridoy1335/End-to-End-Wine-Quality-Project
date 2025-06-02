import sys

class WineException(Exception):
    def __init__(self, error_message: Exception, error_details: sys):
        self.error_message = WineException.get_detail_error_message(error_message=error_message,
                                                                      error_details=error_details)
        
    def get_detail_error_message(error_message: Exception, error_details: sys) -> str:
        _,_,exce_tb = error_details.exc_info()
        
        exception_block_line_no = exce_tb.tb_frame.f_lineno
        try_block_line_no = exce_tb.tb_lineno
        file_name = exce_tb.tb_frame.f_code.co_filename
        
        error_message = f"""
        Error Occured in file name: {file_name}
        try block line no: {try_block_line_no}
        and Exception block line number: {exception_block_line_no}
        Error message: {str(error_message)}
        """
        
        return error_message
    
    def __str__(self):
        return self.error_message
    
    def __repr__(self):
        return WineException.__name__.str()