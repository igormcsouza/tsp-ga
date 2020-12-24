from typing import List, Tuple, Callable, Any, List


RawData = List[str]
Data = List[Tuple[float, float]]
Preprocessor = Callable[[RawData], Any]
Preprocessors = List[Preprocessor]