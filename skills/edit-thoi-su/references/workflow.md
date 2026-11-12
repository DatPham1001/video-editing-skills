# Workflow thời sự hai bước

## Nhận và tổ chức

Tái dùng project hiện tại. Job mới dùng folder/tên/số người dùng chọn, chứa source, media/evidence, transcript/cut map, code Remotion, preview, QA và provenance. Không thay source gốc bằng proxy. Khi được yêu cầu gom/chuyển file, lập manifest đường dẫn/size/SHA-256, xác minh đích đúng workspace, dùng đường dẫn literal và kiểm checksum. Không chuyển junction/node_modules hoặc dữ liệu việc khác. Giữ proxy, source và code cùng job để dễ relink.

Mặc định Remotion trực tiếp; tra cứu, chuẩn bị media, render kiểm tra trong nền. Preview dùng tab trong Codex, không mở Chrome ngoài hoặc chuyển/chiếm chuột bàn phím khi người dùng đang làm việc. Nếu người dùng chọn ChatCut, dùng skill/surface tương ứng; không ép chuyển từ Remotion sang ChatCut. Preset v1 chỉ áp khi được chọn rõ.

## Bước 1 — cắt thô thật

1. Đọc metadata, fps, hướng xoay, audio và transcript. ASR để định vị, audio để xác nhận. Không bắt duyệt transcript trước khi dựng.
2. Mặc định cắt thô phải bỏ ngừng dư, nói lặp, nói lại, lặp ý không thêm thông tin, lần mở câu hỏng và từ đơn lẻ vô nghĩa. Dùng [retake QC](retake-qc.md), rà toàn bộ audio đầu ra bằng cửa sổ ngắn có chồng biên; không cần người dùng nhắc riêng việc cắt nói lặp/nói lại. Kiểm cả cụm lặp trong cùng segment, cụm ngắn và take ASR bỏ sót. Không xóa phủ định/chủ ngữ chỉ vì nhỏ tiếng.
3. Giữ trọn âm tiết, mặc định nhịp gọn: rà VAD/waveform/năng lượng trên cả source và đầu ra, kể cả khoảng không nói nằm trong segment ASR dài. Thử biên 60–100ms mỗi phía theo âm thực, nới khi tiếng nhỏ/phụ âm cần; không ép khoảng ngắt về 0. Rà các khoảng ngừng còn trên khoảng 400ms sau cắt. Dùng [biên cắt an toàn](audio-safe-trims.md). Crossfade ngắn khi cần, không chồng hai từ thành tiếng đôi.
4. Áp tốc độ đích 1.2x một lần, giữ cao độ. Đo loudness và chuẩn hóa: tham chiếu I≈−14 LUFS, TP≤−1.8 dBTP; đo lại đầu ra, không khẳng định đã đạt chỉ vì có filter. Gain 3x chỉ khi được yêu cầu, tính theo source gốc và kiểm clipping.
5. Lưu mapping source in/out → timeline frames, duration/fps thật và thông số đã áp. Tính lại mọi start/duration, không gap/overlap vô ý.
6. Chạy [tối thiểu 3 lượt rà toàn bản](retake-qc.md#ba-lượt-rà-bản-cắt-thô) cho nói lặp, nói lại và đoạn khựng, kết hợp [QC khoảng lặng sau cắt](postcut-silence-qc.md). Sau mỗi sửa, tạo lại media để lượt kế tiếp kiểm trên bản mới nhất. Lưu kết quả từng lượt và rà thêm nếu lượt cuối còn lỗi. Không áp lại tốc độ/gain lên media đã xử lý.
7. Giao preview cắt thô và **dừng để duyệt**, chưa evidence/phụ đề hoàn thiện/MG/nhạc. Hết thời gian chờ không phải duyệt. Sửa bản thô thì giao lại, không tự bước sang hoàn thiện.

Lưu trạng thái job: phase rough_cut_review, version, fps, duration_frames, cut map, tốc độ/loudness thực, approval. Không điền ID của phần mềm không dùng.

## Bước 2 — dựng sau duyệt

Lấy timing đã duyệt; không có checkpoint draft transcript/draft hiệu ứng bắt buộc. Đọc [phong cách dark-tech-v2](dark-tech-v2.md).

- Dùng skill capture-media-index tìm kho capture trước, đọc index/agents/AI guide phù hợp. Ưu tiên ngày mới nhất đúng sự kiện. Không sửa baseline kho chỉ để chèn video; copy có hash/manifest vào job.
- Thiếu thì nghiên cứu web: báo uy tín, tài liệu chính thức cho số liệu, bản đồ có ngày dữ liệu. Dùng [capture báo dài và tô theo thoại](evidence-highlighting.md) để dịch sang tiếng Việt trước khi chụp trang thật, giữ tiêu đề, logo và phần liên quan. Không dựng giả masthead/trích dẫn, không lấy ảnh paywall làm nội dung.
- Lưu URL, tác giả/tổ chức, ngày đăng/cập nhật/dữ liệu/truy cập, câu được hỗ trợ và giới hạn. Đăng lại cùng AP/Reuters là cùng một nguồn. Không biến nguồn mâu thuẫn thành xác nhận, không âm thầm sửa voice.
- Bài/section đọc rõ ít nhất khoảng 4s sau entry. Lời dài thì giữ lâu hơn hoặc thêm nguồn/section phù hợp. Chú thích/nguồn/ngày có sẵn trong capture thì giữ rõ; thiếu thì không cần tự thêm, không suy đoán hoặc thay bằng lời giải thích về thông tin thiếu. Ẩn hàng/footer không có dữ liệu. Ngày file chỉ dùng nội bộ, không tự làm ngày sự kiện. Video tư liệu muted trừ khi có chủ ý dùng tiếng của nó.
- Xen kẽ popup/split một lần theo nhịp/nội dung rồi lưu, không Math.random theo frame, không chia khung mọi insert. Popup: A-roll toàn khung blur/dim. Split: video nền gốc làm mờ/dim toàn khung; lớp người nói tách nền bằng alpha matte chuyển động rõ nét ở phía trước, phía dưới full ngang, nâng đủ cao và giữ tóc; thông tin gọn trên, phụ đề ở giữa màn hình. Bắt buộc kiểm matte đủ entry/hold/exit theo [split tách nền](split-presenter-matte.md), không giao bản crop còn nguyên hậu cảnh. Không remount/nhân đôi tiếng khi đổi layout.
- Safe zone: chỉ thu nhỏ/inset lớp báo, popup, graphic và chân dung; giữ panel/crop A-roll, phụ đề và cách xen kẽ đã duyệt. Không hạ toàn bộ bố cục. Dùng vùng/thông số tham chiếu trong [dark-tech-v2](dark-tech-v2.md), kiểm nội dung đọc rõ và cả entry/exit, đặc biệt footer với caption giữa màn hình khi split.
- Canh insert theo câu thoại thực, không chỉ theo mốc phút/giây gần đúng. Nếu project có retime, phân biệt local frame và master/source frame; lưu mapping trước khi đặt scene, tránh áp offset hai lần. Dùng [dựng theo nhịp thoại](speech-timed-editing.md) cho chữ nhấn và danh sách hiện từng ý.
- Typography diễn tả lời nói: số nhảy, mức tăng, diện tích và so sánh có thể hiện lần lượt; không cần đủ 100 ô/chấm. So sánh tỉnh/vùng theo lời bình không tự bịa tên tỉnh hoặc ranh giới. Không dùng số liệu/hook của clip mẫu cho clip mới.
- Highlight theo [ANTON theo nội dung](highlight-anton.md): HOA, tô đặc, màu pastel cố định theo đoạn. Chữ nhấn/animation thông thường ở phía trên đầu như bố cục đã duyệt; liệt kê bằng chữ có thể đặt giữa màn hình trên nền mờ/dim. Chọn vị trí graphic theo [nhịp thoại](speech-timed-editing.md). Giữ lựa chọn popup/split hiện hành và lưu placement/color theo ID để preview/export ổn định.
- Ảnh nhân vật xuất hiện có chọn lọc, đúng ngữ cảnh, nguồn/năm/license; tránh mặt/caption. Giữ trích dẫn đúng người.
- Phụ đề mặc định 46px trên 1080×1920, 10–12 từ, 2 dòng, tâm trước ngực, viền đen; đo line width bằng font thật. Giữ sửa tên riêng/số liệu. Split chuyển phụ đề mượt đến tâm x≈540/y≈960; trở lại y≈1290 khi ra, không repaginate cả clip vì lỗi một chữ.
- Chỉnh A-roll sáng/trong/hơi lạnh; không áp grade của A-roll lên báo/phụ đề. Note ngày edit thật, trái y≈58%, trắng 50%, chữ đen, bo tròn, 10s đầu.
- Đây là phân tích chính trị có nhận định cá nhân: minh họa lời nói bằng hình/graphic, không ép mọi nhận định phải có báo xác nhận. Popup không tự thêm “chưa xác minh/chưa xác thực”, caveat hay nhãn “minh họa lập luận”. Giới hạn/đối chiếu nguồn ghi trong job; nguồn hiện trên hình vẫn trung thực, không bịa chữ trích hoặc sửa lời bình ngầm.

## Tiếng liền mạch và lỗi preview lặp âm

Ưu tiên proxy hình H.264 CFR đã bake cut/tốc độ, keyframe khoảng mỗi giây, muted; một PCM WAV chuẩn hóa cùng cut map chạy liên tục bằng Html5Audio. Đây là media làm việc, không phải tự xuất video hoàn thiện. Giữ source và mapping để dựng HD sau này.

Khi báo lặp: kiểm số audio/video và muted, decode đoạn lỗi ra PCM, kiểm cut ranges/timestamps/ASR/audio. Phân biệt lặp nằm trong file với trình duyệt tua lại lúc sync. Nếu file tốt mà preview lỗi, bake trim thành file liền và tách một track tiếng thay vì cắt thêm lời. Kiểm duration/frame count và so mẫu PCM với phép nối dự kiến khi phù hợp. Thử playback qua điểm lỗi và các chuyển layout/B-roll. Không tuyên bố chính xác nguyên nhân browser nếu chưa đo được.

## Sửa và giao

Sửa nói lặp phải sửa media/timeline và remap caption/evidence/MG/gain/fade liên quan, giữ sửa hiện có. Không quay job đã duyệt về bước1 vì skill thay đổi. Không tạo marker timeline; lưu QC trong job, ngoại trừ overlay ngày edit theo thiết kế.

QA: TypeScript; still entry/giữa/exit của popup/split; đủ tóc/mặt; metadata có sẵn đọc được, trường thiếu ẩn; không tự thêm disclaimer; card không dư khoảng trống; caption đúng trạng thái; thử audio và kiểm một voice track. Ghi đúng phạm vi kiểm. Giao preview tương tác ở phase final_edit_review. Chỉ export toàn video khi được yêu cầu rõ; xuất HD từ source gốc/cùng cut map, không phóng proxy thấp thành HD.


Khi người dùng yêu cầu xuất clip, làm tiếp [xuất MP4 và giao Drive](export-drive.md) qua trình duyệt trong Codex. Nếu người dùng yêu cầu chỉ lưu local, kết thúc sau khi kiểm tra MP4.


Quy tắc ngày khi render: **Mỗi lần bắt đầu render/xuất clip, luôn cập nhật ngày đầu clip thành hôm nay theo múi giờ người dùng**, ghi cùng ngày vào job và overlay trước khi bundle/render. Kiểm frame đầu từ file xuất để xác nhận. Chỉ mở/khôi phục preview thì không tự đổi ngày.


Khi sửa hiện tượng giật ở bản render: đối chiếu khung hình MP4 với proxy/source cùng thời điểm; kiểm timestamp, frame lặp hoặc frame cũ, loại khoảng freeze có chủ ý. Ưu tiên OffthreadVideo cho hình video trong Remotion render để trích đúng frame, giữ một voice track liên tục. Kiểm lại mẫu từng có lỗi sau export; không coi đủ fps/duration là bằng chứng chuyển động mượt.
