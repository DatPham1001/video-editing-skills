# Video Editing Skills

Hai skill Codex dùng chung cho quy trình dựng video thời sự và quản lý tư liệu capture.

## Nội dung

- [`edit-thoi-su`](skills/edit-thoi-su/SKILL.md): dựng talking head bằng Remotion, cắt thô/chuẩn hóa tiếng, tư liệu, popup/chia khung, phụ đề, highlight ANTON sau đầu, màu theo phông cảnh và giao video.
- [`capture-media-index`](skills/capture-media-index/SKILL.md): cập nhật chỉ mục ảnh/video theo SHA-256, giữ dữ liệu đã phân tích, quản lý liên kết và cách ly bản trùng có thể khôi phục.

Mỗi thư mục chứa đầy đủ `SKILL.md`, metadata giao diện, references, scripts và assets hiện có. Font ANTON kèm giấy phép OFL. Preset v1 dùng Arial có sẵn trên hệ thống, với sans-serif làm font dự phòng.

## Cài đặt

Clone repository, sau đó chép hai thư mục bên trong `skills/` vào thư mục skills của Codex trên máy cần dùng (thường là `~/.codex/skills/`). Nếu đã có bản cũ, sao lưu và kiểm tra thay đổi trước khi thay thế. Mở chat mới để dùng skill.

Tham số và đường dẫn thư viện capture, ngày dựng, nguồn tư liệu, đích xuất/Drive cần phù hợp với từng máy/job. Việc cài skill không tự chạy index, dọn tư liệu, dựng phim hoặc upload.

## Kiểm tra gói

`bundle-manifest.json` liệt kê đường dẫn, dung lượng và SHA-256 của từng file skill. Gói giữ nguyên byte của các file nguồn, không chứa cache Python, video đang dựng, thư viện capture hay thông tin đăng nhập.

Để dùng quy trình xuất và tải Drive, đặt khóa `drive_folder_url` trong `~/.codex/.secrets/edit-thoi-su.json` (hoặc trong `.secrets/` dưới `CODEX_HOME` đã cấu hình). Giá trị là URL thư mục Drive của bạn. Giữ file cấu hình, token và thông tin đăng nhập ngoài repository và gói ZIP.
