# Highlight ANTON sau đầu — kiểu đã duyệt

Dùng khi hoàn thiện hoặc sửa highlight lời nói. Đây là typography riêng, không phải phụ đề hay card bài báo. Tái dùng thiết kế, không copy lời bình/timing của clip mẫu sang job khác. Cập nhật skill không tự áp vào video chưa yêu cầu sửa.

## Chữ và màu theo cảnh

- Font **Anton Regular, weight 400**, viết HOA, **tô đặc toàn bộ chữ**. Không dùng faux bold, viền rỗng, nền card đen hoặc mặc định hai màu trong cùng highlight. Font chính xác và OFL ở [assets/fonts/Anton](../assets/fonts/Anton/Anton-Regular.ttf); copy font/license vào job, tải bằng FontFace và chờ font trước render. Anton này có bộ tiếng Việt; kiểm dấu trong tiêu đề thực.
- Trên canvas 1080×1920, bản đã duyệt mở ngang glyph khoảng **1.2x**, tracking **2.5px**, căn giữa vùng tham chiếu x≈516, rộng gốc≈780px. Đây là transform của chữ, không kéo giãn người nói. Đo biên chữ sau transform để nằm trong safe zone.
- Kích thước khởi điểm: cụm ngắn≈124px, số nhấn≈200px; tiêu đề hai dòng≈134/145px, line-height≈1. Dịch xuống theo tóc/đầu trong footage: bản mẫu top≈452 cho một dòng số và≈360 cho hai dòng. Chỉ để tóc/đầu che một phần chữ; không để mất số, phủ định hay ý chính. Chữ không nằm lên mặt.
- **Chọn bảng màu từ khung hình thật:** xét tường, gỗ/cảnh vật, áo, da, màu sau grade và gradient. Màu hiện đại, dịu nhưng đủ đậm/đủ tương phản để đọc; tránh neon hoặc pastel quá nhạt chìm vào cảnh. Không khóa sage/đào cho mọi source.
- Với nền gỗ ấm, tường kem, áo navy, các màu tham chiếu có thể là sage `#9fbeae`, đào ấm `#db9a81`, xanh khói `#a5bdcb`, cát `#cbb48d`, lavender trầm `#b1acc5`. Chỉ giữ màu hợp cảnh cụ thể, có thể chọn bảng khác ở clip khác.
- **Một đoạn highlight = một màu thống nhất cho tất cả từ/số/dòng.** Chọn ngẫu nhiên trong bảng màu đã lọc, ưu tiên tránh lặp hai đoạn liền nhau khi còn lựa chọn. Xáo trộn/chọn một lần ở bước chuẩn bị, lưu `{segmentId, color}` và seed trong JSON job. Component chỉ đọc màu đã lưu; không Math.random theo frame, mount, lần preview hay render. Giữ lựa chọn khi sửa cỡ/vị trí; chỉ chọn lại khi được yêu cầu đổi màu hoặc cảnh thay đổi làm màu không phù hợp.

## Gradient, mặt và thứ tự lớp

Highlight vào/ra thì mọi lớp phụ trợ cũng fade theo; không biến thành grade tối suốt clip.

1. A-roll liên tục với grade đã duyệt.
2. Dim xung quanh nhẹ, tham chiếu opacity đen≈0.22 ở vùng xa mặt; có vùng chuyển mềm quanh mặt, không hình oval có rìa rõ.
3. Gradient đen **toàn ngang**, đỉnh xuống khoảng **1/3 chiều cao** (640px trên 1920): alpha tham chiếu 0.90 ở đỉnh, 0.72 tại 48%, 0.38 tại 79%, 0 ở cuối. Không card đen có mép cứng.
4. Chữ ANTON tô đặc.
5. Người nói/tóc/đầu đã tách nền bằng alpha matte theo đúng frame và cùng source/time/crop; lớp này ở trước chữ. Giữ đủ tóc, rìa mềm, không dùng mask hình học giả đầu. Có thể feather phần dưới để hòa với thân/nền. Một lựa chọn local đã dùng là Robust Video Matting MobileNetV3 ONNX, xử lý tuần tự và giữ recurrent states; lưu model/source hash và frame mapping trong job.
6. Phụ đề hiện theo bố cục đã duyệt.

Giữ mặt tự nhiên, không đẩy sáng riêng quá mức so với cảnh tối. Trong footage mẫu có grade brightness=1.13, lớp người trước chữ được hạ dần về **0.98 khi highlight đạt cường độ đầy đủ** (giảm khoảng 13% so với trước). Đây là điểm khởi đầu theo source, không mức phơi sáng cố định cho mọi người/camera. Feather và kiểm da, kính, tóc khi đầu chuyển động. Không nhân gain/rate tiếng hoặc chỉnh lại màu cả clip vì thay highlight.

## Motion và kiểm

Spring nhẹ theo cụm/từ, không rung liên tục; tham chiếu damping16–17, stiffness140–150, mass0.8; nhịp sau trễ≈5 frame ở 30fps. Giữ bố cục chữ ổn định khi đọc. Entrance≈0.23s, exit≈0.35s; đổi theo thời lượng câu khi cần.

Kiểm entry/hold/exit và playback: cùng một màu trong đoạn, đoạn khác đổi theo plan, tất cả glyph tô đặc/đủ dấu; chữ sau tóc theo chuyển động, ý chính còn đọc rõ; mặt cân sáng; subtitle/safe zone giữ nguyên. Hai lớp hình đều muted, tiếng vẫn một track liên tục. Preview để review; không tự xuất MP4/upload hoặc áp thiết kế mẫu vào toàn video chỉ vì skill được cập nhật.
