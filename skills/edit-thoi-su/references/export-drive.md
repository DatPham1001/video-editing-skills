# Xuất MP4 và giao qua Google Drive

“Xuất clip”, “xuất 1080p” và các yêu cầu xuất tương đương gồm render, kiểm tra MP4 và tải file lên Drive qua trình duyệt trong Codex. Yêu cầu “không đăng Drive”, “chỉ lưu local” hoặc đích khác được ưu tiên cho lần xuất đó. Chỉ mở hoặc khôi phục preview thì giữ ở chế độ xem trước.

## Cấu hình thư mục riêng

Đọc khóa `drive_folder_url` trong file `~/.codex/.secrets/edit-thoi-su.json` trên máy. Nếu có `CODEX_HOME` tùy chỉnh, dùng thư mục đó thay cho `~/.codex`. File JSON chỉ cần một khóa `drive_folder_url` có giá trị là URL thư mục Google Drive. URL do người dùng chỉ định cho lần xuất hiện tại được ưu tiên. Giữ file cấu hình ngoài thư mục skill, workspace và repo. Dùng tài khoản Google đang đăng nhập trong trình duyệt Codex. Giữ token, mật khẩu, cookie và file cấu hình thật ngoài gói skill và lịch sử Git.

## Render và kiểm tra file

1. Cập nhật ngày hiện trên clip thành hôm nay theo múi giờ người dùng, đồng bộ dữ liệu job trước khi render. Dùng source HD gốc và cut map đã duyệt. Nếu preview dùng proxy, dựng hình HD theo cut map rồi trỏ bản render vào nguồn HD. Mặc định xuất dọc 1080×1920 ở FPS của project, H.264/AAC. Lưu MP4 trong thư mục job theo [quy tắc phiên bản](../SKILL.md#tên-file-xuất).
2. Render Remotion với `--concurrency=2 --offthreadvideo-threads=1`. Nếu gặp lỗi tài nguyên, thử lại với `--concurrency=1 --offthreadvideo-threads=1` và giữ độ phân giải, FPS và thiết lập chất lượng của bản xuất.
3. Dùng ffprobe kiểm tra độ phân giải thực, FPS, thời lượng và số track âm thanh của chính file MP4. Xem frame từ file xuất để kiểm tra ngày đầu clip, cảnh người dẫn, popup, chia khung và phụ đề. Kiểm tra tiếng ở các điểm từng báo lỗi nếu có.

## Tải lên qua trình duyệt Codex

1. Mở đúng URL thư mục bằng trình duyệt tích hợp trong Codex. Kiểm tra tiêu đề thư mục, tài khoản đang đăng nhập và nút tạo mới. Nếu thiếu cấu hình, tài khoản phù hợp hoặc quyền tải lên, giao file local đã kiểm tra và nêu phần còn thiếu.
2. Kiểm tra trong thư mục có file đúng phiên bản chưa. Nếu đã có, đối chiếu checksum khi có thể. Nếu chỉ trùng tên và dung lượng, nêu đúng phạm vi xác minh và kiểm tra thêm trước khi tải lại. Giữ các phiên bản trước.
3. Trong Drive chọn **Mới → Tải tệp lên**. Dùng trình chọn tệp của trình duyệt với đường dẫn tuyệt đối tới MP4 đã kiểm tra. Giữ quyền chia sẻ hiện tại.
4. Chờ Drive báo tải lên hoàn tất và xác nhận file xuất hiện trong chính thư mục đó. Nếu trạng thái gián đoạn, kiểm tra file trong thư mục trước khi thử lại.
5. Giao link file Drive và file local. Lưu thông tin tải lên trong hồ sơ job riêng, ngoài gói skill.
