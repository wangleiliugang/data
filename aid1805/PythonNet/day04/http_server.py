# 导入HTTPSERVER类，兼容python3和python2
try:
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer  # python2
except ImportError:
    from http.server import BaseHTTPRequestHandler, HTTPServer  # python3


# 1.具体的请求处理类
class MyRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print("do get method!")
        fd = open('index.html', 'rb')
        content = fd.read()
        # 设置响应码
        self.send_response(200)
        # 设置响应头
        self.send_header('Content-Type', 'text/html')
        # 响应头设置完毕
        self.end_headers()
        # 发送响应体
        self.wfile.write(content)
        return

    def do_POST(self):
        pass


# 2.搭建并启动服务器
addr = ('127.0.0.1', 10120)
# 生成HTTP服务器对象
server = HTTPServer(addr, MyRequestHandler)
# 启动HTTP服务器
server.serve_forever()
