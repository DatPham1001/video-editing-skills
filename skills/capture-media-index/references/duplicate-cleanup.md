# Dọn file trùng, giữ khả năng khôi phục

## Ưu tiên cấu trúc capture hợp nhất

Khi người dùng đã hợp nhất, ảnh/video ở `capture/capture-me/` và `capture/capture-notion-auto/`; catalog/checkpoint/alias và các guide dùng chung tại gốc capture. Dùng collection để phân nhóm; không tạo lại references/capture-notion hoặc một catalog riêng cho từng nhóm. Hồ sơ MEDIA dùng chung `_catalog/items/`. Các ví dụ capture-notion phẳng bên dưới chỉ áp dụng thư viện độc lập chưa hợp nhất, không áp dụng dự án hiện hành.

## Quyền và phạm vi

Khi người dùng giao dọn trùng, có thể chuyển các bản dư byte-identical vào khu cách ly trong phạm vi thư mục được giao, không cần thêm một vòng hỏi xác nhận cho thao tác có thể khôi phục này. Nếu chỉ yêu cầu tạo/sửa skill, kiểm kê hoặc xem danh sách trùng thì chưa thực thi trên media thật.

Xóa vĩnh viễn hoặc xóa khu cách ly chỉ làm khi người dùng yêu cầu rõ. Nếu người dùng muốn giải phóng dung lượng nhưng chưa chỉ rõ xóa vĩnh viễn, lập danh sách cụ thể và giải thích cách ly vẫn dùng dung lượng; đừng tự coi “dọn” là cho phép mất bản sao không thể khôi phục.

## Xác định trùng

1. Quét file gốc, bỏ `_catalog` và `_duplicates`, không đi theo symlink/junction ra ngoài phạm vi. Hash theo luồng, ưu tiên so nhóm có cùng dung lượng.
2. Chỉ file có cùng dung lượng và cùng SHA-256 mới là bản trùng được dọn tự động. Trước khi chuyển, tính lại hash bản giữ lại và bản dư để tránh kế hoạch cũ khi file đã thay đổi.
3. Hash khác: không tự dọn, kể cả nhìn giống. Crop khác, ảnh có chú thích khác, JPG nén lại, PNG khác độ phân giải và clip có phần tiếng khác có thể mang thông tin cần cho edit.
4. Nhóm gần trùng có thể được ghi `possible_same_source` để người dùng xem sau. Không thay mức này bằng `duplicate_of` đã xác nhận.

## Chọn bản giữ lại

Theo thứ tự: bản được người dùng chỉ định → bản đang được catalog/checkpoint/dự án dựng tham chiếu → bản tại vị trí hiện hành đã kiểm tra → đường dẫn ổn định theo thứ tự xác định. Với byte-identical, không có bản nào chất lượng hình cao hơn chỉ vì tên hoặc ngày lưu khác.

Nếu có hai ID đã index cho cùng hash, giữ cả ID và các ghi chú riêng; chỉ cho chúng cùng trỏ tới bản giữ lại. Không xóa mô tả hoặc transcript để gộp số lượng file. Các dự án dựng ngoài workspace có thể tham chiếu bằng đường dẫn tuyệt đối: nếu biết dự án đó và không cập nhật được đường dẫn, giữ bản đang được tham chiếu, không làm hỏng media link.

## Kế hoạch và thao tác

Với thư viện phẳng `capture-notion`, không tạo `_catalog` hay `_duplicates` trong thư mục ảnh. Dùng khu hỗ trợ bên ngoài do AI_GUIDE chỉ định cho nhật ký, snapshot và cách ly; kiểm tra cả nguồn lẫn đích ở trong workspace/phạm vi người dùng giao. Quy tắc giữ hash, ID, liên kết và khả năng khôi phục không đổi. Các đường dẫn `_catalog`/`_duplicates` bên dưới áp dụng cấu trúc thư viện cũ.

Helper `scripts/plan_duplicates.py` tạo kế hoạch chỉ đọc: keeper, các bản dư, hash, dung lượng và bản dư nào có trong catalog. Đây chưa phải thao tác dọn và chưa chứng minh tất cả liên kết ngoài catalog đều an toàn.

Trước khi di chuyển:

- Kiểm tra đường dẫn nguồn và đích đã resolve đều ở trong thư mục capture được giao; từ chối nguồn symlink/junction và đường dẫn vượt thư mục.
- Ghi nhật ký vào `_catalog/dedup-history/<run-id>.json`, có trạng thái `planned`, và lưu snapshot catalog/checkpoint/alias sẽ cập nhật.
- Đích là `_duplicates/<run-id>/<relative-original-path>`; không ghi đè file có sẵn, không dùng recursive move/delete trên đường dẫn chưa kiểm tra.

Dùng thao tác filesystem native một môi trường xuyên suốt. Trên Windows ưu tiên `Move-Item -LiteralPath` hoặc API filesystem với đối tượng path rõ ràng; không ghép lệnh xóa/di chuyển qua nhiều shell.

Cho từng bản dư: xác nhận lại hash → chuyển đúng file → kiểm tra file đích và bản giữ lại còn nguyên → cập nhật nhật ký thành `quarantined`. Có lỗi thì dừng nhóm liên quan, ghi đúng trạng thái, chưa đánh dấu nhóm đã dọn xong. Nếu có bước đã chuyển thì rollback theo log hoặc để ở trạng thái khôi phục được; không chạy tiếp bằng cách xóa để né lỗi.

## Bảo toàn index

- Thay các link đường dẫn đã biết của bản dư bằng keeper hoặc thêm alias; sửa mục tiêu tham chiếu nhỏ nhất, không sinh lại mô tả/OCR/audio.
- Giữ ID cũ và dấu đã xử lý. Thêm `duplicate_of`, `canonical_path`, `previous_path`, `quarantine_path` và trạng thái lưu trữ khi phù hợp schema có sẵn.
- Catalog active/checkpoint phải tìm được nội dung qua keeper; cả hai ID cũ cùng trỏ một file vẫn giữ provenance. `_duplicates` bị bỏ qua khi quét cập nhật để bản cách ly không xuất hiện như file mới.
- Kiểm tra link Markdown, preview, metadata và liên kết dự án dựng đã biết. Không khẳng định đã sửa mọi tham chiếu ngoài workspace nếu không kiểm tra được.

## Nhật ký và khôi phục

Mỗi bản ghi log cần: original path, keeper path/ID, quarantine path, SHA-256, kích thước, trạng thái, thời điểm và link metadata snapshot. Khôi phục bằng cách kiểm tra hash bản cách ly và chuyển về original path khi đích chưa tồn tại. Nếu original path đã có file khác, không ghi đè; chọn vị trí khôi phục khác và ghi lại. Đường dẫn sau khôi phục cũng phải được kiểm tra ở trong phạm vi.

Bàn giao rõ: bao nhiêu nhóm; bản nào giữ; bao nhiêu file cách ly; file bị chặn do liên kết; gần trùng chỉ ghi nhận; nơi xem log/khôi phục. Tổng byte các bản cách ly là phần dữ liệu đưa ra khỏi tập active, **không phải dung lượng đĩa được giải phóng**.
