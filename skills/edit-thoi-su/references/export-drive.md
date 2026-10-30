# Xuất MP4 và giao qua Drive

## Khi nào thực hiện

- “Xuất” / “xuất 1080p”: xuất file hoàn thiện trong folder job, giữ bản local. Không tự upload.
- **“Xuất và đẩy Drive”, “xuất xong upload Drive” hoặc yêu cầu tương đương:** xuất, QA rồi upload vào đích mặc định bên dưới. Đây là lựa chọn đích mặc định khi có yêu cầu upload, không phải quyền tự upload mọi bản preview hoặc các job không được yêu cầu.
- Nếu người dùng chỉ định đích khác hoặc chỉ lưu local trong job hiện tại, làm theo chỉ định mới đó.

## Đích mặc định đã được người dùng xác nhận

- Tên: **A.Tiktok clip**.
- URL: https://drive.google.com/drive/folders/1JyRWCQ7lxYcMST3SCGluOtYcjXdRYOuL
- Folder ID: `1JyRWCQ7lxYcMST3SCGluOtYcjXdRYOuL`.

Đây là cấu hình đích giao file do người dùng yêu cầu lưu, không phải media ID của clip mẫu. Không lưu file ID của từng video vào skill. Không thay bằng My Drive/root hoặc đoán folder qua `/u/1/my-drive`; số tài khoản trong trình duyệt không chọn tài khoản của connector.

## Các bước

1. Dùng source HD gốc và cut map đã duyệt, giữ nguyên bố cục, grade, âm và phụ đề bản cuối. Mặc định dọc 1080×1920, fps project (thường30), H.264/AAC phù hợp mạng xã hội. Không phóng proxy thấp để giả HD. Xuất file local có tên phân biệt video/version.
2. QA: ffprobe kích thước/fps/duration/số audio stream; frame mẫu từ chính MP4 cho A-roll, popup, split, phụ đề giữa màn hình; đối chiếu tiếng quanh mối cắt/điểm từng báo lỗi. Ghi đúng phạm vi kiểm, không tự nhận đã nghe toàn bộ.
3. Dùng plugin Google Drive, đọc/fetch đúng URL thư mục để xác nhận quyền truy cập và nội dung. Không yêu cầu công khai thư mục hoặc đổi sharing chỉ để upload. Nếu tài khoản đang kết nối không truy cập được, báo thiếu quyền/tài khoản và yêu cầu người dùng kết nối đúng hoặc cung cấp đích truy cập được; vẫn giữ file local đã xuất.
4. Kiểm tệp trùng trước khi ghi. Nếu đúng bản cuối đã ở trong thư mục, xác minh metadata và checksum nếu công cụ cung cấp; có thể giữ bản đó, không upload bản trùng và không nhận là mình vừa tải lên. Tên/dung lượng trùng chỉ chứng minh mức metadata, không khẳng định SHA-256 nếu chưa so được. Nếu bản cũ khác, tạo file phiên bản mới, không tự xóa/ghi đè.
5. Nếu cần tải: dùng upload của plugin với file local/reference theo schema hiện tại, MIME `video/mp4`, tên file có `.mp4` và parent folder ID đã xác nhận. Không base64 toàn video vào prompt, không chuyển sang ChatCut, không để mặc định upload root. Đọc skill Google Drive khi dùng plugin.
6. Chờ upload hoàn tất rồi đọc lại metadata/file hoặc list đúng thư mục. Kiểm tên, byte size, parent/list membership và link file trả về. Không coi “đã bắt đầu upload” là xong; nếu kết quả chưa rõ thì kiểm file hiện có trước khi retry để tránh trùng.
7. Lưu biên nhận vào hồ sơ **job**: local path/hash, destination folder, Drive file ID/URL thực, byte size, phương pháp xác minh và kết quả. Skill chỉ giữ cấu hình đích và quy trình. Giao link file trên Drive cùng đường dẫn local ngắn gọn; giữ nguyên quyền chia sẻ.
