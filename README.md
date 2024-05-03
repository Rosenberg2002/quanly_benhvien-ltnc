
# Hospital Management
![developer](https://img.shields.io/badge/Developed%20By%20%3A-Sumit%20Kumar-red)
---
## Functions
### Quản trị viên
- Đăng ký tài khoản ủa mình. Sau đó đăng nhập (Không yêu cầu phê duyệt).
- Có thể đăng ký/xem/phê duyệt/từ chối/xóa bác sĩ (phê duyệt những bác sĩ đã xin việc vào bệnh viện của mình).
- Có thể tiếp nhận/xem/phê duyệt/từ chối/ cho bệnh nhân xuất viện (khi điều trị xong).
- Có thể tạo/tải xuống hóa đơn pdf (Tạo hóa đơn theo giá thuốc, tiền phòng, phí bác sĩ và các khoản phí khác).
- Có thể xem/đặt/phê duyệt Lịch hẹn (phê duyệt những cuộc hẹn mà bệnh nhân yêu cầu).

### Bác sĩ
- Đăng kí việc làm tại bệnh viện. Sau đó đăng nhập (Yêu cầu phê duyệt của quản trị viên bệnh viện, Sau đó bác sĩ mới có thể đăng nhập).
- Chỉ có thể xem chi tiết bệnh nhân của họ (triệu chứng, tên, số điện thoại di động) do quản trị viên chỉ định cho bác sĩ đó.
- Có thể xem danh sách bệnh nhân của mình xuất viện (bởi quản trị viên).
- Có thể xem các cuộc hẹn của mình, do quản trị viên đặt.
- Có thể xóa cuộc hẹn.

### Bệnh nhân
- Tạo tài khoản để nhập viện. Sau đó Đăng nhập (Yêu cầu phê duyệt của quản trị viên bệnh viện, Sau đó bệnh nhân mới có thể đăng nhập).
- Có thể xem thông tin chi tiết của bác sĩ được chỉ định như chuyên môn, điện thoại di động, địa chỉ.
- Có thể xem trạng thái cuộc hẹn đã đặt của họ (phải chờ xử lý/xác nhận bởi quản trị viên).
- Có thể đặt lịch hẹn (cần có sự phê duyệt của quản trị viên).
- Có thể xem/tải xuống Hóa đơn pdf (Chỉ khi bệnh nhân đó được quản trị viên xuất viện).

---

## HƯỚNG DẪN CHẠY WEB
- Cài đặt Python (3.7.6) (Đánh dấu Thêm vào đường dẫn trong khi cài đặt Python)
- Mở Terminal và thực hiện từng lệnh sau:
```
pip install django==3.0.5
pip install django-widget-tweaks
pip install xhtml2pdf
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
- Sau khi nhập xong các dòng lệnh hãy nhập URL sau vào Trình duyệt của bạn
```
http://127.0.0.1:8000/
```

## Vài lưu ý
- Để đăng kí/đăng nhập admin quản lí web thì thêm "adminclick" vào đuôi link => VD: http://127.0.0.1:8000/adminclick
- Nên có 1 bác sĩ trước mới có bệnh nhân được, tạo tài khoản bác sĩ trước khi tạo bệnh nhân



# quanly_benhvien-ltnc
