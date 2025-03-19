from roop.ui import init

# 定义 start 函数，用于启动处理逻辑
def start_processing():
    print("开始处理")

# 定义 destroy 函数，用于销毁资源
def destroy_resources():
    print("销毁资源")

if __name__ == "__main__":
    # 初始化 UI
    root = init(start_processing, destroy_resources)
    # 进入主循环，显示 UI 并处理用户交互
    root.mainloop()
# !/usr/bin/env python3

# !/usr/bin/env python3

# import sys
# import threading
# from roop import core
# from roop.ui import init


# # 定义启动处理函数
# def start_processing():
#     def run_core():
#         try:
#             # 调用核心处理函数
#             core.run()
#         except Exception as e:
#             print(f"处理过程中出现错误: {e}")
#             sys.exit(1)

#     # 创建并启动一个新线程来运行核心处理逻辑
#     thread = threading.Thread(target=run_core)
#     thread.start()


# # 定义销毁资源函数
# def destroy_resources():
#     print("销毁资源")
#     # 这里可以添加更多的资源销毁逻辑，比如关闭文件、释放内存等
#     sys.exit(0)


# if __name__ == '__main__':
#     # 初始化 UI，传入启动和销毁回调函数
#     root = init(start_processing, destroy_resources)
#     # 进入主循环，显示 UI 并处理用户交互
#     root.mainloop()