## Quản lý bệnh viện

### Chức năng

#### Quản trị viên (Admin)
- **Đăng ký và đăng nhập**: Để đăng ký và đăng nhập vào tài khoản quản trị viên, thêm "adminclick" vào đuôi link. Ví dụ: [http://127.0.0.1:8000/adminclick](http://127.0.0.1:8000/adminclick)
- **Quản lý bác sĩ**:
  - Đăng ký, xem, phê duyệt, từ chối, và xóa bác sĩ.
  - Phê duyệt đề xuất làm việc của bác sĩ.
- **Quản lý bệnh nhân**:
  - Tiếp nhận, xem, phê duyệt, từ chối, và xuất viện bệnh nhân.
  - Tạo và tải xuống hóa đơn PDF cho các dịch vụ.
  - Xem, đặt, và phê duyệt lịch hẹn của bệnh nhân.

#### Bác sĩ
- **Đăng ký và đăng nhập**: Yêu cầu phê duyệt từ quản trị viên trước khi có thể đăng nhập.
- **Xem thông tin bệnh nhân**: Chỉ xem được thông tin của các bệnh nhân được chỉ định.
- **Quản lý lịch hẹn**:
  - Xem danh sách cuộc hẹn.
  - Xóa cuộc hẹn.

#### Bệnh nhân
- **Đăng ký và đăng nhập**: Yêu cầu phê duyệt từ quản trị viên trước khi có thể đăng nhập.
- **Xem thông tin bác sĩ**: Xem thông tin chi tiết của bác sĩ được chỉ định.
- **Quản lý lịch hẹn**:
  - Đặt lịch hẹn.
  - Xem trạng thái của lịch hẹn.

### Hướng dẫn chạy web
1. **Cài đặt Python**: Đảm bảo Python được cài đặt và được thêm vào đường dẫn trong quá trình cài đặt.
2. **Cài đặt các gói cần thiết**:
   ```
   pip install django==3.0.5
   pip install django-widget-tweaks
   pip install xhtml2pdf
   ```
3. **Migrate cơ sở dữ liệu**:
   ```
   py manage.py makemigrations
   py manage.py migrate
   ```
4. **Chạy server**:
   ```
   py manage.py runserver
   ```
5. **Truy cập website**: Sau khi chạy server, truy cập vào địa chỉ [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### Lưu ý
- **Đăng ký/đăng nhập admin**: Thêm "adminclick" vào đuôi link để truy cập trang đăng ký/đăng nhập admin.
- **Tạo tài khoản bác sĩ trước**: Đảm bảo đã tạo ít nhất một tài khoản bác sĩ trước khi tạo bệnh nhân mới.