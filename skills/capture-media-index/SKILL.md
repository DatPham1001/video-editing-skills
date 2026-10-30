---
name: capture-media-index
description: "Lập/cập nhật chỉ mục ảnh và video capture cho dựng phim; dùng checkpoint SHA-256 để chỉ phân tích file mới. Nhận diện và dọn bản trùng byte-identical vào khu cách ly có thể khôi phục, giữ bản gốc, ID và liên kết tư liệu."
---

# Capture Media Index

Tổ chức ảnh/video người dùng chụp hoặc lưu thành thư viện tư liệu dựng có thể truy vấn: **câu kịch bản → chủ đề → file → cảnh/đoạn phù hợp → cách dùng → giới hạn bằng chứng**.

## Phạm vi

- Lập thư viện lần đầu, cập nhật file mới, dọn file trùng, tìm tư liệu hoặc bổ sung lớp OCR/cảnh/audio được người dùng chỉ định.
- Chọn thư mục từ ngữ cảnh. Với dự án hiện tại có thể dùng `D:\Knowlegde\capture`; không mặc định đường dẫn đó cho mọi workspace.
- Chỉ tạo/sửa skill không phải lệnh chạy phân tích hay dọn file thật. Một yêu cầu index không tự cho phép dựng/xuất video, upload media, tìm báo hoặc công khai thư viện.

## Quy tắc cập nhật

1. Đọc `AGENTS.md`, `AI_GUIDE.md`, `INDEX.md`, catalog/checkpoint và alias đường dẫn nếu đã có. Với cấu trúc phẳng, chúng là `catalog.json`, `checkpoint.json`, `path-aliases.json` ngay thư mục gốc; thư viện cũ có thể dùng `_catalog/`.
2. **“Cập nhật” chỉ xử lý file thực sự mới.** Giữ mô tả, ID, OCR, transcript, khung mẫu và kết quả cũ. Không phân tích lại toàn bộ để làm mới index.
3. Nhận dạng bằng SHA-256 của file, không chỉ tên/ngày sửa. File đổi tên, di chuyển hoặc bản sao cùng hash là tư liệu đã có; chỉ bổ sung vị trí/alias nếu cần. Các file cùng hash chỉ cần một kết quả phân tích.
4. Cùng đường dẫn nhưng hash đổi: ghi `changed_existing_keep_previous`; chưa tự phân tích lại. Mất file không tự xóa hồ sơ cũ. Nếu nghi đổi tên đồng thời chỉnh nội dung, giữ ứng viên chờ đối chiếu thay vì tự kết luận mới.
5. Chỉ **“lập lại index từ đầu”**, **“phân tích lại toàn bộ”** hoặc yêu cầu tương đương mới cho phép xử lý lại toàn thư viện. Một yêu cầu cụ thể nghe/chép, OCR hoặc phân tích cảnh cho clip cũ cho phép đúng lớp được giao, giữ nguyên lớp trước đó.
6. Ghi checkpoint sau khi đầu ra của từng file/lớp đã tồn tại và được kiểm tra. Lưu lịch sử rồi thay checkpoint nguyên tử; không đánh dấu xong ngay khi mới quét thấy file.

## Thực hiện

### 1. Quét và lập delta

Chỉ kiểm kê file ảnh/video gốc; loại `_catalog`, `_duplicates` và đầu ra do chính workflow tạo. Không đổi tên, di chuyển, nén hoặc chỉnh file gốc để lập thư viện, ngoại trừ bản trùng hoặc việc tổ chức lại thư mục được người dùng giao. Khi tổ chức lại, chỉ sửa đường dẫn/alias, giữ ID, hash, mô tả và mức phân tích; không xem là file mới. Hash theo luồng để tránh nạp video lớn vào bộ nhớ.

Có thể dùng helper chỉ đọc:

```powershell
python <skill-dir>/scripts/plan_update.py <thu-muc-capture> --report <duong-dan-bao-cao.json>
```

Helper chỉ phân loại file mới/cũ/trùng/thay đổi; không xem ảnh, không chép lời, không cập nhật checkpoint. Nếu chưa có checkpoint, mọi hash chưa biết là ứng viên mới. Khi có catalog từ thư mục cũ như `news`, đối chiếu hash và dùng lại kết quả trước khi phân tích.

### 1b. Dọn các bản trùng

Quét trùng khi lập/cập nhật thư viện. Nếu người dùng giao dọn file trùng hoặc đã yêu cầu kèm dọn khi cập nhật, thực hiện theo [references/duplicate-cleanup.md](references/duplicate-cleanup.md). Nếu chỉ giao kiểm kê/tìm tư liệu, trả danh sách trùng, chưa di chuyển.

- Chỉ tự dọn file **cùng dung lượng và SHA-256**. Giữ một bản ưu tiên đang được index/tham chiếu; giữ nguyên ID, mô tả và mọi lớp phân tích.
- Chuyển bản dư sang `_duplicates/<run-id>/` kèm nhật ký khôi phục; không xóa vĩnh viễn mặc định. Đây là khu cách ly, chưa giải phóng dung lượng đĩa.
- Đối chiếu liên kết trước khi chuyển; cập nhật đường dẫn/alias về bản giữ lại. Không sửa nội dung tóm tắt để dọn trùng. Nếu không bảo toàn được liên kết dự án dựng, giữ file đó và báo trạng thái chờ.
- Ảnh crop, ảnh nén lại, screenshot cùng bài nhưng khác phần, video khác thời lượng/âm thanh hoặc hash khác là **gần trùng**, chỉ nhóm để xem xét; chưa tự loại.

Helper chỉ đọc để lập kế hoạch: `python <skill-dir>/scripts/plan_duplicates.py <thu-muc-capture> --report <bao-cao.json>`. Không tự thực thi dọn chỉ vì tạo xong báo cáo.

### 2. Hiểu nội dung file mới

- **Ảnh:** xem ảnh thật; mô tả cảnh/người/hành động, chữ nhìn thấy, số liệu, bố cục và loại tư liệu. Trích OCR với mức đầy đủ và độ chắc chắn thực tế. Không gọi mô tả thủ công vài dòng là OCR toàn văn.
- **Video:** lấy metadata kỹ thuật, xem các khung mẫu để định hướng. Nếu mới xem mẫu, ghi `sample_frames_only`; không nói đã phân tích từng cảnh. Với yêu cầu phân tích đầy đủ, chia cảnh và xem đoạn chuyển cảnh; ghi thời gian bắt đầu/kết thúc, hành động, chữ và khả năng sử dụng của từng đoạn.
- **Âm thanh:** stream có audio không có nghĩa đã nghe. Chỉ ghi lời nói, ngôn ngữ, nhạc hoặc transcript sau khi thực sự nghe/chép; giữ timestamps và mức chắc chắn. Chưa nghe thì ghi rõ.
- Phân biệt nhận dạng trực quan với xác minh nguồn, ngày và địa điểm. Không suy ngày sự kiện từ ngày sửa file, không đoán nhạc từ phụ đề, không dùng ảnh minh họa AI như ảnh hiện trường.

### 3. Gắn ý nghĩa cho dựng

Mỗi hồ sơ cần: ID ổn định, đường dẫn/hash; mô tả; chủ đề và từ khóa; chữ/transcript theo mức đã xử lý; nguồn/ngày nếu biết; vai trò dựng; metadata khung hình/thời lượng; giới hạn và mức phân tích.

Các vai trò thường dùng: ảnh dẫn chứng/trích bài báo, B-roll bối cảnh, bản đồ, biểu đồ/số liệu, phản ứng người xem, clip montage hoặc đoạn có lời nói. Nêu lý do phù hợp với câu kịch bản. Liên quan chủ đề không tự có nghĩa chứng minh trực tiếp sự kiện.

Đề xuất crop/zoom/overlay hoặc đoạn dùng chỉ ở mức được xem. Chỉ ghi in/out đã xác nhận sau khi mở đoạn gốc. Không điền timecode, lời thoại, địa điểm hoặc nguồn cho đủ hồ sơ.

### 4. Xuất thư viện

Đọc [references/catalog-format.md](references/catalog-format.md) khi ghi dữ liệu hoặc bổ sung lớp phân tích. Tái sử dụng cấu trúc hiện có:

Với thư viện đã hợp nhất, dùng cấu trúc ở mục “Thư viện capture hợp nhất” bên dưới. Với thư viện khác, tái sử dụng cấu trúc hiện có; danh sách sau là dạng metadata cũ có thể gặp:

- `AI_GUIDE.md`: AI nên đọc gì và chọn tư liệu thế nào.
- `INDEX.md`: chủ đề, công dụng dựng và link từng hồ sơ.
- `_catalog/catalog.json`: bản ghi tìm kiếm được.
- `_catalog/items/<ID>.md`: nội dung, giới hạn, ảnh/khung mẫu và liên kết ngược.
- `_catalog/checkpoint.json`: tiến độ, hash, mức phân tích.
- `_catalog/path-aliases.json`: vị trí cũ → vị trí hiện tại khi cần.

Giữ mã MEDIA đã có; ID mới nối tiếp high-water mark và cả những ID đang tồn tại trong kho liên quan, không dựa số lượng file để đánh lại mã. Nếu chưa có namespace chung, chọn một namespace nhất quán cho thư viện mới.

Không dịch lại/chỉnh sửa ảnh capture cũ chỉ vì workflow references có quy tắc chụp báo tiếng Việt. Quy trình này mô tả **file người dùng đã lưu**. Bổ sung OCR, cảnh và audio là lớp riêng có provenance, không xóa kết quả trước.

### 5. Kiểm tra và bàn giao

- File/preview tồn tại, hash file gốc không đổi, đường dẫn và ID không lẫn bản cũ/bản mới.
- Phạm vi ảnh, video và audio được khai đúng; đoạn in/out nằm trong thời lượng thật và đã được xem.
- File đổi tên/trùng không bị phân tích lần hai. Chỉ mục tìm được file theo chủ đề/công dụng và mở tới đúng file gốc.
- Chỉ checkpoint các phần đã kiểm tra. Có lỗi/không đọc được thì lưu trạng thái đó, không gọi hoàn tất phân tích.

Bàn giao: link AI_GUIDE/INDEX; số file mới, cũ dùng lại, trùng và thay đổi đang chờ; lớp phân tích đã làm và còn thiếu. Nếu có dọn: nêu bản giữ lại, số bản cách ly, đường dẫn nhật ký khôi phục và dung lượng được loại khỏi tập hoạt động; không gọi đó là dung lượng đĩa đã giải phóng. Không tự tạo tác vụ chạy nền.

## Khi AI dùng thư viện để dựng

Tìm trong catalog trước, mở hồ sơ và đọc giới hạn, rồi mở đúng file gốc. Với clip, xem/nghe chính khoảng định dùng trước khi quyết định in/out. Trả lời theo mẫu: **file + đường dẫn → nội dung → phù hợp câu nào → cách dùng → timecode đã kiểm tra → giới hạn**. Không biến thao tác tìm tư liệu thành tự chỉnh timeline khi người dùng chưa giao dựng.


## Thư viện capture hợp nhất theo yêu cầu hiện hành

Nếu thư viện capture đã hợp nhất, ưu tiên cấu trúc người dùng chọn: `capture/capture-me/` chứa ảnh/video cá nhân; `capture/capture-notion-auto/` chứa ảnh references tự động, không chia tiếp theo nguồn/Idea. **Một bộ** `catalog.json`, `checkpoint.json`, `path-aliases.json`, `AI_GUIDE.md`, `INDEX.md`, `AGENTS.md` ở gốc `capture/` cho cả hai nhóm; dùng trường `collection` để phân loại. Không tạo catalog/guide riêng trong hai thư mục media. Hồ sơ MEDIA và lịch sử dùng chung `_catalog/`; diagnostics references có thể giữ ở thư mục hỗ trợ bên ngoài được guide dẫn tới.

Quét/cập nhật ở gốc capture để nhận cả hai nhóm. Giữ nguyên MEDIA ID, hash, mô tả, giới hạn và lớp phân tích khi di chuyển; cập nhật link và alias, không xử lý lại. Khi hợp nhất, kiểm tra trùng ID/hash, lưu snapshot hai checkpoint trước khi gộp, cấp ID mới trên high-water toàn kho. Quy ước này thay cấu trúc capture-notion riêng/phẳng khi người dùng đã yêu cầu hợp nhất; thư viện khác giữ bố cục hiện có.
