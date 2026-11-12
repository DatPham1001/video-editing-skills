# Dựng theo nhịp thoại

## Chọn bố cục

Giữ mật độ animation vừa phải: mặc định là A-roll và phụ đề, dùng chữ highlight cho điểm nhấn. Chỉ chọn motion graphic khi chuyển động/quan hệ/diễn biến trực quan giúp hiểu nội dung hoặc người dùng yêu cầu rõ hiệu ứng đó. Không minh họa mọi câu bằng một card/icon mới, không coi “thiếu graphic” là yêu cầu lấp kín toàn bộ thời lượng.

Với lời liệt kê, hiện từng mục bằng chữ đúng lượt nói; với cụm nhấn, cho typography nổi lên màn ảnh, chuyển động nhẹ và giữ đủ để đọc. Không tự dựng tên lửa, máy bay, khiên, chuông hay biểu tượng khác chỉ để thay cho một từ đã đủ rõ bằng chữ. Các đoạn bình luận trừu tượng cần khoảng nghỉ hình trên người nói. Graphic đã được yêu cầu bỏ thì trả về A-roll; giữ hoặc dùng highlight đúng câu khi có điểm nhấn, không tự thay bằng một animation khác.

Hạ chữ nhấn, số và câu hỏi sát phía trên đầu. Dùng gradient đen đậm kéo sâu xuống và tan mềm, giữ mặt người nói rõ. **Các mục liệt kê có thể ở giữa màn hình trên nền video mờ/dim.** Motion graphic giải thích một cơ chế có thể đặt giữa theo nhịp như các mẫu bên dưới. ANTON HOA tô đặc, mỗi đoạn một màu pastel cố định, không đè phụ đề. Lưu placement theo đoạn hoặc từng mục khi lời chuyển từ danh sách sang nhận định/kết luận. Đọc [highlight theo nội dung](highlight-anton.md); không chuyển mọi graphic về giữa.

Chia khung luôn dùng nền video gốc làm mờ/dim và lớp người nói tách nền rõ nét phía trước; đọc [split tách nền](split-presenter-matte.md). Chuẩn bị matte đủ mọi frame trước khi giao preview, không dùng crop còn nguyên hậu cảnh làm bản thay thế.

Popup/split dành cho tư liệu, ảnh, bài báo và graphic minh họa, giữ bố cục thông tin phía trên đầu đã duyệt; không tự đổi split thành popup khi chỉnh chữ. Danh sách chỉ có nhãn/từ hiện từng ý giữa nền mờ theo lời. Chỉ dùng card danh sách khi có minh họa trực quan hoặc người dùng yêu cầu card rõ ràng; card cao theo số hàng đã hiện.

## Canh đúng câu

- Mốc phút/giây người dùng chỉ là điểm tìm câu. Đọc transcript/phụ đề bản hiện hành, đối chiếu audio khi biên chưa rõ, lưu start/end theo cụm thực sự được nói. Giữ phủ định, câu dẫn và các từ như “bị gán nhãn”; không biến câu thuật lại thành khẳng định của graphic.
- Phân biệt thời gian source/master với thời gian local của composition. Nếu có cắt lại hoặc chèn pause, ánh xạ qua cut/retime map; chọn một timebase cho mỗi lớp và ghi rõ, không bù offset hai lần.
- Nhận định/câu hỏi ngắn: một beat, một màu cố định. Các ý nối tiếp hiện lần lượt; không để tên vấn đề sau hiện trước khi người nói nhắc tới. Graphic bình luận có thể cho icon người xuất hiện ở câu nhắc nhóm người, rồi bong bóng ba chấm ở câu nhắc bình luận. Không tự bịa trích dẫn hoặc gán phát ngôn cho nhân vật thật.
- Bài báo vào ở câu nhắc quyết định/chỉ đạo hoặc sự kiện mà bài hỗ trợ. Giữ khoảng 4 giây đọc rõ sau entry khi nhịp thoại cho phép; dùng [ảnh chụp dài có tiêu đề, logo và nội dung](evidence-highlighting.md) với vùng nhìn giới hạn. Khi câu chuyển ý, cho card ra đúng nhịp.
- Mỗi capture evidence tự tạo vệt tô màu cho phần khớp thoại, bao gồm toàn bộ số và đơn vị được nhắc; lưu vùng/timing và kiểm trước/khi/sau quét theo [highlight capture evidence](evidence-highlighting.md). Không tô câu/số không liên quan hoặc sửa nội dung nguồn.

## Chữ bật lên

Trên khung 1080×1920, đặt chữ nhấn một dòng ở top khoảng 400px và số lớn ở top khoảng 365px, rộng 790–840px. Canh theo tóc và mặt. Graphic theo popup/split đặt top khoảng 280px. Riêng liệt kê căn tâm khối x=540/y=960 và làm mờ/dim nền trong khoảng đó. Đo font thật gồm dấu tiếng Việt/scale; ANTON khoảng 100–150px cho cụm, 170–200px cho số ngắn, giảm theo độ dài. Danh sách tự căn giữa khối theo số hàng; phụ đề giữ 46px và vị trí đã duyệt.

Entry dùng spring với damping≈13, stiffness≈180, mass≈0.8; scale khoảng 0.66→1, trượt lên nhẹ, góc nghiêng nhỏ về 0. Gạch sáng quét một lần sau entry khoảng frame 6–22, dấu hỏi thêm khi câu hỏi cần nhấn. Tránh nhấp nháy liên tục, không đổi màu mỗi chữ/frame. Exit fade ngắn. Tất cả hiệu ứng chạy theo frame, không CSS animation hoặc random trong render.

## Motion graphic theo từng nhịp

- **Tỷ lệ trong tổng số.** Hiện mẫu số trước bằng lưới ô hoặc nhóm biểu tượng. Khi lời thoại nhắc tới tập con, lần lượt đổi màu đúng số phần tử, hiện phân số và tên nhóm. Video 10 dùng 33 ô rồi sáng 27 ô, đặt khối ở vùng trên. Số nào thuộc lời bình và chưa được bài báo xác nhận thì lưu rõ trong dữ liệu job, không gắn vào ảnh báo như số liệu của nguồn.
- **Cơ chế nhân quả.** Đặt card giữa khung nếu chuyển động là trọng tâm. Dùng các nhịp nối tiếp như người mua gom, sức ép nguồn cung rồi đường giá tăng. Cho mũi tên, đường biểu diễn hoặc nhãn xuất hiện đúng lúc từng ý được nói. Đường minh họa có thể thể hiện hướng, chỉ thêm mức giá hoặc tỷ lệ khi có dữ liệu nguồn.
- **Diễn biến theo mùa hoặc chuỗi cung ứng.** Dùng một card với icon chuyển động và trạng thái đổi theo lời, như tuyết/mùa đông rồi áp lực nguồn cung. Giữ vài dấu hiệu dễ đọc trên khung dọc và chừa khoảng phụ đề. Dùng tông tối và một màu nhấn chính. Các card giải thích này vẫn đứng riêng với ảnh báo và chữ ANTON.
- Lưu ID, frame vào/ra và vị trí của từng lớp để sửa độc lập trong preview. Sau khi sửa ảnh báo, giữ các lớp chữ nhấn đã duyệt và kiểm thứ tự trước/sau card.

## Tư liệu chuyển động

Ưu tiên trích video trong kho khi chuyển động giúp minh họa ý, giữ ảnh khi ảnh rõ hơn. Nếu mở đầu nói nhiều quốc gia và có montage nhiều khung đúng bối cảnh, chọn đoạn thấy đồng thời các khung thay vì tự lắp nhãn quốc gia mới. Không coi nhãn trong video là xác minh địa điểm/ngày.

Nếu người dùng muốn **dừng lời dẫn để phát clip trích**, giữ khung A-roll đứng hình và làm mờ phía sau, chỉ phát tiếng clip trích trong khoảng chèn, rồi tiếp tục A-roll từ điểm dừng. Với ngày đăng đã ghi trong khung hình, xác định đúng vị trí trên clip sau khi scale/crop và cho vòng đỏ vẽ quanh ngày. Kiểm hình và tiếng ngay trước, trong và sau hai mối nối.

Đọc hồ sơ MEDIA, xem đúng khoảng định dùng rồi lưu source in/out, hash, proxy và crop trong job. Video tư liệu mặc định muted, CFR cùng fps, đủ frame cho cả entry/exit; một voice track chạy liên tục. Không cắt thêm lời dẫn chỉ để khớp B-roll. Clip dọc giữ tỷ lệ, cửa sổ rộng vừa safe zone; tránh chữ nguồn và phụ đề đè nhau. Crop các mép giao diện/bình luận không liên quan khi cần, lưu crop và giữ bản gốc; không cắt mất chi tiết làm đổi nghĩa.

## Kiểm và giao

Kiểm still trước/vào/giữa/ra và ở thời điểm từng ý đổi; đúng vị trí theo nội dung (chữ nhấn ở trên, card minh họa đặt theo vai trò và safe zone), không tràn/đè caption, mỗi đoạn một màu pastel ổn định; tên nguồn/ngày có sẵn đọc được. Xác nhận các matte được dùng tồn tại cho toàn khoảng, media không hết frame trước fade. Kiểm màu da trên A-roll rõ và split, grade không tác động tư liệu. Thử playback qua mối nối khi có khả năng; ghi đúng phạm vi đã kiểm, không nói đã nghe toàn clip khi chỉ xem still.

Ngày note của job mới lấy hôm nay theo múi giờ người dùng, lưu dữ liệu và dùng cùng giá trị cho preview/export. Khi chỉ khôi phục preview giữ ngày đã duyệt; khi người dùng yêu cầu đổi sang hôm nay, cập nhật cả metadata và overlay.


Quy tắc ngày khi render: **Mỗi lần bắt đầu render/xuất clip, luôn cập nhật ngày đầu clip thành hôm nay theo múi giờ người dùng**, ghi cùng ngày vào job và overlay trước khi bundle/render. Kiểm frame đầu từ file xuất để xác nhận. Chỉ mở/khôi phục preview thì không tự đổi ngày.
