# Workflow thời sự hai bước

## Nhận và tổ chức

Tái dùng project hiện tại. Job mới dùng folder/tên/số người dùng chọn, chứa source, media/evidence, transcript/cut map, code Remotion, preview, QA và provenance. Không thay source gốc bằng proxy. Khi được yêu cầu gom/chuyển file, lập manifest đường dẫn/size/SHA-256, xác minh đích đúng workspace, dùng đường dẫn literal và kiểm checksum. Không chuyển junction/node_modules hoặc dữ liệu việc khác. Giữ proxy, source và code cùng job để dễ relink.

Mặc định Remotion trực tiếp, preview Studio mở. Nếu người dùng chọn ChatCut, dùng skill/surface tương ứng; không ép chuyển từ Remotion sang ChatCut. Preset v1 chỉ áp khi được chọn rõ.

## Bước 1 — cắt thô thật

1. Đọc metadata, fps, hướng xoay, audio và transcript. ASR để định vị, audio để xác nhận. Không bắt duyệt transcript trước khi dựng.
2. Bỏ ngừng dư, từ/cụm nói lại, lần mở câu hỏng, từ đơn lẻ vô nghĩa. Dùng [retake QC](retake-qc.md). Kiểm cả cụm lặp trong cùng segment, cụm ngắn và take ASR bỏ sót. Không xóa phủ định/chủ ngữ chỉ vì nhỏ tiếng.
3. Giữ trọn âm tiết; thường chừa 0.1–0.2s rồi tinh theo âm thực, không ép khoảng ngắt về 0. Dùng [biên cắt an toàn](audio-safe-trims.md). Crossfade ngắn khi cần, không chồng hai từ thành tiếng đôi.
4. Áp tốc độ đích 1.2x một lần, giữ cao độ. Đo loudness và chuẩn hóa: tham chiếu I≈−14 LUFS, TP≤−1.8 dBTP; đo lại đầu ra, không khẳng định đã đạt chỉ vì có filter. Gain 3x chỉ khi được yêu cầu, tính theo source gốc và kiểm clipping.
5. Lưu mapping source in/out → timeline frames, duration/fps thật và thông số đã áp. Tính lại mọi start/duration, không gap/overlap vô ý.
6. Giao preview cắt thô và **dừng để duyệt**, chưa evidence/phụ đề hoàn thiện/MG/nhạc. Hết thời gian chờ không phải duyệt. Sửa bản thô thì giao lại, không tự bước sang hoàn thiện.

Lưu trạng thái job: phase rough_cut_review, version, fps, duration_frames, cut map, tốc độ/loudness thực, approval. Không điền ID của phần mềm không dùng.

## Bước 2 — dựng sau duyệt

Lấy timing đã duyệt; không có checkpoint draft transcript/draft hiệu ứng bắt buộc. Đọc [phong cách dark-tech-v2](dark-tech-v2.md).

- Tìm kho capture trước, đọc index/agents/AI guide phù hợp. Ưu tiên ngày mới nhất đúng sự kiện. Không sửa baseline kho chỉ để chèn video; copy có hash/manifest vào job.
- Thiếu thì nghiên cứu web: báo uy tín, tài liệu chính thức cho số liệu, bản đồ có ngày dữ liệu. Chụp trang thật dạng điện thoại, crop theo kích thước pixel thực của PNG (có thể khác CSS viewport). Không dựng giả masthead/trích dẫn, không lấy ảnh paywall làm nội dung.
- Lưu URL, tác giả/tổ chức, ngày đăng/cập nhật/dữ liệu/truy cập, câu được hỗ trợ và giới hạn. Đăng lại cùng AP/Reuters là cùng một nguồn. Không biến nguồn mâu thuẫn thành xác nhận, không âm thầm sửa voice.
- Bài/section đọc rõ ít nhất khoảng 4s sau entry. Lời dài thì giữ lâu hơn hoặc thêm nguồn/section phù hợp. Chú thích/nguồn/ngày có sẵn trong capture thì giữ rõ; thiếu thì không cần tự thêm, không suy đoán hoặc thay bằng lời giải thích về thông tin thiếu. Ẩn hàng/footer không có dữ liệu. Ngày file chỉ dùng nội bộ, không tự làm ngày sự kiện. Video tư liệu muted trừ khi có chủ ý dùng tiếng của nó.
- Xen kẽ popup/split một lần theo nhịp/nội dung rồi lưu, không Math.random theo frame, không chia khung mọi insert. Popup: A-roll toàn khung blur/dim. Split: trên gọn, dưới full ngang, nâng người nói, giữ tóc; phụ đề ở giữa màn hình. Không remount/nhân đôi tiếng khi đổi layout.
- Safe zone: chỉ thu nhỏ/inset lớp báo, popup, graphic và chân dung; giữ panel/crop A-roll, phụ đề và cách xen kẽ đã duyệt. Không hạ toàn bộ bố cục. Dùng vùng/thông số tham chiếu trong [dark-tech-v2](dark-tech-v2.md), kiểm nội dung đọc rõ và cả entry/exit, đặc biệt footer với caption giữa màn hình khi split.
- Typography diễn tả lời nói: số nhảy, mức tăng, diện tích và so sánh có thể hiện lần lượt; không cần đủ 100 ô/chấm. So sánh tỉnh/vùng theo lời bình không tự bịa tên tỉnh hoặc ranh giới. Không dùng số liệu/hook của clip mẫu cho clip mới.
- Highlight theo [ANTON sau đầu](highlight-anton.md): HOA, tô đặc, rộng hơn; matte người trước chữ, gradient đen 1/3 trên, mặt cân sáng. Chọn bảng màu hợp nền thật rồi random một màu duy nhất cho mỗi đoạn, lưu theo ID/seed để preview/export ổn định; không đổi màu từng chữ hoặc random lại khi render.
- Ảnh nhân vật xuất hiện có chọn lọc, đúng ngữ cảnh, nguồn/năm/license; tránh mặt/caption. Giữ trích dẫn đúng người.
- Phụ đề 10–12 từ, 2 dòng, tâm trước ngực, viền đen; đo line width bằng font thật. Giữ sửa tên riêng/số liệu. Split chuyển phụ đề mượt đến tâm x≈540/y≈960; trở lại y≈1290 khi ra, không repaginate cả clip vì lỗi một chữ.
- Chỉnh A-roll sáng/trong/hơi lạnh; không áp grade của A-roll lên báo/phụ đề. Note ngày edit thật, trái y≈58%, trắng 50%, chữ đen, bo tròn, 10s đầu.
- Đây là phân tích chính trị có nhận định cá nhân: minh họa lời nói bằng hình/graphic, không ép mọi nhận định phải có báo xác nhận. Popup không tự thêm “chưa xác minh/chưa xác thực”, caveat hay nhãn “minh họa lập luận”. Giới hạn/đối chiếu nguồn ghi trong job; nguồn hiện trên hình vẫn trung thực, không bịa chữ trích hoặc sửa lời bình ngầm.

## Tiếng liền mạch và lỗi preview lặp âm

Ưu tiên proxy hình H.264 CFR đã bake cut/tốc độ, keyframe khoảng mỗi giây, muted; một PCM WAV chuẩn hóa cùng cut map chạy liên tục bằng Html5Audio. Đây là media làm việc, không phải tự xuất video hoàn thiện. Giữ source và mapping để dựng HD sau này.

Khi báo lặp: kiểm số audio/video và muted, decode đoạn lỗi ra PCM, kiểm cut ranges/timestamps/ASR/audio. Phân biệt lặp nằm trong file với trình duyệt tua lại lúc sync. Nếu file tốt mà preview lỗi, bake trim thành file liền và tách một track tiếng thay vì cắt thêm lời. Kiểm duration/frame count và so mẫu PCM với phép nối dự kiến khi phù hợp. Thử playback qua điểm lỗi và các chuyển layout/B-roll. Không tuyên bố chính xác nguyên nhân browser nếu chưa đo được.

## Sửa và giao

Sửa nói lặp phải sửa media/timeline và remap caption/evidence/MG/gain/fade liên quan, giữ sửa hiện có. Không quay job đã duyệt về bước1 vì skill thay đổi. Không tạo marker timeline; lưu QC trong job, ngoại trừ overlay ngày edit theo thiết kế.

QA: TypeScript; still entry/giữa/exit của popup/split; đủ tóc/mặt; metadata có sẵn đọc được, trường thiếu ẩn; không tự thêm disclaimer; card không dư khoảng trống; caption đúng trạng thái; thử audio và kiểm một voice track. Ghi đúng phạm vi kiểm. Giao preview tương tác ở phase final_edit_review. Chỉ export toàn video khi được yêu cầu rõ; xuất HD từ source gốc/cùng cut map, không phóng proxy thấp thành HD.


Khi được yêu cầu xuất và đẩy Drive, làm tiếp [xuất và giao Drive](export-drive.md). Đích mặc định là A.Tiktok clip, folder ID `1JyRWCQ7lxYcMST3SCGluOtYcjXdRYOuL`; chỉ xuất local thì không tự upload.
