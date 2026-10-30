# Hồ sơ media, lớp phân tích và checkpoint

## Ưu tiên cấu trúc capture hợp nhất

Khi người dùng đã hợp nhất, ảnh/video ở `capture/capture-me/` và `capture/capture-notion-auto/`; catalog/checkpoint/alias và các guide dùng chung tại gốc capture. Dùng collection để phân nhóm; không tạo lại references/capture-notion hoặc một catalog riêng cho từng nhóm. Hồ sơ MEDIA dùng chung `_catalog/items/`. Các ví dụ capture-notion phẳng bên dưới chỉ áp dụng thư viện độc lập chưa hợp nhất, không áp dụng dự án hiện hành.

## Cấu trúc phẳng cho capture-notion

Trong `capture-notion/` không tạo thư mục con: ảnh trực tiếp tại gốc, `catalog.json`, `checkpoint.json`, `path-aliases.json`, `AI_GUIDE.md`, `INDEX.md`, `AGENTS.md`. Đặt tên ảnh có source ID và số khung. Hồ sơ từng MEDIA, preview, lịch sử, chẩn đoán và báo cáo đặt ngoài capture trong thư mục hỗ trợ được guide nêu rõ. Các ví dụ `_catalog/items` và `_catalog/checkpoint` bên dưới là định dạng thư viện cũ, không được dùng để tạo lại thư mục trong capture-notion. Khi gom phẳng theo yêu cầu, giữ nguyên ID/hash và các lớp phân tích, chỉ cập nhật vị trí/link/alias.

## Trường nên lưu cho mỗi file

| Trường | Nội dung |
|---|---|
| id, file_name, current_path, sha256 | Danh tính và vị trí hiện tại |
| aliases, duplicate_of, canonical_path | File di chuyển hoặc bản sao byte-identical; không phân tích lại, giữ ID và mô tả |
| storage_state, previous_path, quarantine_path | Trạng thái bản dư cách ly và vị trí để khôi phục; không tự xóa vĩnh viễn |
| kind, topics, keywords | Ảnh/clip, chủ đề và từ khóa có nghĩa cho dựng |
| description | Nội dung thực sự nhìn thấy, khác với giả thuyết/nhận xét |
| on_screen_text, ocr_status | Phần chữ đọc được; đầy đủ, một phần, lỗi hay chưa làm |
| source_url, source_name, event_date, location | Nguồn và bối cảnh nếu có; dùng null/chưa xác minh khi thiếu |
| edit_role, editing_suggestion | Evidence, B-roll, map/chart, montage, phản ứng, lời nói; cách dùng đề xuất |
| technical | Kích thước hiển thị, rotation, khung dọc/ngang; video thêm duration, FPS, codec, audio stream |
| observed_frames | Timestamp khung đã xem và đường dẫn preview |
| scenes | Mốc cảnh, mô tả hành động/chữ, bằng chứng phần đã xem |
| audio_status, transcript | Chưa nghe, đã nghe, tiếng/nhạc/lời nói; transcript có thời gian nếu thực hiện |
| verified_edit_ranges | In/out đã xem và lý do phù hợp câu kịch bản; bỏ trống khi chưa xem |
| related_ideas, relation_type | Được dẫn trực tiếp, khớp chi tiết, liên quan chủ đề hoặc chưa rõ |
| limitations, analysis_scope, provenance | Điểm không được suy ra, mức xử lý thật, công cụ/lần đọc và cache tái sử dụng |

Không buộc mọi file có đủ giá trị. Thông tin chưa biết để trống có nhãn, không tự điền. Mô tả định hướng dựng không phải xác nhận mọi điều ảnh/video hàm ý là thật.

## Khung Markdown cho từng hồ sơ

1. ID, tên, link file gốc, chủ đề, vai trò dựng.
2. Mô tả nhìn thấy và chữ có thể đọc; nguồn/date nếu biết.
3. Gợi ý đoạn kịch bản phù hợp/cách dùng, kèm giới hạn.
4. Ảnh gốc hoặc khung mẫu có timestamp; cảnh và audio theo lớp đã thực hiện.
5. In/out chỉ sau khi kiểm tra đoạn gốc; thời lượng ảnh tĩnh trong timeline là lựa chọn dựng, không phải thuộc tính tư liệu.
6. Hash, lịch sử vị trí và mức phân tích.

Link ảnh trong hội thoại dùng đường dẫn tuyệt đối. Đầu ra phải trỏ file thật; không dựng ảnh minh họa rồi gọi là khung gốc. Giữ thư mục preview trong `_catalog` để không quét nhầm preview thành media mới.

## Các lớp tiến độ

```text
inventory_hashed
visual_image_reviewed
sample_frames_only
scene_log_reviewed
audio_listened
transcript_reviewed
ocr_partial / ocr_complete_reviewed
edit_ranges_verified
```

Một file đã index với `sample_frames_only` không được đổi thành `scene_log_reviewed` chỉ vì lần sau mở lại catalog. Một yêu cầu riêng bổ sung transcript/cảnh cho file cũ cho phép đúng lớp ấy; một yêu cầu cập nhật chung chỉ bổ sung file mới.

## Checkpoint tương thích thư viện hiện có

```json
{
  "schema_version": 1,
  "high_water_mark": 41,
  "items": [
    {
      "id": "MEDIA-041",
      "file_name": "new-clip.mp4",
      "current_path": "đường-dẫn-file-thật",
      "sha256": "SHA-256-thật",
      "analysis_scope": "sample_frames_only",
      "skip_semantic_reanalysis_on_update": true
    }
  ]
}
```

Ví dụ là schema, không phải trạng thái dự án. Checkpoint hiện tại có thể chưa có schema/high-water; khi tiếp tục, bảo toàn trường cũ và tính high-water từ ID hiện có trong phạm vi thư viện. Giữ namespace toàn kho nếu thư viện đã liên kết knowledge.

Chỉ ghi trạng thái hoàn tất sau khi file đầu ra, mô tả và preview được kiểm tra. Trước khi sửa checkpoint, lưu bản lịch sử. Ghi JSON mới sang file tạm cùng thư mục rồi đổi tên nguyên tử. Không ghi checkpoint từ kế hoạch quét khi chưa phân tích.

## Quyết định delta

| Tình huống | Hành động |
|---|---|
| Hash đã có | skip_reuse; vị trí đổi chỉ thêm alias |
| File mới nhưng trùng hash một ứng viên mới khác | duplicate_of_new_candidate; phân tích một lần |
| Cùng đường dẫn, hash khác | changed_existing_keep_previous; không tự xử lý lại |
| Hash mới, đường dẫn mới, các file cũ còn đó | new_candidate |
| File cũ mất đồng thời có file hash/tên mới | new_candidate_needs_identity_check; có thể là đổi tên kèm sửa nội dung |
| File chỉ không xuất hiện trong lần quét | missing_from_snapshot; không tự xóa mô tả |

Hash khác không đủ kết luận hai ảnh khác nội dung về mặt ngữ nghĩa: JPG nén lại, PNG và bản crop có thể cùng bài/ảnh. Ghi quan hệ cùng nguồn khi đã xem, không gọi các bản này là chứng cứ độc lập. Không tự gộp gần-trùng chỉ dựa cảm giác.

Khi được giao dọn trùng, xem [duplicate-cleanup.md](duplicate-cleanup.md). Giữ bản canonical và các ID/ghi chú; chuyển bản dư byte-identical vào `_duplicates/<run-id>` với log trong `_catalog/dedup-history`. Hai thư mục này không thuộc tập media mới. Dọn vị trí lưu không làm mới mức phân tích của file.

## Dùng kết quả để dựng

Ví dụ câu hỏi: tìm B-roll cảnh sát/đám đông khung dọc; ảnh trích bài có tên nguồn và ngày; đồ thị có cùng đơn vị với lời dẫn; clip có lời nói cần giữ audio. Tìm từ khóa và edit_role trước; không chọn chỉ bằng filename.

Khi được giao chọn tư liệu, có thể lập bảng: câu kịch bản, file, in/out đã xem, vai trò, full-frame/crop/overlay, audio và giới hạn. Với file chưa được xem đầy đủ, nêu việc còn phải kiểm tra thay vì bịa timecode. Không suy thời gian sự kiện từ EXIF/ngày lưu nếu chưa có nguồn xác nhận.
