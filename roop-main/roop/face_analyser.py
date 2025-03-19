import threading
#在实际编程中，当你需要同时处理多个任务，
#并且这些任务之间相互独立时，就可以使用多线程技术。
# 例如，一个程序既要实时显示视频画面，又要对视频中的图像进行处理，
# #这时就可以创建两个线程，一个线程负责显示画面，
#另一个线程负责图像处理，从而提高程序的执行效率
from typing import Any, Optional, List
#Any：表示任意数据类型。
#Optional：表示该变量可以是指定的类型，也可以是None。
#List：表示列表类型，且可以指定列表中元素的类型。

import insightface
#这行代码导入insightface库。insightface是一个开源的人脸识别工具包，
#它基于深度学习技术，提供了高质量的人脸检测、人脸识别、表情识别等功能。

import numpy
#这行代码导入roop库。roop是一个基于深度学习的换脸工具，它可以将一张脸替换到另一张图像或视频中的人脸上。
import roop.globals
#导入 roop 库的全局配置模块 globals，
# 该模块通常用于存储和管理程序运行时的全局参数（如输入路径、输出路径、帧处理器选择等）。
from roop.typing import Frame, Face

FACE_ANALYSER = None
THREAD_LOCK = threading.Lock()


#代码功能：这段代码属于人脸处理框架的初始化部分，通过全局变量和类型注解定义核心数据结构和配置，
# 并通过线程锁确保多线程环境下的稳定性。
#典型应用：在视频换脸或人脸增强场景中，FACE_ANALYSER 
# 可能负责加载深度学习模型，而 THREAD_LOCK 确保模型在多线程推理时的安全性。
def get_face_analyser() -> Any:
    global FACE_ANALYSER

    with THREAD_LOCK:
        if FACE_ANALYSER is None:
            FACE_ANALYSER = insightface.app.FaceAnalysis(name='buffalo_l', providers=roop.globals.execution_providers)
            FACE_ANALYSER.prepare(ctx_id=0)
    return FACE_ANALYSER
#线程安全的人脸分析器单例模式

def clear_face_analyser() -> Any:
    global FACE_ANALYSER

    FACE_ANALYSER = None
#清除全局人脸分析器实例的函数

def get_one_face(frame: Frame, position: int = 0) -> Optional[Face]:
    many_faces = get_many_faces(frame)
    if many_faces:
        try:
            return many_faces[position]
        except IndexError:
            return many_faces[-1]
    return None


def get_many_faces(frame: Frame) -> Optional[List[Face]]:
    try:
        return get_face_analyser().get(frame)
    except ValueError:
        return None


def find_similar_face(frame: Frame, reference_face: Face) -> Optional[Face]:
    many_faces = get_many_faces(frame)
    if many_faces:
        for face in many_faces:
            if hasattr(face, 'normed_embedding') and hasattr(reference_face, 'normed_embedding'):
                distance = numpy.sum(numpy.square(face.normed_embedding - reference_face.normed_embedding))
                if distance < roop.globals.similar_face_distance:
                    return face
    return None
