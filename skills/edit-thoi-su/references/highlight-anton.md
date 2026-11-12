# Highlight ANTON — bố cục theo nội dung

Dùng khi hoàn thiện/sửa chữ nhấn lời nói, không đổi phụ đề hoặc card bài báo. Tái dùng thiết kế, không copy nội dung/timing của clip mẫu.

## Quy tắc đã sửa theo phản hồi người dùng

- **Hạ chữ nhấn, số và câu hỏi sát phía trên đầu.** Trên khung 1080×1920, bắt đầu ở top≈400px với cụm chữ một dòng và khoảng 365px với số cỡ lớn. Kiểm cả chân chữ và gạch chân theo tóc thật để giữ mặt rõ khi người nói chuyển động.
- **Gradient chữ nhấn dùng đen thuần, đậm toàn ngang và kéo sâu xuống 60% chiều cao**, khoảng 1152px trên khung 1080×1920. Tham chiếu độ đậm theo chiều cao khung là 100% đến y=14%, 93% tại y=24%, 60% tại y=33%, 27% tại y=42%, 7% tại y=52% và trong suốt ở y=60%. Fade cùng chữ và kiểm vùng mắt/mặt ở các khung đại diện. Bố cục popup/split dành cho graphic trực quan dùng quy tắc riêng.
- **Đoạn liệt kê bằng chữ có thể đặt giữa màn hình trên nền mờ/dim.** Với motion graphic ở giữa khung, xem [dựng theo nhịp thoại](speech-timed-editing.md). Tâm khối x=540/y=960, rộng≈790–840px. Tham chiếu blur24px/brightness0.70 so với grade; fade cùng đoạn. Danh sách hiện từng mục theo lời và tự căn giữa theo số hàng. Khi chuyển sang câu kết luận/điểm nhấn, đưa chữ trở lại phía trên; lưu placement theo từng mục nếu cần.
- ANTON Regular400, HOA tô đặc, cỡ lớn, bóng mềm; cụm≈100–150px, số ngắn có thể170–200px. Đo font thật gồm dấu/tracking/scale và kiểm không tràn/đè phụ đề.
- **Mỗi đoạn một màu pastel cố định:** vàng kem `#F4DEA8`, mint `#CAE7D7`, xanh phấn `#C5DEED`, hồng `#EDCDDB`, lavender `#D8D0EF`, đào `#F0D5B5`. Lưu theo ID; không random theo frame hoặc đổi từng chữ. Màu cờ/ảnh nguồn/phụ đề/vệt tô bài báo giữ riêng.
- Giữ animation vừa đủ, chuyển động nhẹ. Một video muted và một voice track liên tục; không đổi cut/rate/gain/grade khi chỉ sửa bố cục chữ. Kiểm entry/hold/exit, phân biệt rõ đoạn liệt kê giữa nền mờ và đoạn nhấn phía trên A-roll rõ.

## Tùy chọn lồng chữ sau đầu

Các thông số dưới đây dùng khi chọn kiểu chữ sau đầu với matte chuyển động; không có nghĩa mọi highlight đều phải tách nền hoặc đặt giữa màn hình.

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

Spring nhẹ theo cụm/từ, từng dòng trễ vài frame, gạch dưới quét sáng một lần rồi giữ chữ đủ lâu để đọc; tham chiếu damping16–17, stiffness140–150, mass0.8; nhịp sau trễ≈5 frame ở 30fps. Giữ bố cục chữ ổn định khi đọc. Entrance≈0.23s, exit≈0.35s; đổi theo thời lượng câu khi cần.

Kiểm entry/hold/exit và playback: cùng một màu trong đoạn, đoạn khác đổi theo plan, tất cả glyph tô đặc/đủ dấu; chữ sau tóc theo chuyển động, ý chính còn đọc rõ; mặt cân sáng; subtitle/safe zone giữ nguyên. Hai lớp hình đều muted, tiếng vẫn một track liên tục. Preview để review; không tự xuất MP4/upload hoặc áp thiết kế mẫu vào toàn video chỉ vì skill được cập nhật.


Quy tắc phạm vi tách nền: **chỉ bật lớp người tách nền khi layout hiện hành là chia hai/split và split progress > 0**. A-roll, highlight chữ, popup và countdown không bật matte. Không dùng điều kiện `split || highlight`; đây là mặc định hiện hành thay các preset lồng chữ sau đầu cũ.
