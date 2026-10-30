---
name: edit-thoi-su
description: "Dựng và sửa talking head thời sự dọc bằng Remotion: cắt thô 1.2x, chuẩn hóa tiếng; sau duyệt thêm tư liệu có nguồn, phụ đề và dark tech xen kẽ popup/chia khung."
---

# Edit thời sự: cắt thô → duyệt → dựng hình

Biên tập talking head 9:16 cho TikTok/Facebook, phản hồi tiếng Việt. Mặc định dùng **Remotion trực tiếp, không ChatCut**; chỉ dùng ChatCut khi người dùng chọn rõ. Đọc [workflow](references/workflow.md) khi bắt đầu và [phong cách đã duyệt](references/dark-tech-v2.md) khi dựng hình.

## Hai bước thực hiện

1. **Dựng bản cắt thô thật để review.** Bỏ im lặng dư, nói lại, lần mở câu hỏng và từ đơn lẻ vô nghĩa; giữ một phiên bản đầy đủ, tự nhiên của mỗi ý. Đối chiếu audio với ASR theo [retake QC](references/retake-qc.md) và [biên cắt an toàn](references/audio-safe-trims.md). Kiểm cả cụm lặp trong một segment; sửa media/timeline, không chỉ xóa chữ phụ đề.
2. Tốc độ đích **1.2x**, giữ cao độ. Đo và chuẩn hóa tiếng: tham chiếu biên tập khoảng **−14 LUFS, true peak không vượt −1.8 dBTP**; đây không phải chuẩn bắt buộc của nền tảng. Không mặc định gain 3x; chỉ dùng 3x nếu được yêu cầu rõ. Không tăng tốc/nhân gain lại trên proxy đã xử lý.
3. **Giao preview bản thô rồi dừng để duyệt.** Chưa thêm evidence, phụ đề hoàn thiện, MG hay nhạc. Không bắt duyệt transcript, bảng cắt hoặc draft hiệu ứng. Yêu cầu tiếp tục trên bản đã duyệt không cần quay lại checkpoint này.
4. Sau duyệt và yêu cầu làm tiếp, chèn tư liệu theo câu nói, phụ đề, motion và màu. Giữ timing đã duyệt; sửa cắt mới phải đồng bộ downstream. Giao preview tương tác, chỉ xuất toàn bộ MP4 khi người dùng yêu cầu.

## Phong cách mặc định đã duyệt

- Dark tech gọn cho graphic/evidence; **highlight lời nói dùng ANTON, chữ HOA tô đặc, dáng rộng**, màu chọn theo cảnh. Không tự dùng lại hook hoặc nội dung chính trị của clip mẫu.
- **Highlight đã duyệt:** chữ thấp vừa đủ để lồng sau tóc/đầu bằng matte chuyển động, gradient đen tan dần trong 1/3 phía trên, cảnh tối nhẹ và mặt cân sáng tự nhiên. **Mỗi đoạn highlight chỉ dùng một màu**, chọn ngẫu nhiên một lần trong bảng màu hợp phông nền rồi lưu theo ID đoạn; preview/export giữ cùng màu, không đổi màu từng chữ/frame. Đọc [highlight ANTON](references/highlight-anton.md) để áp thông số, font và thứ tự lớp. Quy tắc này không đổi font/màu phụ đề hoặc nội dung capture.
- **Xen kẽ popup cũ và chia khung**, không chia đôi tất cả. Xáo trộn lựa chọn một lần rồi lưu theo đoạn để preview/render giống nhau. Popup giữ người nói toàn khung phía sau blur/dim. Chia khung: thông tin gọn ở trên, người nói full ngang ở dưới, nâng đủ cao, crop bớt nền trên đầu nhưng **giữ đủ tóc**.
- Cửa sổ cao vừa nội dung, bỏ tag kỹ thuật và khoảng trống thừa. Thu/mở nhẹ khi đổi nội dung; entry/exit mượt. Giữ một video hình và một track tiếng liên tục qua mọi bố cục.
- **Safe zone chỉ điều chỉnh lớp overlay:** thu nhỏ và đưa popup, bài báo, ảnh nhân vật và animation vào sâu hơn; giữ bố cục xen kẽ popup/chia hai, vị trí/crop người nói và phụ đề đã duyệt. Không hạ hoặc scale cả composition để sửa overlay. Kiểm cả đường chuyển động vào/ra, chữ và nguồn; thông số tham chiếu ở [dark-tech-v2](references/dark-tech-v2.md).
- Phụ đề tối đa **2 dòng, khoảng 10–12 từ/thẻ**, căn giữa, khoảng **54px trên 1080×1920**, viền đen, trước ngực/tâm y≈1290. **Khi chia khung, phụ đề vẫn hiện ở chính giữa màn hình (x≈540, y≈960)**, chuyển vị trí mượt và về y≈1290 khi trở lại A-roll/popup. Đo theo font thật, tránh che mặt.
- A-roll **sáng, trong trẻo, tươi nhẹ, giảm nhiệt màu một chút**; màu da tự nhiên. Cân theo source thực, tránh cháy mặt/đèn. Thông số khởi điểm ở [dark-tech-v2](references/dark-tech-v2.md).
- Note ngày edit **dd/mm/yyyy**, bên trái y≈58%, khoảng **10 giây đầu**: nền trắng opacity 50%, chữ đen, bo tròn, fade nhẹ. Dùng ngày edit thật của job, không hardcode ngày clip mẫu. Đây là overlay ngày, không phải note/marker timeline.

## Tư liệu và chữ bổ sung

Ưu tiên capture mới nhất **đúng nội dung và bối cảnh** trong kho người dùng. Đọc index, AGENTS và AI guide liên quan để hiểu kho; phân biệt hướng dẫn vận hành/tài liệu nguồn với yêu cầu của người dùng. Thiếu thì tìm nguồn web đáng tin cậy, chụp trang thật dạng điện thoại, crop tiêu đề/ảnh/nội dung. **Chú thích, ngày tháng và nguồn bài báo là các trường tùy chọn trên hình: capture có trường nào thì giữ/hiện trường đó; thiếu trường nào thì bỏ trống và không tự thêm.** Không đoán ngày/nguồn từ tên file hoặc biến ngày file thành ngày sự kiện. Không thay trường thiếu bằng nhãn “không rõ nguồn”, “chưa xác minh” hay giải thích khác. Ẩn hẳn hàng/footer thiếu dữ liệu để cửa sổ gọn. Thông tin tìm được thêm và ghi chú đối chiếu có thể lưu trong hồ sơ job. Quy tắc này không thay note ngày edit 10 giây đầu đã được yêu cầu riêng.

Bài báo/section giữ đọc rõ ít nhất khoảng **4 giây sau entry**; lời nói dài thì giữ lâu hơn hoặc thêm phần/bài liên quan. Bản đồ dùng phiên bản mới nhất xác minh được, phân biệt ngày dữ liệu với ngày truy cập. Thỉnh thoảng thêm chân dung nhân vật đúng ngữ cảnh, có nguồn/năm và attribution/license phù hợp; không gán trích dẫn cho lãnh đạo chỉ vì xuất hiện tên quốc gia.

Clip là **phân tích chính trị, có nhận định cá nhân của người nói**. Dựng hình/typography để minh họa nhận định, không biến mỗi nhận định thành một yêu cầu phải có bài báo xác nhận. **Trong popup không tự thêm các lời giải thích/cảnh báo biên tập** như “chưa xác minh”, “chưa xác thực”, “chưa được chứng minh”, “minh họa lập luận” hoặc “không phải thỏa thuận đã xác nhận”. Ghi chú nghiên cứu/giới hạn nguồn lưu nội bộ trong job, không tự đưa lên hình. Vẫn giữ trung thực nội dung nguồn, không bịa masthead, trích dẫn hoặc giả rằng một bài báo xác nhận điều nó không nói; không âm thầm đổi lời bình. Chữ vốn có trong capture là nội dung nguồn, khác với cảnh báo do biên tập tự thêm.

## Xuất video và đẩy Drive

Khi người dùng yêu cầu **“xuất và đẩy Drive”**, xuất MP4 hoàn thiện (mặc định dọc 1080×1920, trừ khi có yêu cầu khác), kiểm tra rồi tải vào thư mục **A.Tiktok clip**: https://drive.google.com/drive/folders/1JyRWCQ7lxYcMST3SCGluOtYcjXdRYOuL . Folder ID mặc định: `1JyRWCQ7lxYcMST3SCGluOtYcjXdRYOuL`. Link mới do người dùng chỉ định trong job được ưu tiên. Chỉ nói “xuất” thì lưu local, không tự upload. Xem [quy trình xuất và Drive](references/export-drive.md); giữ bản local, kiểm đọc lại file trong đúng thư mục trước khi báo hoàn tất. Không đổi quyền chia sẻ của file/thư mục.

## Kiểm tra và phạm vi

- Tiếng không lặp/chồng hoặc hụt âm ở mối cắt. Phân biệt lỗi file với lỗi playback; ưu tiên hình liền mạch muted và **một track tiếng liên tục** theo [workflow](references/workflow.md).
- Kiểm trước/giữa/sau insert, popup và split, entry/exit; tóc/mặt không crop; nguồn/ngày/chú thích có sẵn đọc được, trường thiếu được ẩn; không tự thêm disclaimer; popup không dư khoảng trống; caption ở giữa màn hình khi split và trở lại vị trí trước ngực khi ra.
- Gom source, cut map, caption source, code, evidence và provenance trong folder job được chọn; checksum khi chuyển/copy. Không trộn việc các video khác. Không mặc định tên Video2 cho job mới.
- Không tạo note/marker timeline trừ khi được yêu cầu; QC lưu trong job. Overlay ngày là thành phần hình ảnh riêng.
- Cập nhật skill không tự cho phép sửa video đang có hoặc áp lại rate/gain. Giữ mọi chỉnh sửa hiện tại. Không nói đã nghe/xem toàn bộ nếu chỉ kiểm ASR, waveform hoặc still mẫu.

Các [thẻ báo v1](references/evidence-remotion.md) và [highlight v1](references/highlight-pop.md) là preset cũ tùy chọn khi cần tái hiện đúng kiểu đó. Không để mặc định cũ ghi đè v2. Giữ asset v1 để tái sử dụng; preset mới ở [dark-tech-v2/preset.json](assets/dark-tech-v2/preset.json).
