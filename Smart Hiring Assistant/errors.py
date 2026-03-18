class ResumeAnalyzerError(Exception):
    """Base exception for resume analyzer"""
    pass


class ParseError(ResumeAnalyzerError):
    """Raised when parsing fails"""
    pass


class ValidationError(ResumeAnalyzerError):
    """Raised when data validation fails"""
    pass