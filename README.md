# BD2L-Platform
Môi trường sử dụng: conda, python 2.7
Thư viện sử dụng:  
* opencv 3.3.1  
* ffmpeg 3.4.1  

Platform đọc video và xuất video dựa theo yêu cầu của Cuộc Đua Số  
Thể lệ cuộc đua số : https://drive.google.com/file/d/0Bxfxgt9AZux0Q2JZZmcwbDZYWVk/view  
Input:  
* File video  
* Frame_id  
Cần xử lý:  
Hàm on_receive_frame ở file videoprocesshandle.py  
Sửa left, top, right, bottom, sign_id dummy data cho đúng với thuật toan, phần còn lại đã xuất theo yêu cầu đề của FPT.  
Output:  
* output.avi file video đã vẽ bounding box (muốn thêm thông tin, text thì sửa hàm on_object_found ở file videoprocesshandle.py)  
* output.txt gồm thông tin   
n  
id1 c x1 y1 x2 y2  
id2 c x1 y1 x2 y2  
Trong đó:  
n: số lượng các khung hình  
c: mã của kiểu biến báo giao thông (xem bảng 1) xác định trong khung hình thứ i  
id: chỉ số khung hình  
x1: toạ độ theo trục x ở góc trên bên trái của vùng chứa biển tại khung hình thứ i  
y1: toạ độ theo trục y ở góc trên bên trái của vùng chứa biển tại khung hình thứ i  
x2: toạ độ theo trục x ở góc dưới bên phải của vùng chứa biển tại khung hình thứ i   
y2: toạ độ theo trục y ở góc dưới bên phải của vùng chứa biển tại khung hình thứ i  
