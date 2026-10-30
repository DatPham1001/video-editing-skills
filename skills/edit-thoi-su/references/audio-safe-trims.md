# Biên cắt an toàn cho lời nói

Ưu tiên sửa theo góp ý mới nhất của người dùng: rõ lời và giữ trọn âm tiết quan trọng hơn việc xóa mọi mili giây ngắt. Không coi “cắt im lặng” là cắt sát từng token ASR. Đừng đánh đồng một token dài, âm nhỏ, hoặc đoạn chưa được nhận dạng với im lặng; có thể là đầu/đuôi từ hay cả từ bị ASR bỏ sót.

Kiểm nguồn âm thanh và waveform/VAD ở hai đầu từng đoạn giữ. Chừa biên đầu/đuôi thường0.1–0.2s theo thực tế; phụ âm đầu, tiếng nhỏ và đuôi nguyên âm có thể cần thêm. Giữ/nối lại các khoảng ngắt ngắn trong cùng câu khi có tín hiệu lời nói. Nếu chỉ dùng ASR/VAD, ghi rõ phương pháp, không tuyên bố đã nghe trực tiếp.

Khi sửa bản đã cắt quá sát, giữ quyết định chọn take hiện tại và nới handles cơ học thay vì chạy lại toàn bộ reflow theo timestamp ASR. Bảo vệ các khoảng source đã xác nhận là take thừa; không kéo handles sang lần nói lại đã bỏ. Chỉ nới trong source hợp lệ, không chồng/lặp audio giữa các đoạn giữ; chú ý sai số làm tròn frame. Nới biên phải bảo toàn gain, tốc độ và bố cục.

Với các gap ngắn giữa hai clip cùng source/cùng câu, có thể phục hồi gap thực thay vì nối âm tiết bị xén. Với gap lớn có thể chứa take hỏng, chỉ lấy biên đủ bảo vệ từ; không phục hồi cả gap. Dùng tín hiệu giọng nói và ngữ cảnh để quyết định, không áp một padding cố định cho mọi clip.

Backup timeline, lưu source mapping/gain/fade/caption/overlay/marker trước sửa. Tính lại duration và vị trí liên tục; đồng bộ các lớp hình theo những phần lời giữ, giữ trọn source range animation khi đổi duration. Xây lại crossfade rất ngắn sau khi biên đã đúng; crossfade không thay thế việc khôi phục từ đã mất và không được làm mờ phụ âm.

Kiểm lại source coverage và các vùng take thừa đã bảo vệ, so sánh nhận dạng trước/sau khi hữu ích. Xem composed frames để kiểm chữ/hình sau retime. Khi cần kiểm tiếng thực của renderer, dùng audio-only export một đoạn ngắn qua surface hiện tại để kiểm, không xuất toàn bộ video chỉ để QA. Không đổi âm lượng/tốc độ toàn bản nếu yêu cầu chỉ sửa hụt tiếng. Giữ checkpoint duyệt bản cắt thô của workflow hai bước.
