from typing import Any, Optional

def str_to_datetime_processor_factory(regexp, type_): ...
def boolean_to_int(value): ...
def py_fallback(): ...
def to_unicode_processor_factory(encoding, errors: Optional[Any] = ...): ...
def to_conditional_unicode_processor_factory(encoding, errors: Optional[Any] = ...): ...
def to_decimal_processor_factory(target_class, scale): ...