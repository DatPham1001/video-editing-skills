# Tự động rà khoảng không thoại sau cắt thô

Đọc và thực hiện sau mỗi lần tạo/sửa bản thô, trước khi giao preview. Không coi lần cắt đầu hoặc transcript sạch là đã đạt. Quy trình này được phép tự sửa khoảng không thoại trong phạm vi cắt thô, vẫn giữ checkpoint người dùng duyệt trước dựng hình.

## Vòng rà → sửa → đo lại

1. Lấy **audio đầu ra hiện tại** và cut map hiện tại; backup phiên bản trước sửa. Quét toàn thời lượng bằng VAD kết hợp waveform/năng lượng theo cửa sổ ngắn. Mặc định lập danh sách mọi khoảng nghi không thoại từ khoảng 0.5s trở lên, cả đầu/cuối, giữa câu và bên trong token/segment ASR kéo dài. Ngưỡng là mốc để rà, không phải lệnh xóa mọi khoảng vượt mốc.
2. Phân loại từng khoảng: ngừng dư, nhịp thở/ngắt nghĩa cần giữ, lời nhỏ tiếng bị VAD bỏ sót hoặc chưa xác định. VAD có thể bỏ sót từ đầu câu; ASR có thể kéo một từ qua nhiều giây im lặng. Đối chiếu ngữ cảnh trước/sau với tín hiệu thật; vùng chưa rõ dùng nghe trực tiếp hoặc ASR độc lập không VAD trên đoạn có ngữ cảnh. Không dùng riêng RMS trung bình để quyết định xóa, và không giữ nguyên cả khoảng trống chỉ vì nó nằm trong timestamp một từ.
3. Cắt khoảng ngừng dư đã xác nhận, thường giữ tổng nhịp nghỉ khoảng 0.2–0.35s và handles 0.1–0.2s theo âm thực. Bảo vệ phụ âm, đuôi từ, tiếng nhỏ và khoảng lấy hơi có ý nghĩa theo [biên cắt an toàn](audio-safe-trims.md). Không kéo vào take thừa đã bỏ. Sửa media/timeline thật, đồng bộ source map và mọi lớp downstream. Giữ tốc độ/gain hiện tại, không áp 1.2x hay chuẩn hóa chồng lần nữa lên proxy đã xử lý.
4. Tạo audio/preview mới rồi **quét lại toàn bộ audio mới** bằng cùng tiêu chí. Kiểm mối nối vừa sửa, duration/frame count, một track tiếng liên tục và đo lại loudness/true peak. Nếu còn khoảng ngừng dư hoặc lỗi biên cắt thì tự sửa và lặp lại; không giao bản chưa đạt chỉ vì đã chạy một lượt.

## Điều kiện dừng và hồ sơ QC

Chỉ kết thúc vòng tự rà khi không còn khoảng ngừng dư đã phát hiện, không còn ứng viên chưa được phân loại, các khoảng dài được giữ đều có lý do gắn ngữ cảnh (thở/ngắt nghĩa/lời nhỏ), và không có dấu hiệu hụt/lặp tiếng ở các mối nối mới. Lưu từng vòng: phiên bản, ngưỡng, danh sách khoảng, quyết định/lý do, source↔timeline mapping, tổng thời gian bỏ, kết quả quét lại và phương pháp kiểm. Không ép mọi khoảng ngắt về 0 hoặc xóa nhịp tự nhiên để vượt kiểm tra.

Nếu không thể phân biệt lời nhỏ với im lặng bằng phương tiện hiện có, giữ âm và báo rõ vùng chưa kết luận; không ghi QC đạt hoặc chạy vòng lặp vô hạn với cùng dữ liệu. Sau khi đạt, giao preview bản thô và dừng để người dùng duyệt; không tự chuyển sang evidence/phụ đề/MG.
