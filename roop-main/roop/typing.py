# from typing import Any

# from insightface.app.common import Face
# import numpy

# Face = Face
# Frame = numpy.ndarray[Any, Any]
from typing import Any
from insightface.app.common import Face
import numpy as np
from numpy.typing import NDArray

# 这里第二行赋值多余，可省略
# Face = Face

# 使用 NDArray 定义 Frame 类型
Frame = NDArray[Any]
