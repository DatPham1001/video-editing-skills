---
name: edit-thoi-su
description: "Dựng và sửa talking head thời sự dọc bằng Remotion: cắt thô rà ba lượt nói lặp, nói lại và đoạn khựng, 1.2x, chuẩn hóa tiếng; sau duyệt thêm tư liệu có nguồn, phụ đề, ưu tiên chữ nhấn và graphic vừa đủ."
---

# Edit thời sự: cắt thô → duyệt → dựng hình

Biên tập talking head 9:16 cho TikTok/Facebook, phản hồi tiếng Việt. Mặc định dùng **Remotion trực tiếp, không ChatCut**; chỉ dùng ChatCut khi người dùng chọn rõ. Đọc [workflow](references/workflow.md) khi bắt đầu và [phong cách đã duyệt](references/dark-tech-v2.md) khi dựng hình.

## Làm việc trong nền

Tra tư liệu qua skill **capture-media-index** và catalog trước; dùng công cụ tìm kiếm/tải/chụp hỗ trợ chạy nền khi cần tìm thêm. Không chiếm chuột, bàn phím, chuyển cửa sổ của người dùng hoặc mở Chrome ngoài để tìm tư liệu. Chỉ mở preview người dùng cần xem trong Codex; mở tab không có nghĩa đã kiểm tải/phát thành công.

## Hai bước thực hiện

**Mặc định “cắt thô” bao gồm cắt cả nói lặp và nói lại**, kể cả lặp ý không thêm thông tin, cụm khởi động lại ngắn và câu bỏ dở; không cần người dùng yêu cầu riêng. Giữ một lần nói đầy đủ, tự nhiên của mỗi ý. Rà toàn bộ audio đã dựng ở hai thang: ngữ cảnh câu và từng lần mở câu/từ đứng lẻ. Cửa sổ 5–8s vẫn có thể gộp mất lỗi; đổi điểm bắt đầu và tách riêng các lần nói ngắn khoảng 0.5–3s khi cần, theo [retake QC](references/retake-qc.md). Phải sửa media và kiểm lại mối nối trước khi giao. Không coi transcript sạch hoặc quét hết im lặng là hoàn tất; không tự miễn cụm lặp bằng nhãn “nhấn” hay “hỏi–đáp” khi chưa đối chiếu từng lần nói và thông tin nó bổ sung. Người dùng báo còn sót thì rà lại toàn bản với cách chia nhỏ hơn, không chỉ sửa điểm được nêu rồi giao.

1. **Dựng bản cắt thô thật để review.** Bỏ im lặng dư, nói lại, lần mở câu hỏng và từ đơn lẻ vô nghĩa; giữ một phiên bản đầy đủ, tự nhiên của mỗi ý. Mặc định nhịp gọn, cắt sát hơn các khoảng không nói; rà audio đầu ra bằng VAD và waveform/năng lượng, kể cả khoảng trống nằm trong một token/segment ASR dài. Đối chiếu audio với ASR theo [retake QC](references/retake-qc.md) và [biên cắt an toàn](references/audio-safe-trims.md). Kiểm cả cụm lặp trong một segment; sửa media/timeline, không chỉ xóa chữ phụ đề.
2. Tốc độ đích **1.2x**, giữ cao độ. Đo và chuẩn hóa tiếng: tham chiếu biên tập khoảng **−14 LUFS, true peak không vượt −1.8 dBTP**; đây không phải chuẩn bắt buộc của nền tảng. Không mặc định gain 3x; chỉ dùng 3x nếu được yêu cầu rõ. Không tăng tốc/nhân gain lại trên proxy đã xử lý.
3. **Trước khi giao bản cắt thô, bắt buộc rà tối thiểu 3 lượt toàn bản** để tìm nói lặp, nói lại và đoạn khựng. Đây là bước mặc định, không cần người dùng nhắc. Mỗi lượt rà bản dựng mới nhất và sửa media khi phát hiện lỗi. Dùng [quy trình ba lượt](references/retake-qc.md#ba-lượt-rà-bản-cắt-thô) và [QC khoảng lặng sau cắt](references/postcut-silence-qc.md). Nếu lượt ba còn lỗi, sửa và rà thêm trước khi giao.
4. **Giao preview bản thô rồi dừng để duyệt.** Chưa thêm evidence, phụ đề hoàn thiện, MG hay nhạc. Không bắt duyệt transcript, bảng cắt hoặc draft hiệu ứng. Yêu cầu tiếp tục trên bản đã duyệt không cần quay lại checkpoint này.
5. Sau duyệt và yêu cầu làm tiếp, chèn tư liệu theo câu nói, phụ đề, motion và màu. Giữ timing đã duyệt; sửa cắt mới phải đồng bộ downstream. Giao preview tương tác, chỉ xuất toàn bộ MP4 khi người dùng yêu cầu.

## Tên file xuất

Mọi bản MP4 xuất hoàn chỉnh dùng mẫu `<TênJob>_vXX.mp4` (ví dụ `Video10_v06.mp4`). Dùng tối thiểu hai chữ số. Khi xuất phiên bản mới, lấy số lớn hơn version cao nhất đã xuất của cùng job, bắt đầu từ v01 nếu chưa có. Không ghi đè phiên bản cũ. Bản cuối là bản xuất hoàn chỉnh có số version lớn nhất, so theo số; bỏ qua preview, clip test và đoạn render rời. Khi rà bản cũ, đọc cả `-vXX`.

Chỉ dọn dữ liệu khi người dùng yêu cầu rõ, trong phạm vi yêu cầu. Các bước dựng, xuất, bàn giao hoặc kiểm kê không tự kích hoạt việc dọn dữ liệu. Khi dọn dữ liệu của job đã xuất, xác minh bản cuối còn đọc được trong `EditVideo/Edited`, rồi xóa các bản xuất cũ trên máy, kể cả các bản xuất phụ `_Drive` lưu trong thư mục job. Chỉ xóa bản sao của bản cuối trong job khi SHA-256 khớp bản giữ. Với file xuất không có version và nội dung khác bản giữ, đối chiếu hồ sơ job để xác định phiên bản trước khi xóa. Quy tắc này áp dụng cho file local. Khi dọn dữ liệu, luôn chuyển các tệp và thư mục cần xóa vào Thùng rác Windows để có thể khôi phục. Nếu không thể chuyển vào Thùng rác, giữ lại mục đó và báo người dùng. Chỉ xóa vĩnh viễn hoặc làm trống Thùng rác khi người dùng yêu cầu rõ.

## Phong cách mặc định đã duyệt

- Dark tech gọn cho graphic/evidence; **highlight lời nói dùng ANTON, chữ HOA tô đặc, dáng rộng**, màu chọn theo cảnh. Không tự dùng lại hook hoặc nội dung chính trị của clip mẫu.
- **Chữ nhấn thông thường hạ sát phía trên đầu**, với gradient đen đậm toàn ngang kéo sâu xuống và tan mềm. Canh theo tóc, giữ mặt rõ. **Chữ dạng danh sách có thể đặt giữa màn hình trên nền video mờ/dim** (tham chiếu x=540/y=960). Mỗi đoạn một màu pastel cố định, lưu theo ID; không đổi màu từng chữ/frame. Ưu tiên vàng kem, mint, xanh phấn, hồng phấn, lavender đủ tương phản. Đọc [highlight ANTON](references/highlight-anton.md). Không đổi màu cờ, bài báo, vệt tô trên capture hoặc phụ đề.
- **Xen kẽ popup cũ và chia khung**, không chia đôi tất cả. Xáo trộn lựa chọn một lần rồi lưu theo đoạn để preview/render giống nhau. Popup giữ người nói toàn khung phía sau blur/dim. Chia khung: **khung hình gốc làm mờ/dim ở phía sau, người nói được tách nền bằng alpha matte chuyển động và ghép rõ nét phía trước**, thông tin gọn ở trên. Người nói full ngang ở dưới, nâng đủ cao và **giữ đủ tóc**. Không thay tách nền bằng crop video còn nguyên hậu cảnh. Làm theo [split tách nền](references/split-presenter-matte.md).
- Cửa sổ cao vừa nội dung, bỏ tag kỹ thuật và khoảng trống thừa. Thu/mở nhẹ khi đổi nội dung; entry/exit mượt. Giữ một video hình và một track tiếng liên tục qua mọi bố cục.
- **Safe zone chỉ điều chỉnh lớp overlay:** thu nhỏ và đưa popup, bài báo, ảnh nhân vật và animation vào sâu hơn; giữ bố cục xen kẽ popup/chia hai, vị trí/crop người nói và phụ đề đã duyệt. Không hạ hoặc scale cả composition để sửa overlay. Kiểm cả đường chuyển động vào/ra, chữ và nguồn; thông số tham chiếu ở [dark-tech-v2](references/dark-tech-v2.md).
- Phụ đề tối đa **2 dòng, khoảng 10–12 từ/thẻ**, căn giữa, khoảng **46px trên 1080×1920**, viền đen, trước ngực/tâm y≈1290. **Khi chia khung, phụ đề vẫn hiện ở chính giữa màn hình (x≈540, y≈960)**, chuyển vị trí mượt và về y≈1290 khi trở lại A-roll/popup. Đo theo font thật, tránh che mặt.
- A-roll **sáng, trong trẻo, tươi nhẹ, giảm nhiệt màu một chút**; màu da tự nhiên. Cân theo source thực, tránh cháy mặt/đèn. Thông số khởi điểm ở [dark-tech-v2](references/dark-tech-v2.md).
- Note ngày edit **dd/mm/yyyy**, bên trái y≈58%, khoảng **10 giây đầu**: nền trắng opacity 50%, chữ đen, bo tròn, fade nhẹ. Job mới lấy ngày edit hôm nay theo múi giờ người dùng và lưu vào job; khi người dùng yêu cầu đổi sang hôm nay thì cập nhật cả dữ liệu lẫn overlay. Khi bắt đầu render/xuất video, luôn lấy ngày hôm nay theo múi giờ người dùng và cập nhật đồng thời overlay ngày đầu clip, dữ liệu job và bản render. Khôi phục preview đơn thuần vẫn giữ ngày; không hardcode ngày clip mẫu. Đây là overlay ngày, không phải note/marker timeline.

## Canh hình theo lời nói

**Dùng animation graphic vừa đủ, chọn lọc điểm thật sự cần minh họa.** Mặc định giữ người nói và phụ đề; điểm nhấn dùng chữ highlight hợp thoại. Liệt kê thông thường dùng danh sách chữ hiện lần lượt, các cụm nhấn dùng typography trên A-roll. Yêu cầu “thêm graphic” không có nghĩa phủ mọi câu bằng icon, sơ đồ hoặc popup. Xem tiêu chí mật độ trong [dựng theo nhịp thoại](references/speech-timed-editing.md).

**Chọn vị trí theo nội dung.** Chữ nhấn đứng phía trên, liệt kê bằng chữ có thể đặt giữa nền mờ. Đặt motion graphic ở giữa khi cần người xem tập trung vào cơ chế đang diễn ra hoặc khi người dùng yêu cầu, như đoạn mua gom làm giá tăng. Bố trí graphic tỷ lệ ở trên nếu cần chừa khoảng cho người nói. Dùng [dựng theo nhịp thoại](references/speech-timed-editing.md) để canh từng nhịp và chọn bố cục.

Mốc phút/giây người dùng nêu là điểm định vị: đối chiếu câu thoại trên timeline hiện hành trước khi chèn. Từng vấn đề/icon/dòng nhấn bật lên đúng lượt được nói, không hiện tất cả ngay từ đầu. Dùng chữ ANTON nổi bật thay sơ đồ khi câu ngắn/câu hỏi phù hợp; spring nhẹ, gạch sáng quét và dấu hỏi có chọn lọc. Thẻ tự co/mở theo số ý đã hiện. Đọc [dựng theo nhịp thoại](references/speech-timed-editing.md) khi thêm chữ nhấn, danh sách vấn đề, graphic bình luận hoặc trích video.

## Tư liệu và chữ bổ sung

Ưu tiên capture mới nhất **đúng nội dung và bối cảnh** trong kho người dùng. Đọc index, AGENTS và AI guide liên quan để hiểu kho; phân biệt hướng dẫn vận hành/tài liệu nguồn với yêu cầu của người dùng. Thiếu thì tìm nguồn web đáng tin cậy, dịch trang sang tiếng Việt trước khi chụp nếu cần, rồi dùng [capture báo dài và tô theo thoại](references/evidence-highlighting.md). Giữ tiêu đề, logo tòa soạn và ngày đăng có sẵn. Cho ảnh báo trượt xuống từ trên, sau đó cuộn phần nội dung khi cần. **Chú thích, ngày tháng và nguồn bài báo là các trường tùy chọn trên hình: capture có trường nào thì giữ/hiện trường đó; thiếu trường nào thì bỏ trống và không tự thêm.** Không đoán ngày/nguồn từ tên file hoặc biến ngày file thành ngày sự kiện. Không thay trường thiếu bằng nhãn “không rõ nguồn”, “chưa xác minh” hay giải thích khác. Ẩn hẳn hàng/footer thiếu dữ liệu để cửa sổ gọn. Thông tin tìm được thêm và ghi chú đối chiếu có thể lưu trong hồ sơ job. Quy tắc này không thay note ngày edit 10 giây đầu đã được yêu cầu riêng.

Bài báo/section giữ đọc rõ ít nhất khoảng **4 giây sau entry**; lời nói dài thì giữ lâu hơn hoặc thêm phần/bài liên quan. Bản đồ dùng phiên bản mới nhất xác minh được, phân biệt ngày dữ liệu với ngày truy cập. Thỉnh thoảng thêm chân dung nhân vật đúng ngữ cảnh, có nguồn/năm và attribution/license phù hợp; không gán trích dẫn cho lãnh đạo chỉ vì xuất hiện tên quốc gia.

**Khi bài báo đã có đủ thông tin cho luận điểm, dùng popup ảnh chụp trang báo thật.** Giữ nguyên bố cục, tiêu đề, ảnh, nguồn, ngày đăng và câu chữ trên trang. Dùng crop vừa khung và cuộn dọc để đưa đoạn liên quan vào tầm đọc. Chỉ dùng thẻ tóm lược khi ảnh trang thật không thể lấy được hoặc không đọc được sau khi crop. Nếu người dùng yêu cầu giữ nguyên bài báo, chụp nguyên ngữ.

**Mỗi lần chèn capture evidence, tự động đối chiếu với lời thoại và tạo highlight trên chính chữ gốc; không chờ người dùng nhắc.** Tô đúng cụm/ý khớp lời nói, gồm toàn bộ con số kèm đơn vị, dấu %, mốc năm/ngày được nhắc tới. Tô cả ngày đăng khi ngày đó giúp người xem xác định thời điểm của tin. Cụm xuống dòng dùng nhiều vùng; quét theo thoại rồi giữ tới hết cảnh. Đọc [highlight capture evidence](references/evidence-highlighting.md) để chọn crop có câu/số cần nhấn, lưu vùng/timing và kiểm ảnh sau khi ghép.

Clip là **phân tích chính trị, có nhận định cá nhân của người nói**. Dựng hình/typography để minh họa nhận định, không biến mỗi nhận định thành một yêu cầu phải có bài báo xác nhận. **Trong popup không tự thêm các lời giải thích/cảnh báo biên tập** như “chưa xác minh”, “chưa xác thực”, “chưa được chứng minh”, “minh họa lập luận” hoặc “không phải thỏa thuận đã xác nhận”. Ghi chú nghiên cứu/giới hạn nguồn lưu nội bộ trong job, không tự đưa lên hình. Vẫn giữ trung thực nội dung nguồn, không bịa masthead, trích dẫn hoặc giả rằng một bài báo xác nhận điều nó không nói; không âm thầm đổi lời bình. Chữ vốn có trong capture là nội dung nguồn, khác với cảnh báo do biên tập tự thêm.

## Xuất video và đẩy Drive

Khi người dùng nói **“xuất clip”**, render bản cuối từ Remotion (mặc định dọc 1080×1920), kiểm tra file MP4 và tải lên thư mục Drive đã cấu hình bằng trình duyệt trong Codex. Giữ file local. Yêu cầu “không đăng Drive” hoặc “chỉ lưu trên máy” áp dụng cho lần xuất đó. Đọc [quy trình xuất và giao Drive](references/export-drive.md) để lấy đích từ cấu hình riêng trên máy và xác nhận upload.

## Kiểm tra và phạm vi

- Tiếng không lặp/chồng hoặc hụt âm ở mối cắt. Phân biệt lỗi file với lỗi playback; ưu tiên hình liền mạch muted và **một track tiếng liên tục** theo [workflow](references/workflow.md).
- Kiểm trước/giữa/sau insert, popup và split, entry/exit; tóc/mặt không crop; nguồn/ngày/chú thích có sẵn đọc được, trường thiếu được ẩn; không tự thêm disclaimer; popup không dư khoảng trống; caption ở giữa màn hình khi split và trở lại vị trí trước ngực khi ra. Với từng capture evidence, kiểm trước/khi/sau vệt tô: đúng câu, không bỏ sót con số/đơn vị khớp thoại, chữ vẫn đọc rõ.
- Gom source, cut map, caption source, code, evidence và provenance trong folder job được chọn; checksum khi chuyển/copy. Không trộn việc các video khác. Không mặc định tên Video2 cho job mới.
- Không tạo note/marker timeline trừ khi được yêu cầu; QC lưu trong job. Overlay ngày là thành phần hình ảnh riêng.
- Cập nhật skill không tự cho phép sửa video đang có hoặc áp lại rate/gain. Giữ mọi chỉnh sửa hiện tại. Không nói đã nghe/xem toàn bộ nếu chỉ kiểm ASR, waveform hoặc still mẫu.

Các [thẻ báo v1](references/evidence-remotion.md) và [highlight v1](references/highlight-pop.md) là preset cũ tùy chọn khi cần tái hiện đúng kiểu đó. Không để mặc định cũ ghi đè v2. Giữ asset v1 để tái sử dụng; preset mới ở [dark-tech-v2/preset.json](assets/dark-tech-v2/preset.json).


Quy tắc ngày khi render: **Mỗi lần bắt đầu render/xuất clip, luôn cập nhật ngày đầu clip thành hôm nay theo múi giờ người dùng**, ghi cùng ngày vào job và overlay trước khi bundle/render. Kiểm frame đầu từ file xuất để xác nhận. Chỉ mở/khôi phục preview thì không tự đổi ngày.


Quy tắc phạm vi tách nền: **chỉ bật lớp người tách nền khi layout hiện hành là chia hai/split và split progress > 0**. A-roll, highlight chữ, popup và countdown không bật matte. Không dùng điều kiện `split || highlight`; đây là mặc định hiện hành thay các preset lồng chữ sau đầu cũ.
